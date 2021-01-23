"""
https://leetcode.com/problems/subsets-ii/
P090 Subsets II
Medium


Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
"""

from typing import *


class Solution_A:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        With the help from the combinationSolo from Leetcode P077
        """
        result = []
        for i in range(0, len(nums) + 1):
            result += self.combinationSolo(nums, i)

        # use set to remove repeat then convert back to list
        return [list(i) for i in set(result)]

    def combinationSolo(self, nums: List[int], k: int) -> List[Tuple[int]]:
        """
        Helper for A1, refer to LC077, modify to output in tuple
        """
        nums = sorted(nums)  # make sure the nums is sorted to begin with

        if k == 0:
            return [tuple()]
        elif k == len(nums):
            return [tuple(nums)]
        elif k == 1:
            return [(i,) for i in nums]
        else:
            result = []
            next_list = nums[:]
            tail = next_list.pop()
            result += self.combinationSolo(nums[:len(nums) - 1], k)
            result += [com + (tail,) for com in self.combinationSolo(next_list, k - 1)]
            return result



if __name__ == "__main__":
    testCase = Solution_A()

    assert sorted(testCase.subsetsWithDup([])) == [
        []
    ], "Edge 0"

    assert sorted(testCase.subsetsWithDup([1])) == [
        [],
        [1]
    ], "Edge 1"

    assert sorted(testCase.subsetsWithDup([1, 2])) == [
        [],
        [1],
        [1, 2],
        [2]
    ], "Example 1"

    assert sorted(testCase.subsetsWithDup([1, 2, 2])) == [
        [],
        [1],
        [1, 2],
        [1, 2, 2],
        [2],
        [2, 2]
    ], "Example 2"

    assert sorted(testCase.subsetsWithDup([1, 2, 3])) == [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 3],
        [2],
        [2, 3],
        [3]
    ], "Additional 1"

    assert sorted(testCase.subsetsWithDup([1, 1, 2, 2])) == [
        [],
        [1],
        [1, 1],
        [1, 1, 2],
        [1, 1, 2, 2],
        [1, 2],
        [1, 2, 2],
        [2],
        [2, 2]
    ], "Additional 2"

    print("All passed")
