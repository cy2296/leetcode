from entities import TreeNode

class Solution:
    """
        Recursive
        Time:
            O(N), it visits each node exactly once
        Space:
            O(log(N)) if the tree is balanced, can be O(N), if the tree is completely unbalanced
    """
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node, depth):
            if not node:
                return depth
            return max(dfs(node.left, depth+1), dfs(node.right, depth+1))
        return dfs(root, 0)

    """
        BFS Solution
    """
    def maxDepth_bfs(self, root: TreeNode) -> int:
        depth = 0
        level = [root] if root else []

        while level:
            depth += 1
            queue = []
            for node in level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level = queue

        return depth

    """
        Tail Recursion + BFS
        https://leetcode.com/problems/maximum-depth-of-binary-tree/solution/
        
        The benefit of having tail recursion, is that for certain programming languages (e.g. C++), 
        the compiler could optimize the memory allocation of call stack by reusing the same space for 
        every recursive call, rather than creating the space for each one. As a result, one could obtain 
        the constant space complexity O(1) for the overhead of the recursive calls.
        
        Note that the optimization of tail recursion is not supported by Python or Java.
    """