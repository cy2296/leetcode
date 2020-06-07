from typing import List
from entities import TreeNode

class Solution:
    """
        BFS Solution
        Time: O(N)
        Space: O(N)
    """
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        level = [root] if root else []
        cnt = 0

        while level:
            cur = []    # current level result
            nxt = []    # next level nodes
            for node in level:
                if cnt & 1:
                    cur.insert(0, node.val)
                else:
                    cur.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            ret.append(cur)
            level = nxt
            cnt += 1

        return ret


    def zigzagLevelOrder_dfs(self, root: TreeNode) -> List[List[int]]:
        def dfs(cur, level):
            if not cur:
                return

            if len(ret) == level:
                ret.append([])

            if level & 1:   # odd level
                ret[level].insert(0, cur.val)
            else:
                ret[level].append(cur.val)

            dfs(cur.left, level+1)
            dfs(cur.right, level+1)

        ret = []
        dfs(root, 0)
        return ret

