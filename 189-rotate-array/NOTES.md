## Possible solutions
1. O(n^2)
​
```
def rotate(self, nums: List[int], k: int) -> None:
"""
Do not return anything, modify nums in-place instead.
"""
size = len(nums)
for j in range (k):
temp = nums[size-1]
for i in range(size-1,-1,-1):
nums[i] = nums[i-1]
nums[0] = temp
```
> Time limit Exceeded
2. O(n)
我们可以先把整个数组翻转一下，这样后半段元素就到了前边，前半段元素就到了后边，只不过元素顺序是反着的。我们再从 k 位置分隔开，将 [0, k-1] 的元素和 [k, n-1] 的元素再翻转一下，就得到了最终结果。
​
具体步骤：
​
将数组 [0, n-1] 位置上的元素全部翻转
将数组 [0, k-1] 位置上的元素进行翻转
将数组 [k+1, n-1] 位置上的元素进行翻转
```
def rotate(self, nums: List[int], k: int) -> None:
"""
Do not return anything, modify nums in-place instead.
"""
n = len(nums)
k = k % n
self.reverse(nums, 0, n -1)
self.reverse(nums, 0, k-1)
self.reverse(nums, k, n-1)
def reverse(self, nums: List[int], left: int, right: int) -> None:
while left < right :
tmp = nums[left]
nums[left] = nums[right]
nums[right] = tmp
left += 1
right -= 1
```
​