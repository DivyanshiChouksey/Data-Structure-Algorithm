# Number of Ways to Divide a Long Corridor


corridor = "SSPPSPS"

def numberOfWays(corridor):
    MOD = ((10**9)+7)
    ans = 0
    seat1 = 0
    seat2= 1
    for obj in corridor:
        if obj=="S":
            ans = seat1
            seat1,seat2 = seat2,seat1
        else:
            seat2 = (seat2+ans)
    return ans%MOD


print( numberOfWays(corridor))
