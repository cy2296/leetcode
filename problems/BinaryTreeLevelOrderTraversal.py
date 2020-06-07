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
            cur = []  # current level result
            nxt = []  # next level nodes
            for node in level:
                cur.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            ret.append(cur)
            level = nxt
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
        def dfs(cur, level):
            if not cur:
                return

            if len(ret) == level:
                ret.append([])

            ret[level].append(cur.val)

            dfs(cur.left, level+1)
            dfs(cur.right, level+1)

        ret = []
        dfs(root, 0)
        return ret











