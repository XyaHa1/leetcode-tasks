from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])
        while queue:
            first, second = queue.popleft()

            if first is None and second is None:
                continue
            
            if first is None or second is None:
                return False

            if first.val != second.val :
                return False
            
            queue.append((first.left, second.left))
            queue.append((first.right, second.right))
        return True
    