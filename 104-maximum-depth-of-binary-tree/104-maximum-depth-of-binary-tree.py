# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = collections.deque([root])
        depth = 0
        
        while queue:
            depth += 1
            
            # 큐 연산 추출 노드의 자식 노드 삽입 -> 애초에 len(queue) 만큼만 반복해서 문제 없음
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right) 
                    
        # bfs 반복 횟수 == 깊이
        return depth
        