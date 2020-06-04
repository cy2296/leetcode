from typing import List
from entities import TreeNode

class Solution:
    """
        Iterative Solution:
        key points:
            1. While root OR stack
            2. In each while loop:
                - left: goes all the way to the left while adding nodes to the stack
                - root: pop the nodes from the stack and add to the result
                - right: switch to the right

        Inorder (Left, Root, Right): 42513

            1
           / \
          2   3
         / \
        4   5

        WHILE: ret=[], stack=[], root=1
            |__ while: ret=[], stack=[1], root=2
                |__ while: ret=[], stack=[1,2], root=4
                    |__ while: ret=[], stack=[1,2,4], root=null

            |__ pop: ret=[], stack=[1,2], root=4
            |__ add: ret=[4], stack=[1,2], root=null

        WHILE: ret=[4], stack=[1,2], root=null
            |__ pop: ret=[4], stack=[1], root=2
            |__ add: ret[4,2], stack=[1], root=5

        WHILE: ret=[4,2], stack=[1], root=5
            |__ while: ret=[4,2], stack=[1,5], root=null
            |__ pop: ret=[4,2], stack=[1], root=5
            |__ add: ret=[4,2,5], stack=[1], root=null

        WHILE: ret=[4,2,5], stack=[1], root=null
            |__ pop: ret=[4,2,5], stack=[], root=1
            |__ add: ret=[4,2,5,1], stack=[], root=3

        WHILE: ret=[4,2,5,1], stack=[], root=3
            |__ while: ret=[4,2,5,1], stack=[3], root=null
            |__ pop: ret=[4,2,5,1], stack=[], root=3
            |__ add: ret=[4,2,5,1,3], stack=[], root=null

    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ret.append(root.val)
            root = root.right
        return ret

    """
        Inorder (left, root, right): 42513

            1
           / \
          2   3
         / \
        4   5

        while: ret=[], stack=[], root=1
            |__ root: ret=[], stack=[1], root=2
            |__ root: ret=[], stack=[1,2], root=4
            |__ root: ret=[], stack=[1,2,4], root=null
            |__ stack: ret=[4], stack=[1,2], root=null
            |__ stack: ret=[4,2], stack=[1], root=5
            |__ root: ret=[4,2], stack=[1,5], root=null
            |__ stack: ret=[4,2,5], stack=[1], root=null
            |__ stack: ret=[4,2,5,1], stack=[], root=3
            |__ root: ret=[4,2,5,1,3], stack=[], root=null
    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left      # left
            else:
                root = stack.pop()
                res.append(root.val)  # root
                root = root.right     # right
        return res

    """
        Recursive Solution: easy
    """
    def inorderTraversal_resursive(self, root: TreeNode) -> List[int]:
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            ret.append(root.val)
            dfs(root.right)

        ret = []
        dfs(root)
        return ret
