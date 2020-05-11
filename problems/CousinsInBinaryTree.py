from entities import TreeNode

class Solution:
    def isCousinsDFS(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(node, parent, depth):
            if node is None:
                return
            if node.val == x:
                self.x_depth = depth
                self.x_parent = parent
            elif node.val == y:
                self.y_depth = depth
                self.y_parent = parent
            else:
                dfs(node.left, node, depth+1)
                dfs(node.right, node, depth+1)

        self.x_depth, self.y_depth = -1, -2
        self.x_parent, self.y_parent = None, None
        dfs(root, None, 0)
        return self.x_depth == self.y_depth and self.x_parent != self.y_parent

    def isConsinsBFS(self, root: TreeNode, x: int, y: int) -> bool:
        pass


"""
    Analysis
    Both methods need to traverse all nodes in worst case.

    DFS
    Time: O(n), Space: O(h)
    BFS
    Time: O(n), Space: O(n)

    n is the total number of nodes, h is the height of the binary tree

    TODO:
    Improve performance
"""




