from typing import List

from collections import Counter

class Solution:
    """
    Reference:
    https://leetcode.com/problems/permutations-ii/discuss/18594/Really-easy-Java-solution-much-easier-than-the-solutions-with-very-high-vote

    Sort the array first, then use a boolean array to mark the elements after used, for the duplicates we can choose
    either always placing element with smaller index before element with larger index (scenario 1), or the other way
    around (scenario 2).

    Both scenario works:
    1. if i > 0 and nums[i] == nums[i-1] and not used[i-1]: continue
    2. if i > 0 and nums[i] == nums[i-1] and used[i-1]: continue

    for example:
    nums = [A, B, B'], used = [0, 0, 0]

    Scenario 1:
        if i > 0 and nums[i] == nums[i-1] and not used[i-1]: continue

    dfs(perm=[], used=[0,0,0], nums, ret=[])
    |__i=0: dfs(perm=[A], used=[1,0,0], nums, ret=[])
            |__i=0: x
            |__i=1: dfs(perm=[A,B], used=[1,1,0], nums, ret=[])
                |__i=0: x
                |__i=1: x
                |__i=2: dfs(perm=[A,B,B'], used=[1,1,1], nums, ret=[]) --> add [A,B,B'] to ret
            |__i=2: x
    |__i=1: dfs(perm=[B], used=[0,1,0], nums, ret=[[A,B,B']])
            |__i=0: dfs(perm=[B,A], used=[1,1,0], nums, ret=[[A,B,B']])
                    |__i=0: x
                    |__i=1: x
                    |__i=2: dfs(perm=[B,A,B'], used=[1,1,1], nums, ret=[[A,B,B']]) --> add [B,A,B'] to ret
            |__i=1: x
            |__i=2: dfs(perm=[B,B'], used=[0,1,1], nums, ret=[[A,B,B'], [B,A,B']])
                    |__i=0: dfs(perm=[B,B'A], used=[1,1,1], nums, ret=[[A,B,B'], [B,A,B']]) --> add [B,B'A] to ret
                    |__i=1: x
                    |__i=2: x
    |__i=2: x
    Final result: [[A,B,B'], [B,A,B'], [B,B'A]]


    Scenario 2:
        if i > 0 and nums[i] == nums[i-1] and used[i-1]: continue

    dfs(perm=[], used=[0,0,0], nums, ret=[])
    |__i=0: dfs(perm=[A], used=[1,0,0], nums, ret=[])
            |__i=0: x
            |__i=1: dfs(perm=[A,B], used=[1,1,0], nums, ret=[])
                    |__i=0: x
                    |__i=1: x
                    |__i=2: x
            |__i=2: dfs(perm=[A,B'], used=[1,0,1], nums, ret=[])
                    |__i=0: x
                    |__i=1: dfs(perm=[A,B',B], used=[1,1,1], nums, ret=[]) --> add [A,B',B] to ret
                    |__i=2: x
    |__i=1: dfs(perm=[B], used=[0,1,0], nums, ret=[[A,B,B']])
            |__i=0: dfs(perm=[B,A], used=[1,1,0], nums, ret=[[A,B',B]])
                    |__i=0: x
                    |__i=1: x
                    |__i=2: x
            |__i=1: x
            |__i=2: x
    |__i=2: dfs(perm=[B'], used=[0,0,1], nums, ret=[[A,B',B]])
            |__i=0: dfs(perm=[B',A], used=[1,0,1], nums, ret=[[A,B',B]])
                    |__i=0: x
                    |__i=1: dfs(perm=[B',A,B], used=[1,1,1], nums, ret=[[A,B',B]]) --> add [B',A,B] to ret
            |__i=1: dfs(perm=[B,B'], used=[0,1,1], nums, ret=[[A,B',B], [B',A,B]])
                    |__i=0: dfs(perm=[B,B',A], used=[1,1,1], nums, ret=[[A,B',B], [B',A,B]]) --> add [B,B',A] to ret
                    |__i=1: x
                    |__i=2: x
            |__i=2: x

    Final result: [[A,B',B], [B',A,B], [B,B',A]]

    Scenario 1 is faster than scenario 2, because for every segment that contains duplicate elements, scenario 1
    always places element with smaller index before placing the ones with large index, which end up using fewer
    iterations for getting the final result.
    """
    def dfs(self, perm, used, nums, ret):
        if len(perm) == len(used):
            ret.append(perm)
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            used[i] = True
            self.dfs(perm+[nums[i]], used, nums, ret)
            used[i] = False

    def permuteUnique_dfs1(self, nums: List[int]) -> List[List[int]]:
        ret = []
        used = [0] * len(nums)
        nums.sort()
        self.dfs([], used, nums, ret)
        return ret

    """
        Solution 2: DFS
        https://leetcode.com/problems/permutations-ii/discuss/18602/9-line-python-solution-with-1-line-to-handle-duplication-beat-99-of-others-%3A-)
        
        nums = [A, B, B], 
        dfs(perm=[], counter={A:1, B:2})
        |__k=A: dfs(perm=[A], counter={A:0, B:2})
                |__k=A: x
                |__k=B: dfs(perm=[A,B], counter={A:0, B:1})
                        |__k=A: x
                        |__k=B: dfs(perm=[A,B,B], counter={A:0, B:0}) --> add [A,B,B]
        |__k=B: dfs(perm=[B], counter={A:1, B:1})
                |__k=A: dfs(perm=[B,A], counter={A:0, B:1})
                        |__k=A: x
                        |__k=B: dfs(perm=[B,A,B], counter={A:0, B:0}) --> add [B,A,B]
                |__k=B: dfs(perm=[B,B], counter={A:1, B:0})
                        |__k=A: dfs(perm=[B,B,A], counter={A:0, B:0}) --> add [B,B,A]
                        |__k=B: x
    """
    def permuteUnique_dfs2(self, nums: List[int]) -> List[List[int]]:
        def dfs(perm, counter):
            if len(perm) == len(nums):
                ret.append(perm)
                return
            for k in counter:
                if counter[k] > 0:
                    counter[k] -= 1
                    dfs(perm+[k], counter)
                    counter[k] += 1

        ret = []
        counter = Counter(nums)
        dfs([], counter)
        return ret


    """
        Solution 3 BFS
        
        nums = [A, B, B']
        perms = [[]]
        
        n=A: perm=[]
                |__i=0: add [A] --> new_perms=[[A]] 
             perms = [[A]]
        n=B: perm=[A]
                |__i=0: add [B,A] --> new_perms=[[B,A]]
                |__i=1: add [A,B] --> new_perms=[[B,A], [A,B]]
             perms = [[B,A], [A,B]]
        n=B':perm=[B,A]
                |__i=0: add [B',B,A] --> new_perms=[[B',B,A]] 
                        break
             perm=[A,B]
                |__i=0: add [B',A,B] --> new_perms=[[B',B,A], [B',A,B]]
                |__i=1: add [A,B',B] --> new_perms=[[B',B,A], [B',A,B], [A,B',B]]     
                        break
             new_perms = [[B',B,A], [B',A,B], [A,B',B]]
            
    """
    def permuteUnique_BFS(self, nums):
        perms = [[]]
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm)+1):
                    new_perms.append(perm[:i]+[n]+perm[i:])
                    if i < len(perm) and perm[i] == n:
                        break
            perms = new_perms

        return perms
