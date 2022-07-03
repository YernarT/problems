from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 报错
'''
TypeError: object of type 'ListNode' has no len()
    for i in range(max(len(list1), len(list2))):
Line 14 in mergeTwoLists (Solution.py)
    ret = Solution().mergeTwoLists(param_1, param_2)
Line 47 in _driver (Solution.py)
    _driver()
Line 58 in <module> (Solution.py)
'''

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        result = []

        for i in range(max(len(list1), len(list2))):
            list1_el = list1[i]
            list2_el = list2[i]
            
            if list1_el > list2_el:
                result.extend([list2_el, list1_el])
            else:
                result.extend([list1_el, list2_el])

        return result


if __name__ == '__main__':
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]

    solution = Solution()
    result = solution.mergeTwoLists(l1, l2)

    print(result)

        