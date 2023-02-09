class Solution(object):
    def twoSum(self, nums, target):
        numsCount = len(nums)
        for i in range(0, numsCount):
            for j in range(i + 1, numsCount):
                if target == (nums[i] + nums[j]):
                    return [i, j]
        
        return []
    
