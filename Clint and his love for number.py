import math


def is_prime(num):

    for val in range(2, int(math.sqrt(num)) + 1):

        if num % val == 0:

            return False

    return True


def largest_prime(num):

    maxp = 0

    n = int(math.sqrt(num)) + 1

    for val in range(2, n):

        if num % val == 0:

            if is_prime(val):

                maxp = max(maxp, val)

            if is_prime(num // val):

                maxp = max(maxp, num // val)

    if not maxp:

        return num

    return maxp


input1 = 20

l = largest_prime(input1)

if l == input1:

    count = 0

else:

    count = 1

input1 = l

while input1 > 0:

    while is_prime(input1):

        input1 -= 1

        count += 1

        if input1 == 0:

            print(count)

            break

    input1 = largest_prime(input1)

    count += 1


# input1 = 20
# arr = []
# for n in range(2, input1):
#     for i in range(2, n):
#         if n % i == 0:
#             break
#     else:
#         arr.append(n)
# ans = 0
# while input1 > 1:
#     for a in reversed(arr):
#         if input1 % a == 0 and a < input1:
#             input1 = a
#             break
#     else:
#         input1 -= 1
#     ans += 1
# print(ans + 1)
