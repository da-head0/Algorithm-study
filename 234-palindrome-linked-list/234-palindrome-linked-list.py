# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        head_list = []
        head_copy = head
        while head:
            head_list.append(head.val)
            head = head.next
            
        while len(head_list) > 1:
            if head_list.pop(0) != head_list.pop():
                return False
        return True
        
        