'''给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1:

输入: [1, 2, 2, 3, 1]
输出: 2
解释: 
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.

示例 2:

输入: [1,2,2,3,1,4,2]
输出: 6
'''

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """unique_nums = list(set(nums))    #  去重
        n = {}
        for i in unique_nums:
            n.update({i: nums.count(i)}) # 取出各个数的个数
        max_key = []
        for key, value in n.items():
            if value == max(n.values()):  #度
                max_key.append(key)      #取出度对应的数


        '''answer = []
        for each in max_key:
            m = []
            for index, value in enumerate(nums):
                if each == value:
                    m.append(index)
            answer.append(max(m)-min(m)+1)
        return min(answer)'''                 #超时了
        answer = []
        for each in max_key:
            for i in range(len(nums)):
                if nums[i] == each:
                    a = i
                    break
            for j in range(len(nums)-1, -1, -1):
                if nums[j] == each:
                    b = j
                    break
            answer.append(b-a+1)
        return min(answer)


        #n = [nums.count(i) for i in unique_nums]
        #return max_key"""

        # 定义字典元素以及对应的位置信息，count记录每个元素出现的次数
        left, right, count = {}, {}, {}
        for i, num in enumerate(nums):
            # 如果元素num第一次出现，则存入left中
            if num not in left:
                left[num] = i
            # 将出现的元素及对应的位置信息存入right中
            right[num] = i
            # 每个元素出现一次，则count对位num位置的数值 +1
            count[num] = count.get(num, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for num in count:
            if count[num] == degree:
                ans = min(ans, right[num] - left[num] + 1)
        return ans



nums = [1,1,2,3,3,33,3,2,2,2]
s = Solution()
print(s.findShortestSubArray(nums))
