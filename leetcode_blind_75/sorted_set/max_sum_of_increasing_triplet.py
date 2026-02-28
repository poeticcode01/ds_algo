from sortedcontainers import SortedList

def max_sum_increasing_triplet(nums):
    n = len(nums)
    if n < 3:
        return 0

    right_max = [0] * n
    right_max[-1] = nums[-1]

    for i in range(n - 2, -1, -1):
        right_max[i] = max(nums[i], right_max[i + 1])

    left = SortedList()
    ans = 0

    for j in range(1, n - 1):
        left.add(nums[j - 1])

        idx = left.bisect_left(nums[j])

        if idx > 0 and right_max[j + 1] > nums[j]:
            left_val = left[idx - 1]
            ans = max(ans, left_val + nums[j] + right_max[j + 1])

    return ans

if __name__ == "__main__":
    nums = [2, 5, 3, 1, 4, 9]
    print(max_sum_increasing_triplet(nums))