# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
            
        self.List = []
        self.recursion(self.List, root)
        return self.List

    def recursion(self, List, root):
        if root.left != None:
            self.recursion(List, root.left)
        
        List.append(root.val)

        if root.right != None:
            self.recursion(List, root.right)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

s = Solution()
print(s.inorderTraversal(a))