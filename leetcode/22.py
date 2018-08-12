"""给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

说明:

    你可以假设数组不可变。
    会多次调用 sumRange 方法。

"""

#超时做法
'''class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        sum = self.nums[i]
        for n in range(j-i):
            sum += self.nums[i+1]
            i +=1
        return sum'''


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sums = []
        self.sums.append(0)

        for n in range(1, len(self.nums) + 1):
            self.sums.append(self.sums[n - 1] + self.nums[n - 1])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

        return self.sums[j + 1] - self.sums[i]




        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(i,j)

nums = [-2, 0, 3, -5, 2, -1]
N = NumArray(nums)
print(N.sumRange(0,2))
print(N.sumRange(2,5))
print(N.sumRange(0,5))