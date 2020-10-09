"""
https://leetcode.com/problems/trapping-rain-water/
P042 Trapping Rain Water
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
"""

from typing import *

class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        tops = []
        trend = "flat"
        i = 0
        while i < len(height) - 1:
            cur = height[i]
            next = height[i+1]
            if cur > next:
                if trend == "flat":
                    tops.append((cur, i))
                    trend = "down"
                elif trend == "down":
                    pass
                elif trend == "up":
                    tops.append((cur, i))
                    trend = "down"
            elif cur < next:
                if trend == "flat":
                    trend = "up"
                elif trend == "down":
                    trend = "up"
                elif trend == "up":
                    pass
            else:
                if trend == "flat":
                    pass
                elif trend == "down":
                    trend = "flat"
                elif trend == "up":
                    tops.append((cur, i))
                    trend = "flat"
            i += 1

        if height[i] > height[i-1]:
            tops.append((height[i], i))




print(Solution().trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6]))
                  #    0  1  2  3  4  5  6  7  8  9









# if __name__ == "__main__":
#     testCase = Solution()
#     assert testCase.trap([]) == 0, "Edge 1"
#     assert testCase.trap([0]) == 0, "Edge 2"
#     assert testCase.trap([1]) == 0, "Edge 3"
#     assert testCase.trap([1, 1]) == 0, "Edge 4"
#     assert testCase.trap([2, 2, 2]) == 0, "Edge 5"
#     assert testCase.trap([2, 0, 2]) == 2, "Edge 6"
#
#     assert testCase.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6, "Example 1"
#     assert testCase.trap([10, 1, 2, 1, 2, 1, 10]) == 43, "Example 2"
#     assert testCase.trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6]) == 23, "Example 3"
#     assert testCase.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6, "Extra 1"
#     print("all passed")
