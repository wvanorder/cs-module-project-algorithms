'''
Input: an integer
Returns: an integer
'''
import functools

# solution utilizing caching
# @functools.lru_cache(maxsize=256)
# def eating_cookies(n):
#     # Your code here
#     if n < 0:
#         return 0
#     if n == 0:
#         return 1
#     return eating_cookies(n - 1) + eating_cookies(n-2) + eating_cookies(n-3)

# solution utilizing a bottom-up approach


def eating_cookies(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    arr = [0] * (n + 1)
    arr[0], arr[1], arr[2], arr[3] = 0, 1, 2, 4

    for i in range(4, len(arr)):
        arr[i] = sum(arr[i-3:i])
    return arr[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
