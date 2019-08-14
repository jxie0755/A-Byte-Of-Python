"""
https://leetcode.com/problems/palindrome-number/
p009 Palindrome Number
Easy

Determine whether an integer is a palindrome. Do this without extra space.
Negative integer will not be a palindrome
"""

class Solution:

    def isPalindrome(self, x: int) -> bool:
        """Version A, string method, takes extra space"""

        if x < 0:
            return False
        else:
            return str(x) == str(x)[::-1]

class Solution:

    def isPalindrome(self, x: int) -> bool:
        """Version B, divmod method"""

        if x < 0:
            return False
        copy, reverse = x, 0
        while copy > 0:
            reverse = reverse * 10 + copy % 10
            copy //= 10
        return reverse == x


if __name__ == "__main__":
    assert Solution().isPalindrome(21477412) == True, "Is palindrome (even)"
    assert Solution().isPalindrome(12321) == True, "Is palindrome (odd)"
    assert not Solution().isPalindrome(1477412), "Not palindrome"
    assert Solution().isPalindrome(1), "Single digit 1"
    assert Solution().isPalindrome(0), "Single digit 0"

    print("all passed")
