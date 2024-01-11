from typing import List


def move_zeroes_to_end(nums: List[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[fast], nums[slow] = nums[slow], nums[fast]
            slow += 1
        print(nums)


nums = [0, 1, 7, 8, 0, 10, 0, 5, 9, 0]
move_zeroes_to_end(nums)
assert nums == [1, 7, 8, 10, 5, 9, 0, 0, 0, 0]

nums2 = [0, 0, 1]
move_zeroes_to_end(nums2)
assert nums2 == [1, 0, 0]

print("OK")
