class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        while i>=0 and j>=0:
            if nums1[i] >= nums2[j]:
                nums1[i+j+1] = nums1[i]
                i -= 1
            else:
                nums1[i+j+1] = nums2[j]
                j -= 1
        if i < 0:
            while j >= 0: 
               nums1[i+j+1] = nums2[j]
               j -= 1
        if j < 0:
            while j >= 0: 
               nums1[i+j+1] = nums1[i]
               i -= 1
        return nums1

if __name__ == "__main__":
    A = [3, 5, 8, 0, 0, 0, 0, 0]
    B = [2, 4, 6, 7]
    Solution().merge(A, 3, B, 4)
    print A
