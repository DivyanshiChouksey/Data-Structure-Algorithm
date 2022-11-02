# Minimum Genetic Mutation

start = "AACCGGTT"
end = "AACCGGTA"
bank = ["AACCGGTA"]

# Time Complexity = O(n) || Space Complexity = O(n)

from collections import deque


def minMutation(start, end, bank):
    queue = deque([(start, 0)])
    seen = {start}

    while queue:
        node, steps = queue.popleft()
        if node == end:
            return steps

        for c in "ACGT":
            for i in range(len(node)):
                neighbor = node[:i] + c + node[i + 1 :]
                if neighbor not in seen and neighbor in bank:
                    queue.append((neighbor, steps + 1))
                    seen.add(neighbor)

    return -1


print(minMutation(start, end, bank))
