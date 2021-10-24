from io import IncrementalNewlineDecoder
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

class Solution:
# 94. Binary Tree Inorder Traversal
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []         
        opt = [root.val]
        return self.inorderTraversal(root.left) + opt + self.inorderTraversal(root.right)

# 100. Same Tree
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None or q == None:
            return p == q
        
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
