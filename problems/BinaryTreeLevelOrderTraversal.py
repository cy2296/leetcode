from typing import List
from entities import TreeNode

class Solution:
    """
        BFS Solution
        Time: O(N)
        Space: O(N)
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        level = [root] if root else []

        while level:
            res = []  # current level result
            queue = []  # next level nodes
            for node in level:
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret.append(res)
            level = queue
        return ret

    """
        DFS Solution:
        Time: O(N)
        Space: O(N)
        
            3
           / \
          9  20
            /  \
           15   7
           
        dfs(root=3, level=0), ret: [] -> [[3]]
        |__dfs(root=9, level=1), ret: [[3]] -> [[3], [9]] 
        |__dfs(root=20, level=1), ret: [[3],[9]] -> [[3],[9,20]]
            |__dfs(root=15, level=2), ret: [[3],[9,20]] -> [[3],[9,20],[15]]
            |__dfs(root=7, level=2), ret: [[3],[9,20],[15]] -> [[3],[9,20],[15,7]]
    """
    def levelOrder_dfs(self, root: TreeNode) -> List[List[int]]:
        def dfs(root, level):
            if not root:
                return
            if len(ret) == level:
                ret.append([])
            ret[level].append(root.val)
            dfs(root.left, level+1)
            dfs(root.right, level+1)

        ret = []
        dfs(root, 0)
        return ret











