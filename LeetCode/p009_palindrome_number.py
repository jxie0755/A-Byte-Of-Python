# p009 Palindrome Number
# Easy

# Determine whether an integer is a palindrome. Do this without extra space.
# Negative integer will not be a palindrome


class Solution:

    # Version A,  string method, takes extra space
    def isPalindrome(self, x: int) -> bool:
        #
        if x < 0:
            return False
        else:
            return str(x) == str(x)[::-1]

    # Version B, divmod method
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        copy, reverse = x, 0
        while copy > 0:
            reverse = reverse * 10 + copy % 10
            copy //= 10
        return reverse == x

if __name__ == '__main__':
    assert Solution().isPalindrome2(21477412) == True, 'Is palindrome (even)'
    assert Solution().isPalindrome2(12321) == True, 'Is palindrome (odd)'
    assert Solution().isPalindrome2(-21477412) == False, 'Not palindrome'
    assert Solution().isPalindrome2(1) == True, 'Single digit'
    print('all passed')
