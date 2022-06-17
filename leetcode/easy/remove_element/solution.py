from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        
        return len(nums)


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3

    solution = Solution()
    result = solution.removeElement(nums, val)

    print(result)
