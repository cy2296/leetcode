from typing import List
from entities import TreeNode

class Solution:
    """
        Iterative Solution:
        Time: O(n)
        Space: O(n)

        Preorder (Root, left, Right): 12453

            1
           / \
          2   3
         / \
        4   5

        while: ret=[], stack=[], root=1
            |__ root: ret=[1], stack=[1], root=2
            |__ root: ret=[1,2], stack=[1,2], root=4
            |__ root: ret=[1,2,4], stack=[1,2,4], root=null
            |__ stack: ret=[1,2,4], stack=[1,2], root=null
            |__ stack: ret=[1,2,4], stack=[1], root=5
            |__ root: ret=[1,2,4,5], stack=[1,5], root=null
            |__ stack: ret=[1,2,4,5], stack=[1], root=null
            |__ stack: ret=[1,2,4,5], stack=[], root=3
            |__ root: ret=[1,2,4,5,3], stack=[3], root=null
            |__ stack: ret=[1,2,4,5,3], stack=[], root=null
    """
    def preorderTraversal_iter1(self, root: TreeNode) -> List[int]:
        ret = []
        stack = []
        while root or stack:
            if root:
                ret.append(root.val)    # root
                stack.append(root)
                root = root.left        # left
            else:
                root = stack.pop()
                root = root.right       # right
        return ret

    """
        ret=[], s=[1]
        ret=[1], s=[3,2]
        ret=[1,2] s=[3,5,4]
        ret=[1,2,4] s=[3,5]
        ret=[1,2,4,5], s=[3]
        ret=[1,2,4,5,3], s=[]   
    """
    def preorderTraversal_iter2(self, root: TreeNode) -> List[int]:
        ret = []
        stack = []
        if root:
            stack.append(root)

        while stack:
            cur = stack.pop()
            ret.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

        return ret

    """
        Recursive:
        Time: O(N)
        Space: O(1)
        
        Might suffer from the stack overflow issue when the tree depth is too large 
    """
    def preorderTraversal_resursive(self, root: TreeNode) -> List[int]:
        def dfs(root):
            if not root:
                return
            ret.append(root.val)
            dfs(root.left)
            dfs(root.right)

        ret = []
        dfs(root)
        return ret

    """
        Further reference: 
        9 solutions: 
        Morris Traversal:
        Time: O(n)
        Space: O(1)
        https://github.com/liuyubobobo/Play-Leetcode/blob/master/0145-Binary-Tree-Postorder-Traversal/java-0145/src/Solution9.java
    """
