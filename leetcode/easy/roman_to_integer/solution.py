from typing import List

class Solution:
    
    def getElementByIdx(self, array: List[int], idx: int):
        if idx < len(array):
            return array[idx]

    def romanToInt(self, s: str) -> int:
        rule = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        nums = [rule.get(roman) for roman in s]
        result = 0
        i = 0

        while i < len(nums):
            currNum = nums[i]
            nextNum = self.getElementByIdx(nums, i+1)

            if nextNum and nextNum > currNum:
                result += nextNum-currNum
                i += 2
            else:
                result += currNum
                i += 1

        return result


if __name__ == '__main__':
    test_cases = 'I', 'III', 'IV', 'IX', 'LVIII', 'MCMXCIV'
    expected_result = 1, 3, 4, 9, 58, 1994

    solution = Solution()

    for idx, test_case in enumerate(test_cases):
        result = solution.romanToInt(test_case)
        print(f'{test_case}({expected_result[idx]}) -> {result}')
