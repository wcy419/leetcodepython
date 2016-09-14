class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        increasing = []
        maxarea = 0
        i = 0
        while i <= len(heights):
            if not increasing or (i <len(heights) and heights[i] > heights[increasing[-1]]):
                increasing.append(i)
                i += 1
            else:
                h = increasing.pop()
                if not increasing:
                    maxarea = max(maxarea, heights[h]*i)
                else:
                    maxarea = max(maxarea, heights[h]*(i - increasing[-1] -1))
        return maxarea
if __name__ == "__main__":
    print Solution().largestRectangleArea([2, 0, 2])
    print Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])
