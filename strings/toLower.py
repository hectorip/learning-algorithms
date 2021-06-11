def toLower(s):
    r = ''
    for c in s:
        if 'A' <= c <= 'Z':
            r += chr(ord(c)+32)
        else:
            r += c
    return r
