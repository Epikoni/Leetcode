class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [0]*(rowIndex+1)
        for i in range(rowIndex+1):
            for j in range(i, -1, -1):
                if j == 0 or j == i:
                    ans[j] = 1
                else:
                    ans[j] = ans[j-1] + ans[j]
        return ans