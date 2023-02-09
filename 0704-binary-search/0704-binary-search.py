class Solution(object):
    def search(self, nums, target):
        first_index = 0
        last_index = len(nums) - 1

        while first_index <= last_index:
            current_index = (first_index + last_index) / 2

            if nums[current_index] == target:
                return current_index
            
            elif nums[current_index] > target:
                last_index = current_index - 1

            else:
                first_index = current_index + 1

        return -1

            