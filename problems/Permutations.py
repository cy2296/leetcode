class Solution:
    """
        my solution: DFS
        Time: O(n*n!)
        Space: ?
    """
    def permute_dfs1(self, nums):
        def dfs(current, num_set):
            if len(current) == len(nums):
                ret.append(current)
                return

            for n in num_set:
                c = current.copy()
                n_set = num_set.copy()
                c.append(n)
                n_set.remove(n)
                dfs(c, n_set)

        ret = []
        dfs([], set(nums))
        return ret

    """
        Recursive solution
        Reference: 
        https://leetcode.com/problems/permutations/discuss/18296/Simple-Python-solution-(DFS).
        
        dfs(nums = [1, 2, 3] , path = [] , result = [] )
        |____ dfs(nums = [2, 3] , path = [1] , result = [] )
        |      |___dfs(nums = [3] , path = [1, 2] , result = [] )
        |      |    |___dfs(nums = [] , path = [1, 2, 3] , result = [[1, 2, 3]] ) # added a new permutation to the result
        |      |___dfs(nums = [2] , path = [1, 3] , result = [[1, 2, 3]] )
        |           |___dfs(nums = [] , path = [1, 3, 2] , result = [[1, 2, 3], [1, 3, 2]] ) # added a new permutation to the result
        |____ dfs(nums = [1, 3] , path = [2] , result = [[1, 2, 3], [1, 3, 2]] )
        |      |___dfs(nums = [3] , path = [2, 1] , result = [[1, 2, 3], [1, 3, 2]] )
        |      |    |___dfs(nums = [] , path = [2, 1, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] ) # added a new permutation to the result
        |      |___dfs(nums = [1] , path = [2, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] )
        |           |___dfs(nums = [] , path = [2, 3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] ) # added a new permutation to the result
        |____ dfs(nums = [1, 2] , path = [3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
               |___dfs(nums = [2] , path = [3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
               |    |___dfs(nums = [] , path = [3, 1, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] ) # added a new permutation to the result
               |___dfs(nums = [1] , path = [3, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] )
                    |___dfs(nums = [] , path = [3, 2, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] ) # added a new permutation to the result        
    """
    def dfs(self, nums, path, ret):
        if not nums:
            ret.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], ret)

    def permute_dfs2(self, nums):
        ret = []
        self.dfs(nums, [], ret)
        return ret

    """
        Iterative solution
        Reference:
        https://leetcode.com/problems/permutations/discuss/18237/My-AC-simple-iterative-javapython-solution
        
        Time: O(n*n!)
        Space: O(n*n!)
        
        nums = [1, 2, 3]
        perms = [[]]
        
        |___n=1 
            |__perm=[]
                |__i=0 --> [1]
            new_perms = [[1]]  
        |___n=2
            |__perm=[1]
                |__i=0 --> [2,1]
                |__i=1 --> [1,2]
            new_perms = [[2,1], [1,2]]
        |___n=3
            |__perm=[2,1]
                |__i=0 --> [3,2,1] 
                |__i=1 --> [2,3,1]
                |__i=2 --> [2,1,3]
            |__perm=[1,2]
                |__i=0 --> [3,1,2] 
                |__i=1 --> [1,3,2]
                |__i=2 --> [1,2,3]
            new_perms = [[3,2,1], [2,3,1], [2,1,3], [3,1,2], [1,3,2], [1,2,3]]    
    """
    def permute_bfs(self, nums):
        perms = [[]]
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm)+1):
                    new_perms.append(perm[:i] + [n] + perm[i:])  # insert n
            perms = new_perms
        return perms
