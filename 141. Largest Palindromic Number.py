from typing import Counter


num = "444947137"
cnt = Counter(num)
first = ""
for ch in "9876543210":
    if ch == "0" and first == "":
        break
    first += ch * (cnt[ch] // 2)
    cnt[ch] %= 2
mid = ""
for ch in "9876543210":
    if cnt[ch]:  # check for first largest odd number to be in mid
        mid = ch
        break
print(first + mid + first[::-1])
