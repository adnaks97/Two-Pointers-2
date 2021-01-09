# Time Complexity : O(M+N)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : YES
# Any problem you faced while coding this : NO


# Your code here along with comments explaining your approach

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        i, j = 0, n-1
        
        while j >=0 and i<m :
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            if matrix[i][j] < target:
                i += 1
        return False