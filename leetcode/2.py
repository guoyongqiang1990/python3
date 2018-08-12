"""请编写一个函数，其功能是将输入的字符串反转过来。

示例：

输入：s = "hello"
返回："olleh"

"""


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''a = ''
        for i in range(len(s)):
            a = a + (s[len(s) - (i+1)])
        return (a)'''
        return str(s)[::-1]

A = "hello world!"
s = Solution()
print(s.reverseString(A))
print(type(s.reverseString(A)))