class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_length = 0
        substring = ""
        
        start_index = 0
        last_index = 0
        
        while start_index < len(s):
            if last_index == len(s) or s[last_index] in substring:
                start_index += 1
                last_index = start_index
                
                max_length = max(max_length, len(substring))
                
                substring = ""
                
            else:
                substring += s[last_index]
                last_index += 1
        
        return max_length
        
        """
        :type s: str
        :rtype: int
        """
        