# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head 
        
        # 런너를 이용해 역순 연결 리스트 구성
        # next 가 존재하지 않을 때까지 이동
        while fast and fast.next:
            fast = fast.next.next # 2칸씩
            # 역순 연결 리스트도 생성
            rev, rev.next, slow = slow, rev, slow.next # slow는 한 칸씩
        
        # 입력값이 홀수일 때
        if fast:
            # slow를 한 칸 더 이동해 마무리
            slow = slow.next
        
        # 역순 연결 리스트가 있고 이 값이 slow의 값과 같다면
        while rev and rev.val == slow.val:
            # 둘 다 한 칸씩 이동하며 비교
            slow, rev = slow.next, rev.next
        
        # 최종에는 끝까지 이동해 None이 됨 -> return True
        # rev에 값이 있다면 -> return False
        return not rev
        