string = "xy"
key = 1


def caesarCipherEncryptor2(string, key):
    ans = []
    k = key % 26
    for ch in string:
        if (ord(ch) + k) <= 122:
            ans.append(chr(ord(ch) + k))
        else:
            ans.append(chr(((ord(ch) + k) % 122) + 96))
    print(ans)
    return "".join(ans)


print(caesarCipherEncryptor2(string, key))


def caesarCipherEncryptor(string, key):
    ans = []
    k = key % 26
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    for ch in string:
        ans.append(alpha[(alpha.index(ch) + k) % 26])
    return "".join(ans)


print(caesarCipherEncryptor(string, key))
