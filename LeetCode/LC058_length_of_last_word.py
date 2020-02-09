"""
https://leetcode.com/problems/length-of-last-word/
p058 Length of Last word
Easy

Given a string s consists of upper/lower-case alphabets and empty space characters " ", return the length of last word in the string.
If the last word does not exist, return 0

Note:
    A word is defined as a character sequence consists of non-space characters only.
"""

class Solution_A:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Use Python built-in method split
        """
        if len(s.split()) == 0:
            return 0
        return len(s.split()[-1])

class Solution_B:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Set a counter for spaces
        No need for extra space
        """
        cnt = 0
        for v in reversed(s):  # create reversed iterator
            if v.isspace():  # to avoid end with a " "
                if cnt != 0:  # force to move down from the end " ",
                    break  # but break at next " "
            else:
                cnt += 1
        return cnt


if __name__ == "__main__":
    testCase = Solution_B()
    assert testCase.lengthOfLastWord("") == 0, "Edge 1"
    assert testCase.lengthOfLastWord(" ") == 0, "Edge 2"
    assert testCase.lengthOfLastWord("Hello World") == 5, "Regular"
    print("all passed")