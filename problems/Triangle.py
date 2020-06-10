from typing import List

class Solution:
    """
        Recursion (Top-Down): Time Limited Exceed

        Time: O(2^N)
        Space: O(2^N)
                            # of calls: 16
        [
             [2],               1
            [3,4],             1+1
           [6,5,7],           1+2+1
          [4,1,8,3]          1+3+3+1
        ]

        tr(0,0,cur=0)
        |__tr(1,0,cur=2)
            |__tr(2,0,cur=2+3)
                |__tr(3,0,cur=2+3+6)
                    |__tr(4,0,cur=2+3+6+4) --> ret=2+3+6+4=15
                    |__tr(4,1,cur=2+3+6+1) --> ret=2+3+6+1=12
                |__tr(3,1,cur=2+3+5)
                    ...
            |__tr(2,1,cur=2+4)
                ...
        |__tr(1,1,cur=2)
            ...
    """
    def minimumTotal_1(self, triangle: List[List[int]]) -> int:
        def traverse(i, j, cur):
            nonlocal ret
            if i == len(triangle):
                ret = min(ret, cur)
                return
            traverse(i+1, j, triangle[i][j]+cur)
            traverse(i+1, j+1, triangle[i][j]+cur)

        ret = float('inf')
        traverse(0, 0, 0)
        return ret

    """
        Divide Conquer (Bottom Up): Time limit Exceed
        
        Time: O(2^N) 
        Space: O(2^N) 
                            # of calls: 16
        [                       
             [2],               1
            [3,4],             1+1
           [6,5,7],           1+2+1  
          [4,1,8,3]          1+3+3+1  
        ]
        
        dc(0,0): 2 + min(3+min(7,x), y)
        |__dc(1,0): 3 + min(7, x)
            |__dc(2,0): 7 (6+1) 
                |__dc(3,0): 4 (4+0)
                    |__dc(4,0): 0
                    |__dc(4,1): 0
                |__dc(3,1): 1 (1+0)
                    |__
                    |__
            |__dc(2,1): x
                |__dc(3,1)
                    |__
                    |__
                |__dc(3,2)        
                    |__
                    |__
        |__dc(1,1): y
            |__dc(2,1)
                |__dc(3,1)
                    |__dc(4,1)
                    |__dc(4,2)
                |__dc(3,2)
                    |__dc(4,2)
                    |__dc(4,3)
            |__dc(2,2)
                |__dc(3,2)
                    |__dc(4,2)
                    |__dc(4,3)
                |__dc(3,3)        
                    |__dc(4,3)
                    |__dc(4,4)
    """
    def minimumTotal_2(self, triangle) -> int:
        def divide_conquer(i, j):
            if i == len(triangle):
                return 0
            return triangle[i][j] + min(divide_conquer(i+1, j),
                                        divide_conquer(i+1, j+1))
        return divide_conquer(0, 0)

    """
        Divide Conquer + Memorization: 
        Time Limited Exceed but better than above solutions
        
        Time: O(N^2) 
        Space: O(N^2) 
                            # of calls: 
        [                       
             [2],               1
            [3,4],             1+1
           [6,5,7],           1+2+1  
          [4,1,8,3]          1+2+2+1  
        ]
        
        dc(0,0): memo[(0,0)] = 11
        |__dc(1,0): memo[(1,0)] = 9
            |__dc(2,0): memo[(2,0)] = 7  
                |__dc(3,0): memo[(3,0)] = 4
                    |__dc(4,0): 0
                    |__dc(4,1): 0
                |__dc(3,1): memo[(3,1)] = 1
                    |__dc(4,1): 0
                    |__dc(4,2): 0
            |__dc(2,1): memo[(2,1)] = 6
                |__dc(3,1): 1 
                |__dc(3,2): memo[(3,2)] = 8
                    |__dc(4,2): 0
                    |__dc(4,3): 0
        |__dc(1,1): memo[(1,1)] = 10
            |__dc(2,1): 6 
            |__dc(2,2): memo[(2,2)] = 10
                |__dc(3,2): 8 
                |__dc(3,3): memo[(3,3)] = 3
                    |__dc(4,3): 0
                    |__dc(4,4): 0       
    """
    def minimumTotal_3(self, triangle) -> int:
        def divide_conquer(i, j):
            if i == len(triangle):
                return 0
            if (1, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = triangle[i][j] + min(divide_conquer(i+1, j),
                                                divide_conquer(i+1, j+1))
            return memo[(i, j)]

        memo = {}
        return divide_conquer(0, 0)

    """
        DP: Top Down
        
        Time: O(N^2) 
        Space: O(N) 
                             
               [                       
                    [2],
                   [3, 4],
                  [6, 5, 7],  
                 [4, 1, 8, 3]  
               ]
             j =  0   1   2   3 
          memo = [2,  2,  2,  2]
                    
        i=1:     [3,  4]
            j=1: [2,  6,  2,  2]
            j=0: [5,  6,  2,  2]
            
        i=2:     [6,  5,  7]
            j=2: [5,  6,  13, 2]
            j=1: [5,  10, 13, 2]
            j=0: [11, 10, 13, 2]
            
        i=3:     [4,  1,  8,  3]
            j=3: [11, 10, 13, 16]
            j=2: [11, 10, 18, 16]
            j=1: [11, 11, 18, 16]
            j=0: [14, 11, 18, 16]
    """
    def minimumTotal_4(self, triangle):
        memo = [triangle[0][0]] * len(triangle)

        for i in range(1, len(triangle)):
            for j in range(i, -1, -1):  # right to left
                if j == i:  # right most
                    memo[j] = triangle[i][j] + memo[j-1]
                elif j == 0:  # left most
                    memo[j] = triangle[i][j] + memo[0]
                else:
                    memo[j] = triangle[i][j] + min(memo[j-1], memo[j])

        return min(memo)

    """
        DP (Multi-ForLoop): Bottom Up: 80%
        
        Time: O(N^2) 
        Space: O(1), change the triangle in place 
                             
               [                       
                    [2],
                   [3, 4],
                  [6, 5, 7],  
                 [4, 1, 8, 3]  
               ]                
    """
    def minimumTotal_5(self, triangle) -> int:
        for i in range(len(triangle)-2, -1, -1):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i+1][j],
                                      triangle[i+1][j+1])
        return triangle[0][0]

    """
        DP: Bottom Up without changing the triangle
    """
    def mimimumTotal_6(self, triangle) -> int:
        memo = triangle[-1]

        for i in range(len(triangle)-2, -1, -1):
            for j in range(i+1):
                memo[j] = triangle[i][j] + min(memo[j], memo[j+1])

        return memo[0]
