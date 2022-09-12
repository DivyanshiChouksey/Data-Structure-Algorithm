# Bag of Tokens
"""
    taking greedy approach for maximizing score
    sort the tokens and take 2 pointer left(l) at starting of token and right(r) at the end of tokens
    if the tokens of left is less than or equal to the given power then increase score by 1 and power decrease by the tokens of left
    or if score is greater than or equal to "1" then increase the power by tokens of left minus tokens of right
    else break and return the score. 
 """

# Time Complexity = O(nlogn) || Space Complexity = O(1)

tokens = [100, 200, 300, 400]
power = 200


def bagOfTokensScore(tokens, power):
    tokens.sort()
    ans = 0
    l = 0
    r = len(tokens) - 1
    while l <= r:
        if tokens[l] <= power:
            ans += 1
            power -= tokens[l]
            l += 1
        elif ans >= 1:
            power += tokens[r] - tokens[l]
            r -= 1
            l += 1
        else:
            break
    return ans


print(bagOfTokensScore(tokens, power))
