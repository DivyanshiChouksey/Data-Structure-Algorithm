# Tandem Cycle
redShirtSpeeds = [5, 5, 3, 9, 2]  # 2,3,5,5,9
blueShirtSpeeds = [3, 6, 7, 2, 1]  # 1,2,3,6,7
fastest = True


def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    if fastest == False:
        redShirtSpeeds.sort(reverse=True)

    i = 0
    j = len(blueShirtSpeeds) - 1
    ans = 0
    while i < len(redShirtSpeeds) and j >= 0:
        ans += max(redShirtSpeeds[i], blueShirtSpeeds[j])
        i += 1
        j -= 1 

    return ans


print(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest))
