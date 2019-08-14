"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
P004 Median of Two Sorted Array
Hard

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
"""

from typing import *


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Version A, O(N)
        Merge two sorted list then find the median
        Not very efficient, as we go all the way, and used a lot of space
        """

        def median(array: List[int]) -> float:
            """Helper"""

            length = len(array)
            half = length // 2
            if length == 0:
                return 0
            elif length % 2 != 0:
                return array[half]
            else:
                return (array[half - 1] + array[half]) / 2

        # Merge sort
        i, j = 0, 0
        merge = []
        while i <= len(nums1) - 1 or j <= len(nums2) - 1:
            if i == len(nums1):
                merge += nums2[j:]
                break
            elif j == len(nums2):
                merge += nums1[i:]
                break
            elif nums1[i] <= nums2[j]:
                merge.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                merge.append(nums2[j])
                j += 1

        return median(merge)

class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Version B, O(1/2N)
        Modified merge sort to only merge half way
        """

        l1, l2 = len(nums1), len(nums2)
        total_l = l1 + l2

        i, j = 0, 0
        merge = []
        while i <= len(nums1) - 1 or j <= len(nums2) - 1:
            if len(merge) == total_l // 2 + 1:
                break

            elif i == len(nums1):
                merge.append(nums2[j])
                j += 1
            elif j == len(nums2):
                merge.append(nums1[i])
                i += 1
            elif nums1[i] <= nums2[j]:
                merge.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                merge.append(nums2[j])
                j += 1

        if len(merge) == 1:
            return merge[-1]
        if total_l % 2 == 0:
            return (merge[-1] + merge[-2]) / 2
        else:
            return merge[-1]

class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Version C1, Time O(N), space O(1/2N)
        Same half way method with different index
        """

        cur1, cur2 = 0, 0
        ct, lst = 0, []
        m1 = (len(nums1) + len(nums2) + 1) // 2 - 1
        m2 = (len(nums1) + len(nums2) + 2) // 2 - 1

        if not nums1:
            return (nums2[m1] + nums2[m2]) / 2
        if not nums2:
            return (nums1[m1] + nums1[m2]) / 2

        while ct <= m2:
            if cur1 == len(nums1):
                lst.append(nums2[cur2])
                cur2 += 1
            elif cur2 == len(nums2):
                lst.append(nums1[cur1])
                cur1 += 1
            elif nums1[cur1] <= nums2[cur2]:
                lst.append(nums1[cur1])
                cur1 += 1
            elif nums1[cur1] > nums2[cur2]:
                lst.append(nums2[cur2])
                cur2 += 1
            ct += 1

        return (lst[m1] + lst[m2]) / 2

class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Version C2, Time O(N), space O(1)
        Same half way method with different index, but only keep track last two
        """

        total_length = len(nums1) + len(nums2)
        mid_idx = total_length // 2
        i1, i2 = 0, 0
        ct = 0
        pre, cur = 0, 0

        while True:

            # push next sorted item to cur position
            if i1 == len(nums1):
                cur = nums2[i2]
                i2 += 1
            elif i2 == len(nums2):
                cur = nums1[i1]
                i1 += 1
            elif nums1[i1] <= nums2[i2]:
                cur = nums1[i1]
                i1 += 1
            else:
                cur = nums2[i2]
                i2 += 1

            if ct < mid_idx:  # record cur position to pre and go for next cur
                pre = cur
                ct += 1
            else:  # don't update pre, stay as it is
                break

        if total_length % 2 == 0:
            return (cur + pre) / 2
        else:
            return cur


if __name__ == "__main__":
    assert Solution().findMedianSortedArrays([], [1]) == 1.0, "Edge 1"
    assert Solution().findMedianSortedArrays([1], [2]) == 1.5, "Edge 2"
    assert Solution().findMedianSortedArrays([2], []) == 2.0, "Edge 3"

    assert Solution().findMedianSortedArrays([1, 3], [2]) == 2.0, "Example 1"
    assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5, "Example 2"
    assert Solution().findMedianSortedArrays([1, 2, 3, 4], [2, 3, 4, 5]) == 3.0, "Example 3"
    assert Solution().findMedianSortedArrays([3], [-2, -1]) == -1.0, "Negative"

    print("all passed")
