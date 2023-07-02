# Maximum Number of Achievable Transfer Requests

n = 5
requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]

def maximumRequests(n, requests):
    nr = len(requests)
    res = 0

    def test(mask):
        outd = [0] * n
        ind = [0] * n
        for k in range(nr):
            if (1 << k) & mask:
                outd[requests[k][0]] += 1
                ind[requests[k][1]] += 1
        return sum(outd) if outd == ind else 0

    for i in range(1 << nr):
        res = max(res, test(i))
    return res


print(maximumRequests(n, requests))
