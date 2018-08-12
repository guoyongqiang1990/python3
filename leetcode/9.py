'''给定两个数组，写一个方法来计算它们的交集。

例如:
给定 nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2, 2].

注意：

       输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
       我们可以不考虑输出结果的顺序。

跟进:

    如果给定的数组已经排好序呢？你将如何优化你的算法？
    如果 nums1 的大小比 nums2 小很多，哪种方法更优？
    如果nums2的元素存储在磁盘上，内存是有限的，你不能一次加载所有的元素到内存中，你该怎么办？

'''
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1, count2 = {}, {}
        for i,num in enumerate(nums1):
            count1[num] = count1.get(num, 0) + 1
        for i, num in enumerate(nums2):
            count2[num] = count2.get(num, 0) + 1

        ans = []
        for num in count1:
            if num in count2:
                for i in range(min(count1[num], count2[num])):
                    ans.append(num)
        return ans

nums1 = [1]
nums2 = [1, 1]

s = Solution()
print(s.intersect(nums1, nums2))