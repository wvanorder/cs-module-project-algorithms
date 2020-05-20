'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    if k % 2 == 0:
        extension = 1
        window_range = k // 2
    else:
        extension = 0
        window_range = 1 + k // 2
    # Your code here
    max_nums = []

    for i in range(k // 2, len(nums) - k // 2 + extension):
        max_nums.append(max(nums[i - k // 2: i + window_range]))
    return max_nums


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
