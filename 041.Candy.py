# Candy
"""
"""
ratings = [1, 2, 3, 4, 5, 3, 2, 1, 2, 6, 5, 4, 3, 3, 2, 1, 1, 3, 3, 3, 4, 2]

result = 1
up = 1
down = peak = 0
for i in range(1, len(ratings)):
    # if rising, then update up/peak and clear down
    if ratings[i] > ratings[i - 1]:
        up += 1
        peak = up
        down = 0
        result += up
    # if equal, then add 1 and clear up/down/peak
    elif ratings[i] == ratings[i - 1]:
        up = 1
        down = 0
        peak = 0
        result += 1
    # if declining, then update down and clear up
    else:
        up = 1
        down += 1
        result += down
        # if peak is not large enough, then we need to make peak larger
        if peak <= down:
            result += 1


"""
Naive solution - find local minima and 
maxima then expand to both the sides -
One for loop and then 2 while loops 
to go left and right
"""
# Two pass solution
rewards = [1 for _ in ratings]
for i in range(1, len(ratings)):
    if ratings[i] > ratings[i - 1]:
        rewards[i] = rewards[i - 1] + 1
# rewards = [1,2,3,1]
for i in range(len(ratings) - 2, -1, -1):
    if ratings[i] > ratings[i + 1] and rewards[i] <= rewards[i + 1]:
        rewards[i] = rewards[i + 1] + 1

print(sum(rewards))
