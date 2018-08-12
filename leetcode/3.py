"""给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

"""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        D = 1
        for i in range(len(digits)):
            D = D + digits[i] * 10 ** (len(digits)-i-1)
        '''A = []
        for i in str(D):
            A.append(i)
        for i in range(len(A)):
            A[i] = int(A[i])
        return A'''
        return ([int(i) for i in list(str(D))])

Digits = [1,2,3]
s = Solution()
print(s.plusOne(Digits))
print(type(s.plusOne(Digits)))