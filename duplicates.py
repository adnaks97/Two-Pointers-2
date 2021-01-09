# Time Complexity : O(N)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : YES
# Any problem you faced while coding this : NO


# Your code here along with comments explaining your approach

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        cur_pos = 0
        
        while i < len(nums):
            ct = 1
            val = nums[i]
            while i< len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
                ct += 1
            if ct > 1:
                nums[cur_pos] = val
                nums[cur_pos + 1] = val
                cur_pos += 2
                i += 1
            else:
                nums[cur_pos] = val
                i += 1
                cur_pos += 1

        return cur_pos