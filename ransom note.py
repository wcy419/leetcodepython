class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = [0] * 26
        letters = 0
        
        for i in magazine:
            l = ord(i) - ord('a')
            count[l] += 1
            
        
        for i in ransomNote:
            l = ord(i) - ord('a')
            count[l] -= 1
            if count[l] < 0:
               return False 
        return True

print Solution().canConstruct("a", "b") 
print Solution().canConstruct("aac", "abderfswrc")
print Solution().canConstruct("aac", "aabcccc") 
