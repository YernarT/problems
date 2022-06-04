class Solution:

    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        if x < 10:
            return True

        x = str(x)

        return x == x[::-1]
        


if __name__ == '__main__':
    x = 123

    solution = Solution()
    result = solution.isPalindrome(x)

    print(result)

        