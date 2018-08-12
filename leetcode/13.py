'''给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。

American keyboard

示例1:

输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]

注意:

    你可以重复使用键盘上同一字符。
    你可以假设输入的字符串将只包含字母。
'''


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        A = ['q','w','e','r','t','y','u','i','o','p']
        B = ['a','s','d','f','g','h','j','k','l']
        C = ['z','x','c','v','b','n','m']
        for word in words:
            AC = False
            BC = False
            CC = False
            for letter in word.lower():
                if letter in A:
                    AC = True
                elif letter in B:
                    BC = True
                elif letter in C:
                    CC = True
            lier = [AC, BC, CC]
            if lier.count(True) == 1:
                ans.append(word)

        return ans







words = ["Hello", "Alaska", "Dad", "Peace"]
s = Solution()
print(s.findWords(words))