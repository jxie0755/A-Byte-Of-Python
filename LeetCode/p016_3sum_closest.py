# 3Sum Closest
# Medium


# Given an array nums of n integers and an integer target,
# find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        diff = float('inf')
        result = float('inf')

        i = 0
        ### Similar structure as 3Sum.
        ### Revise by checking the 3Sum with Target, and update the 3sum of lowest diff
        while i < len(nums) - 2:

            if i == 0 or nums[i] != nums[i - 1]:

                j, k = i + 1, len(nums) - 1
                # i 是下一个, k是尾部

                while j < k:
                    three_sum = nums[i] + nums[j] + nums[k]
                    check = abs(three_sum-target)
                    if check < diff:
                        diff = check
                        result = three_sum

                    if nums[i] + nums[j] + nums[k] < target:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > target:
                        k -= 1

                    # 如果找到一个解, 也就是刚好等于target, 那就直接return
                    else:
                        return target
            i += 1
        return result




if __name__ == '__main__':
    # No need to test edge as gurantee to have exactly one solution
    assert Solution().threeSumClosest([1, 1, 1], 1000) == 3, 'Edge'
    assert Solution().threeSumClosest([-1, 2, 1, -4], 1) == 2, 'Example 1'
    assert Solution().threeSumClosest([-1, 2, 1, -4], -1) == -1, 'Match'

    print('all passed')
