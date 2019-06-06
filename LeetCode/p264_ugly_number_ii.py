# P264 Ugly Number II
# Medium

# Write a program to find the n-th ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

# Note:
# 1 is typically treated as an ugly number.
# n does not exceed 1690.


import heapq

class Solution(object):

    # Version A, Abandoned
    # Use prime sieves to get all the prime numbers
    # Then sieve again with prime numbers > 2,3,5
    def primesunder(self, n):
        sieve = list(range(0, n+1))
        sieve[1] = 0
        sieve[2] = 0
        sieve[3] = 0
        sieve[5] = 0
        for i in range(2,n+1):
            for k in range(2*i, len(sieve), i):
                sieve[k] = 0
        return list(filter(lambda x:bool(x), sieve))

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        # choose factor wisely:
        # primes must cover all the primes bigger than nth ugly number
        # And after sieving, there should be more than n items left in the sieve
        # This leads to a huge factor of sieve, caused the algorithm taking too long to calculate
        # Therefore, this is not a good way, abandon this method
        sieve_size = 10*n
        sieve = list(range(sieve_size))
        primes = self.primesunder(sieve_size)
        # print('prime list', primes)

        for i in primes:
            for k in range(i, len(sieve), i):
                sieve[k] = 0

        sieve = list(filter(lambda x:bool(x), sieve))
        print('n is', n, 'sieve length:', len(sieve))
        print('final sieve:', sieve)
        # return sieve[n-1]


class Solution(object):
    # @param {integer} n
    # @return {integer}

    # STD ans A1
    def nthUglyNumber(self, n):
        ugly = [1]
        i2 = i3 = i5 = 0

        while len(ugly) < n:

            while ugly[i2] * 2 <= ugly[-1]:
                i2 += 1
            while ugly[i3] * 3 <= ugly[-1]:
                i3 += 1
            while ugly[i5] * 5 <= ugly[-1]:
                i5 += 1

            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))

        return ugly[-1]

    # STD ans A2
    # Need to use heapq
    def nthUglyNumber(self, n):

        q2, q3, q5 = [2], [3], [5]
        ugly = 1
        for u in heapq.merge(q2, q3, q5):
            if n == 1:
                return ugly
            if u > ugly:
                ugly = u
                n -= 1
                q2 += 2 * u,
                q3 += 3 * u,
                q5 += 5 * u,

class Solution(object):

    # STD ans B1
    # Get all UG number within 32bit, and sorted....
    ugly = sorted(2**a * 3**b * 5**c
                  for a in range(32) for b in range(20) for c in range(14))

    def nthUglyNumber(self, n):
        return self.ugly[n-1]



print(Solution().nthUglyNumber(10))

# if __name__ == '__main__':
#     assert Solution().nthUglyNumber(1) == 1, 'Edge'
#     assert Solution().nthUglyNumber(2) == 2, 'Example 1'
#     assert Solution().nthUglyNumber(6) == 6, 'Example 2'
#     assert Solution().nthUglyNumber(7) == 8, 'Example 3'
#     assert Solution().nthUglyNumber(10) == 12, 'Example 4'
#     assert Solution().nthUglyNumber(11) == 15, 'Example 5'
#
#     assert Solution().nthUglyNumber(80) == 800, 'Long 1'
#     # assert Solution().nthUglyNumber(1690) == 2304, 'End'
#     print('all passed')
