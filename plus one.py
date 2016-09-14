class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        lenth = len(digits)
        for i in reversed(range(lenth)):
            digits[i] += carry
            carry = digits[i] /10
            digits[i] = digits[i]%10

        if carry:
            digits = [1] + digits
        return digits

if __name__ == "__main__":
    print (Solution().plusOne([9, 9, 9, 9]))
