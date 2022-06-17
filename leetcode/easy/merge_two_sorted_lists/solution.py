from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass
        


if __name__ == '__main__':
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]

    solution = Solution()
    result = solution.mergeTwoLists(l1, l2)

    print(result)

        