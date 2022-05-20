def generate(self, numRows: int) -> List[List[int]]:
if numRows == 1:
arr = [[1]]
return arr
if numRows == 2:
arr = [[1],[1,1]]
return arr
arr = [[1],[1,1]]
for i in range(numRows - 1):
out = []
out.append(1)
for i in range(numRows - 3):
out.append(i+2)
out.append(1)
arr.append(out)
return arr