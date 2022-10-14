# Decode the Message

# Time Complexity = O(n+m) || Space Complexity = O(n)
key = "the quick brown fox jumps over the lazy dog"
msg = "vkbs bs t suepuv"


def decodeMessage(key, msg) -> str:
    alph = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    dct = {}
    for ch in key:
        if ch == " " or ch in dct:
            continue
        if i == 26:
            break
        else:
            dct[ch] = alph[i]
            i += 1
    ans = ""
    for ch in msg:
        if ch == " ":
            ans += " "
        else:
            ans += dct[ch]
    return ans


print(decodeMessage(key, msg))
