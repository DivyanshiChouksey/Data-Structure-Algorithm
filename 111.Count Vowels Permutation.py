from functools import lru_cache


dct = {
    ".": ["a", "e", "i", "o", "u"],
    "a": ["e"],
    "e": ["a", "i"],
    "i": ["a", "e", "o", "u"],
    "o": ["i", "u"],
    "u": ["a"],
}
n = 1


@lru_cache(None)
def helper(i, last):
    if i == n:
        return 1
    ans = 0
    for nxt in dct[last]:
        ans += helper(i + 1, nxt)
    return ans


print(helper(0, "."))
