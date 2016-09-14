
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiou"
        l = list(s)
        i, j = 0, len(s)-1
        while i < j:
            if l[i] not in vowels:
                i += 1
            elif l[j] not in vowels:
                j -= 1
            else:
                l[i], l[j] = l[j], l[i]
                j -= 1
                i += 1
        return "".join(l)
                
print Solution().reverseVowels("hello") 
print Solution().reverseVowels("leetcode")
