class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        List = []
        for i in range(numRows):
            List.append([])
            for j in range(i+1):
                if j in (0,i):
                    List[i].append(1)
                else:
                    List[i].append(List[i-1][j-1]+List[i-1][j])
        return List
                    
                        

if __name__ == "__main__":
    print Solution().generate(5)
