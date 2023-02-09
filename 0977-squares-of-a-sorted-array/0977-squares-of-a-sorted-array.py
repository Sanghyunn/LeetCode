class Solution(object):
    def sortedSquares(self, nums):
        left = 0
        right = len(nums) - 1
        
        retval = []
        
        while left <= right:
            left_pow = pow(nums[left], 2)
            right_pow = pow(nums[right], 2)
            
            if left_pow < right_pow:
                retval.insert(0, right_pow)
                right -= 1
            else:
                retval.insert(0, left_pow)
                left += 1
        
        return retval
                
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        