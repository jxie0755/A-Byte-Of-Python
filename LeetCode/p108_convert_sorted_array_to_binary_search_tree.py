# P108 Convert Sorted Array to Binary Search Tree
# Easy



# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


from typing import *

# Definition for a binary tree node.
from math import log

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):

        def layer(T, L=1):
            if T.val is None:
                return 'N'

            s = str(T.val)
            if T.left and T.right:
                return s + '\n' + '  ' * L + layer(T.left, L + 1) + '\n' + '  ' * L + layer(T.right, L + 1)
            elif T.left and not T.right:
                return s + '\n' + '  ' * L + layer(T.left, L + 1) + '\n' + '  ' * L + 'N'
            elif not T.left and T.right:
                return s + '\n' + '  ' * L + 'N' + '\n' + '  ' * L + layer(T.right, L + 1)
            else:
                return s + '\n' + '  ' * L + 'N' + '\n' + '  ' * L + 'N'

        return layer(self)

    def __eq__(self, other):
        return str(self) == str(other)


def genTree(lst):
    """
    generate a binary tree according to a non-empty list of values
    The lst must be all filled, even the branch is empty, then use None to suggest the empty treeNode
    """
    LLL = log(len(lst)+1,2)
    if int(LLL) != LLL:
        print("List length is not complete, it must be 2^n - 1")
        raise ZeroDivisionError

    layers = []
    i, L = 0, 1

    while i != len(lst):
        layers.append(lst[i:i + L])
        i += L
        L *= 2
    pre_root = [TreeNode(i) for i in layers[0]]
    root_to_return = pre_root[0]

    for k in range(1, len(layers)):
        cur = []
        for i in layers[k]:
            if i is not None:
                cur.append(TreeNode(i))
            else:
                cur.append(None)

        for j in range(len(cur)):
            rt_idx, brc_side = divmod(j, 2)
            if brc_side == 0 and cur[j] is not None:
                pre_root[rt_idx].left = cur[j]
            elif brc_side != 0 and cur[j] is not None:
                pre_root[rt_idx].right = cur[j]
        pre_root = cur

    return root_to_return


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid_idx = len(nums) // 2
        mid = nums[mid_idx]
        ans = TreeNode(mid)

        def helper(root, left_list, right_list):
            if left_list:
                left_mid_idx = len(left_list) // 2
                left_val = left_list[left_mid_idx]
                root.left = TreeNode(left_val)
                LL, LR = left_list[:left_mid_idx], left_list[left_mid_idx+1:]
                helper(root.left, LL, LR)

            if right_list:
                right_mid_idx = len(right_list) // 2
                right_val = right_list[right_mid_idx]
                root.right = TreeNode(right_val)
                RL, RR = right_list[:right_mid_idx], right_list[right_mid_idx + 1:]
                helper(root.right, RL, RR)

        helper(ans, nums[:mid_idx], nums[mid_idx+1:])
        return ans



if __name__ == '__main__':
    A = []
    assert Solution().sortedArrayToBST(A) is None, 'Edge 0'

    A = [1]
    assert Solution().sortedArrayToBST(A) == genTree([1]), 'Edge 1'

    A = [-10, -3, 0, 5, 9]
    assert Solution().sortedArrayToBST(A) == genTree([0, -3, 9, -10, None, 5, None]), 'Example 1'

    print('all passed')