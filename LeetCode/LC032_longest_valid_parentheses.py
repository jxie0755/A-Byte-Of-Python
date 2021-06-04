"""
https://leetcode.com/problems/longest-valid-parentheses/
LC020 Longest Valid Parentheses
Hard

Given a string containing just the characters "(" and ")", find the length of the longest valid (well-formed) parentheses substring.
"""


class Solution_A:

    def longestValidParentheses(self, s: str) -> int:
        """
        Iterate all substring from long to short and find the first valid
        This will exceed max time
        """
        for lenth in range(len(s), 0, -1):
            for start_idx in range(len(s) - lenth + 1):
                sample = s[start_idx:start_idx + lenth]
                if self.parenIsValid(sample):
                    return len(sample)
        return 0

    def parenIsValid(self, s: str) -> bool:
        """
        Helper function from LC020
        Modified with just to evaluate curved parentheses
        """
        brackets = 0
        for i in s:
            if i == "(":
                brackets += 1
            if i == ")":
                if brackets == 0:
                    return False
                else:
                    brackets -=1

        return brackets == 0


class Solution_B:

    def longestValidParentheses(self, s: str) -> int:
        """
        O(N) new idea, Divide and Conquer

        )) (  ) ((( ) (( )) ( )) convert to
        -1 1 -1  3 -1 2 -2  1 -2 then merge L positive + R negative
        -1  00   200  0000  00 -1
        -1  00 1 000  0000  00  0

        longest string of 0 is length = 10
        """
        # first translate sequence to digits
        pass


testCase = Solution_B()
print(testCase.longestValidParentheses("))()((()(())())"))

if __name__ == '__main__':
    testCase = Solution_B()

    assert testCase.longestValidParentheses("(()") == 2, "Example 1, '()'"
    assert testCase.longestValidParentheses(")()())") == 4, "Example 2, '()()'"
    assert testCase.longestValidParentheses("") == 0, "Example 3, Edge 0"

    assert testCase.longestValidParentheses("()(()") == 2, "Additional 1"
    assert testCase.longestValidParentheses("()(()()") == 4, "Additional 2"
    assert testCase.longestValidParentheses("(()(((()") == 2, "Additional 3"
    assert testCase.longestValidParentheses("(()((()))") == 8, "Additional 4"
    assert testCase.longestValidParentheses("(((()())))") == 10, "Additional 5"
    assert testCase.longestValidParentheses("))()((()(())())") == 10, "Additional 6"

    print("All passed")

