from entities import TreeNode

class Solution:
    def isCousins_dfs1(self, root: TreeNode, x: int, y: int) -> bool:
        self.x_depth, self.y_depth = 0, 0
        self.x_parent, self.y_parent = None, None

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

        dfs(root, None, 0)
        return self.x_depth == self.y_depth and self.x_parent != self.y_parent

    """
        LeetCode solution:
        1. Start traversing the tree from the root node. Look for Node x and Node y.
        2. Record the depth when the first node i.e. either of x or y is found and return true.
        3. Once one of the nodes is discovered, for every other recursive call after this discovery, 
           we return false if the current depth is more than the recorded depth. This basically means we 
           didn't find the other node at the same depth and there is no point going beyond. 
           This step of pruning helps to speed up the recursion by reducing the number of recursive calls.
        4. Return true when the other node is discovered and has the same depth as the recorded depth.
        5. Recurse the left and the right subtree of the current node. If both left and right recursions 
           return true and the current node is not their immediate parent, then Node x and Node y are cousins. 
           Thus, isCousin is set to value true.
    """
    def isConsins_dfs2(self, root: TreeNode, x: int, y: int) -> bool:
        # To save the depth of the first node.
        self.recorded_depth = None
        self.is_cousin = False

        def dfs(node, depth):
            if node is None:
                return False

            # Don't go beyond the depth restricted by the first node found
            if self.recorded_depth and depth > self.recorded_depth:
                return False

            if node.val == x or node.val == y:
                if self.recorded_depth is None:
                    # Save depth for the first node.
                    self.recorded_depth = depth
                # Return true, if the second node is found at the same depth.
                return self.recorded_depth == depth

            left = dfs(node.left, depth+1)
            right = dfs(node.right, depth+1)

            # self.recorded_depth != depth + 1 would ensure node x and y are not
            # immediate child nodes, otherwise they would become siblings.
            if left and right and self.recorded_depth != depth + 1:
                self.is_cousin = True

            return left or right

        dfs(root, 0)
        return self.is_cousin

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




