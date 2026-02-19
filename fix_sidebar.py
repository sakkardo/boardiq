content = open('app.py', encoding='utf-8').read()

old = '.sidebar{position:fixed;left:0;top:0;bottom:0;width:220px;background:var(--ink);display:flex;flex-direction:column;z-index:100;overflow-y:auto}'
new = '.sidebar{position:fixed;left:0;top:0;bottom:0;width:220px;background:var(--ink);display:flex;flex-direction:column;z-index:100;overflow-y:auto;min-height:0}'

if old in content:
    content = content.replace(old, new)
    print("Fixed with overflow-y version")
else:
    # Try original without overflow-y
    old2 = '.sidebar{position:fixed;left:0;top:0;bottom:0;width:220px;background:var(--ink);display:flex;flex-direction:column;z-index:100}'
    new2 = '.sidebar{position:fixed;left:0;top:0;bottom:0;width:220px;background:var(--ink);display:flex;flex-direction:column;z-index:100;overflow-y:auto}'
    if old2 in content:
        content = content.replace(old2, new2)
        print("Fixed original version")
    else:
        print("Could not find sidebar CSS - searching...")
        idx = content.find('.sidebar{')
        if idx >= 0:
            print(f"Found at index {idx}: {content[idx:idx+120]}")
        else:
            print("No .sidebar{ found in file")

open('app.py', 'w', encoding='utf-8').write(content)
print("Done")
