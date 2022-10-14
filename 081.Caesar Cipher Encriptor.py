string = "xyz"
key = 2
dct = {}
out = ""
for i in range(26):
    dct[i] = chr(i + 97)

for ch in string:
    n = (ord(ch) + key - 97) % 26
    out += dct[n]
print(out)
