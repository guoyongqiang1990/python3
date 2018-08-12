'''给定两个数组，写一个函数来计算它们的交集。

例子:

 给定 num1= [1, 2, 2, 1], nums2 = [2, 2], 返回 [2].

提示:

    每个在结果中的元素必定是唯一的。
    我们可以不考虑输出结果的顺序。

'''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num1 = list(set(nums1))
        num2 = list(set(nums2))
        ans = []
        for i in num1:
            if i in num2:
                ans.append(i)
        return ans


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
s = Solution()
print(s.intersection(nums1,nums2))