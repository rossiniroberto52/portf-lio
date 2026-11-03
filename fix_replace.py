with open('/home/rossini/portf-lio/index.html', 'r') as f:
    content = f.read()

old = "const desc = (r.description || '').replace(/&/g, '&').replace(/</g, '<').replace(/>/g, '>') || '\u2014';"
new = "const desc = (r.description || '').replace(/&/g, '&').replace(/</g, '<').replace(/>/g, '>') || '\u2014';"

if old in content:
    content = content.replace(old, new)
    with open('/home/rossini/portf-lio/index.html', 'w') as f:
        f.write(content)
    print('Fixed!')
else:
    print('Pattern not found')