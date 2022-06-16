from typing import List


class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        # +1
        digits[len(digits)-1] += 1

        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 10:
                break
            else:
                digits[i] = 0

                if i != 0:
                    digits[i-1] += 1
                else:
                    digits.insert(0, 1)

        return digits


if __name__ == '__main__':
    digits = [1, 2, 3]
    # digits = [9, 9, 9]

    solution = Solution()
    result = solution.plusOne(digits)

    print(result)
