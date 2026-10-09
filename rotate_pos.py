def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    if n <= 1:
        return

    k %= n

    def reverse(start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse the entire array
    reverse(0, n - 1)
    # Step 2: Reverse the first k elements
    reverse(0, k - 1)
    # Step 3: Reverse the remaining n - k elements
    reverse(k, n - 1)


# Example Walkthrough
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(arr, k)
print(arr)  # Output: [5, 6, 7, 1, 2, 3, 4]
