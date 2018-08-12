"""给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true

示例 2:

输入: "()[]{}"
输出: true

示例 3:

输入: "(]"
输出: false

示例 4:

输入: "([)]"
输出: false

示例 5:

输入: "{[]}"
输出: true



class Solution:
    def isValid(self,s):
        if s == "":
            return True
        B = list(s)
        A = [B[0]]
        for i in range(1,len(B)):
            if A == []:
                A.append(B[i])
            elif A[-1] == "{" and (B[i]) == "}":
                A.pop()
            elif A[-1] == "[" and (B[i]) == "]":
                A.pop()
            elif A[-1] == "(" and (B[i]) == ")":
                A.pop()
            else:
                A.append(B[i])
        if A == []:
            return True
        else:
            return False
"""
class Solution:
    def isValid(self,s):
        table = {"(":")", '[':']', '{':'}'}
        stack = []
        for i in s:
            if len(stack) >0 and stack[-1] in table and table[stack[-1]] == i:
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0






s = "{}()[]"
S = Solution()
print(S.isValid(s))