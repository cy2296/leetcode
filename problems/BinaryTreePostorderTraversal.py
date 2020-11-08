from typing import List
from entities import TreeNode


class Solution:
    """
        Iterative Solution:
        key point:
            1. Append data in the root->right->left order
            2. Return data in the reversed order

        Post (left, right, root): 45231

            1
           / \
          2   3
         / \
        4   5

        while: ret=[], stack=[], root=1
            |__ root: ret=[1], stack=[1], root=3
            |__ root: ret=[1,3], stack=[1,3], root=null
            |__ stack: ret=[1,3], stack=[1], root=null
            |__ stack: ret=[1,3], stack=[], root=2
            |__ root: ret=[1,3,2], stack=[2], root=5
            |__ root: ret=[1,3,2,5], stack=[2,5], root=null
            |__ stack: ret=[1,3,2,5], stack=[2], root=null
            |__ stack: ret=[1,3,2,5], stack=[], root=4
            |__ root: ret=[1,3,2,5,4], stack=[], root=null
            |__ return: ret[::-1]
    """
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        stack = []
        # getting root->right->left
        while root or stack:
            if root:
                ret.append(root.val)    # root
                stack.append(root)
                root = root.right       # right
            else:
                root = stack.pop()
                root = root.left        # left
        return ret[::-1]

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        s = []
        if root:
            s.append(root)
        while s:
            cur = s.pop()
            ret.append(cur.val)
            if cur.left:
                s.append(cur.left)
            if cur.right:
                s.append(cur.right)

        return ret[::-1]

    """
        Recursive
    """
    def postorderTraversal_resursive(self, root: TreeNode) -> List[int]:
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            ret.append(root.val)

        ret = []
        dfs(root)
        return ret
