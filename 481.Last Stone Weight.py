# Last Stone Weight

stones = [2,7,4,1,8,1]

def lastStoneWeight(stones):
    heap = []
    for stone in stones:
        heappush(heap,(-stone))

    while len(heap)>1:
        x = heappop(heap)
        y = heappop(heap)
        if x!=y:
            heappush(heap,(x-y))

    return -(heap[-1]) if len(heap)!=0 else 0
  
print(lastStoneWeight(stones)
