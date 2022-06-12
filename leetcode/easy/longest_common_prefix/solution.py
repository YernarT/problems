from typing import List


class Solution:

    def __init__(self):
        self.result = ''

    def diff(self, string):
        if self.result == '':
            self.result = string
            return

        result = ''
        for i in range(min(len(self.result), len(string))):
            if self.result[i] == string[i]:
                result += self.result[i]
            else:
                break
        
        self.result = result

    def longestCommonPrefix(self, strs: List[str]) -> str:
        for string in strs:
            self.diff(string)

            if self.result == '':
                return ''

        return self.result


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    # strs = ["dog", "racecar", "car"]

    solution = Solution()
    result = solution.longestCommonPrefix(strs)

    print(result)
