"""
https://leetcode.com/problems/length-of-last-word/
p058 Length of Last word
Easy

Given a string s consists of upper/lower-case alphabets and empty space characters " ", return the length of last word in the string.
If the last word does not exist, return 0

Note:
    A word is defined as a character sequence consists of non-space characters only.
"""

import re

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
                    pass
            else:
                cnt += 1
        return cnt


class Solution_C:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Use regex match
        """
        if not s:
            return 0

        raw_pattern = r"(.*\s|\.*)([A-Za-z]*\b)"
        # 2 situations
        # whatever + a space + word (some other thing, but then must be separated by at least a space)
        # whatever + word (just spaces)

        # use \b to have clear cut on words at the end to avoid suffix spaces

        match = re.search(raw_pattern, s)
        if match:
            return len(match.group(2))
        else:
            return 0



if __name__ == "__main__":
    testCase = Solution_B()
    assert testCase.lengthOfLastWord("") == 0, "Edge 1"
    assert testCase.lengthOfLastWord(" ") == 0, "Edge 2"

    assert testCase.lengthOfLastWord("Hello World") == 5, "Regular"

    assert testCase.lengthOfLastWord("Today is a nice day") == 3, "Extra 1"
    assert testCase.lengthOfLastWord("a") == 1, "Extra 2"
    assert testCase.lengthOfLastWord(" a") == 1, "Extra 3"
    assert testCase.lengthOfLastWord("  a") == 1, "Extra 4"
    assert testCase.lengthOfLastWord("aaaa ") == 4, "Extra 5"

    print("all passed")
