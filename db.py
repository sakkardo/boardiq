"""
BoardIQ — PostgreSQL persistence layer
========================================
Uses DATABASE_URL env var (provided by Railway).
Falls back gracefully to in-memory-only mode when no database is configured.

Tables:
  - vendor_data: building vendor spend records (BBL + vendor + category)
  - vendor_profiles: full vendor profile JSON (keyed by vendor_id)
  - vendor_registry: vendor login credentials (keyed by email)
"""

import os
import json
import traceback

_db_url = os.environ.get("DATABASE_URL")
_pool = None

def _get_pool():
    global _pool
    if _pool is not None:
        return _pool
    if not _db_url:
        return None
    try:
        import psycopg2.pool
        # Railway provides postgres:// but psycopg2 needs postgresql://
        url = _db_url
        if url.startswith("postgres://"):
            url = url.replace("postgres://", "postgresql://", 1)
        _pool = psycopg2.pool.SimpleConnectionPool(1, 5, url)
        print("[BoardIQ DB] Connected to PostgreSQL")
        return _pool
    except Exception as e:
        print(f"[BoardIQ DB] Could not connect to PostgreSQL: {e}")
        return None


def _get_conn():
    pool = _get_pool()
    if pool is None:
        return None
    return pool.getconn()


def _put_conn(conn):
    pool = _get_pool()
    if pool and conn:
        pool.putconn(conn)


# ── Schema creation ──────────────────────────────────────────────────────────

def init_db():
    """Create tables if they don't exist. Safe to call on every startup."""
    conn = _get_conn()
    if conn is None:
        print("[BoardIQ DB] No database configured — running in-memory only")
        return False
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS vendor_data (
                bbl TEXT NOT NULL,
                vendor TEXT NOT NULL,
                category TEXT NOT NULL,
                annual DOUBLE PRECISION,
                per_unit DOUBLE PRECISION,
                last_bid_year INTEGER,
                months_left INTEGER,
                last_invoice_date TEXT,
                last_invoice_amount DOUBLE PRECISION,
                extra JSONB DEFAULT '{}',
                PRIMARY KEY (bbl, vendor, category)
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS vendor_profiles (
                vendor_id TEXT PRIMARY KEY,
                data JSONB NOT NULL DEFAULT '{}'
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS vendor_registry (
                email TEXT PRIMARY KEY,
                vendor_id TEXT NOT NULL,
                password TEXT NOT NULL,
                data JSONB NOT NULL DEFAULT '{}'
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS building_contracts (
                contract_id TEXT PRIMARY KEY,
                building_bbl TEXT NOT NULL,
                data JSONB NOT NULL DEFAULT '{}'
            );
        """)
        cur.execute("""
            CREATE INDEX IF NOT EXISTS idx_contracts_bbl ON building_contracts(building_bbl);
        """)
        conn.commit()
        cur.close()
        print("[BoardIQ DB] Tables ready (including contracts)")
        return True
    except Exception as e:
        conn.rollback()
        print(f"[BoardIQ DB] Error creating tables: {e}")
        traceback.print_exc()
        return False
    finally:
        _put_conn(conn)


# ── Vendor Data (building spend records) ─────────────────────────────────────

def load_all_vendor_data():
    """Load all building vendor_data from DB. Returns {bbl: [vendor_dict, ...]}."""
    conn = _get_conn()
    if conn is None:
        return {}
    try:
        cur = conn.cursor()
        cur.execute("SELECT bbl, vendor, category, annual, per_unit, last_bid_year, months_left, last_invoice_date, last_invoice_amount FROM vendor_data")
        rows = cur.fetchall()
        cur.close()
        result = {}
        for bbl, vendor, category, annual, per_unit, last_bid_year, months_left, inv_date, inv_amount in rows:
            entry = {
                "vendor": vendor,
                "category": category,
                "annual": annual,
                "per_unit": per_unit,
                "last_bid_year": last_bid_year,
                "months_left": months_left,
            }
            if inv_date:
                entry["last_invoice_date"] = inv_date
            if inv_amount is not None:
                entry["last_invoice_amount"] = inv_amount
            result.setdefault(bbl, []).append(entry)
        print(f"[BoardIQ DB] Loaded vendor data for {len(result)} buildings")
        return result
    except Exception as e:
        print(f"[BoardIQ DB] Error loading vendor data: {e}")
        return {}
    finally:
        _put_conn(conn)


def save_building_vendor_data(bbl, vendor_list):
    """Upsert all vendor records for a single building."""
    conn = _get_conn()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        # Delete existing rows for this building, then insert fresh
        cur.execute("DELETE FROM vendor_data WHERE bbl = %s", (bbl,))
        for v in vendor_list:
            cur.execute("""
                INSERT INTO vendor_data (bbl, vendor, category, annual, per_unit, last_bid_year, months_left, last_invoice_date, last_invoice_amount)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                bbl,
                v.get("vendor", ""),
                v.get("category", ""),
                v.get("annual"),
                v.get("per_unit"),
                v.get("last_bid_year"),
                v.get("months_left"),
                v.get("last_invoice_date"),
                v.get("last_invoice_amount"),
            ))
        conn.commit()
        cur.close()
    except Exception as e:
        conn.rollback()
        print(f"[BoardIQ DB] Error saving vendor data for {bbl}: {e}")
    finally:
        _put_conn(conn)


def save_all_vendor_data(buildings_db):
    """Persist vendor_data for every building that has it."""
    conn = _get_conn()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM vendor_data")
        count = 0
        for bbl, building in buildings_db.items():
            for v in building.get("vendor_data", []):
                cur.execute("""
                    INSERT INTO vendor_data (bbl, vendor, category, annual, per_unit, last_bid_year, months_left, last_invoice_date, last_invoice_amount)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    bbl,
                    v.get("vendor", ""),
                    v.get("category", ""),
                    v.get("annual"),
                    v.get("per_unit"),
                    v.get("last_bid_year"),
                    v.get("months_left"),
                    v.get("last_invoice_date"),
                    v.get("last_invoice_amount"),
                ))
                count += 1
        conn.commit()
        cur.close()
        print(f"[BoardIQ DB] Saved {count} vendor data rows")
    except Exception as e:
        conn.rollback()
        print(f"[BoardIQ DB] Error in save_all_vendor_data: {e}")
    finally:
        _put_conn(conn)


# ── Vendor Profiles ──────────────────────────────────────────────────────────

def load_all_vendor_profiles():
    """Returns {vendor_id: profile_dict}."""
    conn = _get_conn()
    if conn is None:
        return {}
    try:
        cur = conn.cursor()
        cur.execute("SELECT vendor_id, data FROM vendor_profiles")
        rows = cur.fetchall()
        cur.close()
        result = {}
        for vid, data in rows:
            profile = data if isinstance(data, dict) else json.loads(data)
            profile["vendor_id"] = vid
            result[vid] = profile
        print(f"[BoardIQ DB] Loaded {len(result)} vendor profiles")
        return result
    except Exception as e:
        print(f"[BoardIQ DB] Error loading vendor profiles: {e}")
        return {}
    finally:
        _put_conn(conn)


def save_vendor_profile(vendor_id, profile):
    """Upsert a single vendor profile."""
    conn = _get_conn()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        data = json.dumps(profile, default=str)
        cur.execute("""
            INSERT INTO vendor_profiles (vendor_id, data)
            VALUES (%s, %s::jsonb)
            ON CONFLICT (vendor_id) DO UPDATE SET data = EXCLUDED.data
        """, (vendor_id, data))
        conn.commit()
        cur.close()
    except Exception as e:
        conn.rollback()
        print(f"[BoardIQ DB] Error saving vendor profile {vendor_id}: {e}")
    finally:
        _put_conn(conn)


def save_all_vendor_profiles(profiles_dict):
    """Bulk save all vendor profiles."""
    conn = _get_conn()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        for vid, profile in profiles_dict.items():
            data = json.dumps(profile, default=str)
            cur.execute("""
                INSERT INTO vendor_profiles (vendor_id, data)
                VALUES (%s, %s::jsonb)
                ON CONFLICT (vendor_id) DO UPDATE SET data = EXCLUDED.data
            """, (vid, data))
        conn.commit()
        cur.close()
        print(f"[BoardIQ DB] Saved {len(profiles_dict)} vendor profiles")
    except Exception as e:
        conn.rollback()
        print(f"[BoardIQ DB] Error in save_all_vendor_profiles: {e}")
    finally:
        _put_conn(conn)


# ── Vendor Registry ──────────────────────────────────────────────────────────

def load_all_vendor_registry():
    """Returns {email: {vendor_id, password, ...}}."""
    conn = _get_conn()
    if conn is None:
        return {}
    try:
        cur = conn.cursor()
        cur.execute("SELECT email, vendor_id, password, data FROM vendor_registry")
        rows = cur.fetchall()
        cur.close()
        result = {}
        for email, vid, pw, data in rows:
            entry = data if isinstance(data, dict) else json.loads(data) if data else {}
            entry["vendor_id"] = vid
            entry["password"] = pw
            result[email] = entry
        print(f"[BoardIQ DB] Loaded {len(result)} vendor registry entries")
        return result
    except Exception as e:
        print(f"[BoardIQ DB] Error loading vendor registry: {e}")
        return {}
    finally:
        _put_conn(conn)


def save_vendor_registry_entry(email, entry):
    """Upsert a single vendor registry entry."""
    conn = _get_conn()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        vid = entry.get("vendor_id", "")
        pw = entry.get("password", "")
        # Store extra fields beyond vendor_id/password in data column
        extra = {k: v for k, v in entry.items() if k not in ("vendor_id", "password")}
        data = json.dumps(extra, default=str)
        cur.execute("""
            INSERT INTO vendor_registry (email, vendor_id, password, data)
            VALUES (%s, %s, %s, %s::jsonb)
            ON CONFLICT (email) DO UPDATE SET vendor_id = EXCLUDED.vendor_id, password = EXCLUDED.password, data = EXCLUDED.data
        """, (email, vid, pw, data))
        conn.commit()
        cur.close()
    except Exception as e:
        conn.rollback()
        print(f"[BoardIQ DB] Error saving vendor registry for {email}: {e}")
    finally:
        _put_conn(conn)


def has_database():
    """Check if a database is available."""
    return _get_pool() is not None


# ── Building Contracts ──────────────────────────────────────────────────────

def load_all_contracts():
    """Load all contracts from DB. Returns {contract_id: contract_dict}."""
    conn = _get_conn()
    if conn is None:
        return {}
    try:
        cur = conn.cursor()
        cur.execute("SELECT contract_id, building_bbl, data FROM building_contracts")
        rows = cur.fetchall()
        cur.close()
        result = {}
        for cid, bbl, data in rows:
            contract = data if isinstance(data, dict) else json.loads(data)
            contract["contract_id"] = cid
            contract["building_bbl"] = bbl
            result[cid] = contract
        print(f"[BoardIQ DB] Loaded {len(result)} contracts")
        return result
    except Exception as e:
        print(f"[BoardIQ DB] Error loading contracts: {e}")
        return {}
    finally:
        _put_conn(conn)


def save_contract(contract_id, contract):
    """Upsert a single contract."""
    conn = _get_conn()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        bbl = contract.get("building_bbl", "")
        data = json.dumps(contract, default=str)
        cur.execute("""
            INSERT INTO building_contracts (contract_id, building_bbl, data)
            VALUES (%s, %s, %s::jsonb)
            ON CONFLICT (contract_id) DO UPDATE SET building_bbl = EXCLUDED.building_bbl, data = EXCLUDED.data
        """, (contract_id, bbl, data))
        conn.commit()
        cur.close()
    except Exception as e:
        conn.rollback()
        print(f"[BoardIQ DB] Error saving contract {contract_id}: {e}")
    finally:
        _put_conn(conn)


def save_all_contracts(contracts_dict):
    """Bulk save all contracts."""
    conn = _get_conn()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        for cid, contract in contracts_dict.items():
            bbl = contract.get("building_bbl", "")
            data = json.dumps(contract, default=str)
            cur.execute("""
                INSERT INTO building_contracts (contract_id, building_bbl, data)
                VALUES (%s, %s, %s::jsonb)
                ON CONFLICT (contract_id) DO UPDATE SET building_bbl = EXCLUDED.building_bbl, data = EXCLUDED.data
            """, (cid, bbl, data))
        conn.commit()
        cur.close()
        print(f"[BoardIQ DB] Saved {len(contracts_dict)} contracts")
    except Exception as e:
        conn.rollback()
        print(f"[BoardIQ DB] Error in save_all_contracts: {e}")
    finally:
        _put_conn(conn)
