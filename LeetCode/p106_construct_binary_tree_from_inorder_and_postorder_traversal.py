# P106 Construct Binary Tree from Inorder and Postorder Traversal
# Medium


# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.


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

    def isLeaf(self):
        try:
            leftval = self.left.val
        except AttributeError:
            leftval = None
        try:
            rightval = self.right.val
        except AttributeError:
            rightval = None

        return leftval and rightval

def genTree(lst, i=1):
    """
    To generate a perfect binary tree according to a non-empty list of values
    The lst must be all filled, even the branch is empty, then use None to suggest the empty treeNode
    """
    if lst and i <= len(lst) and lst[i-1] is not None:
        node = TreeNode(lst[i-1])
        node.left = genTree(lst, i*2)
        node.right = genTree(lst, i*2+1)
        return node


class Solution:
    ### Basically the same idea of my own slow version in leetcode P105
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        hmp = dict()
        for idx, val in enumerate(inorder):
            hmp[val] = idx

        def helper(postorder_lst):
            if not postorder_lst:
                return None
            root_val = postorder_lst[-1]
            root = TreeNode(root_val)
            root_idx = hmp[root_val]

            left_postorder, right_postorder = [], []
            for i in postorder_lst[::-1]:
                check_idx = hmp[i]
                if check_idx > root_idx:
                    right_postorder.insert(0, i)
                elif check_idx < root_idx:
                    left_postorder.insert(0, i)

            root.left = helper(left_postorder)
            root.right = helper(right_postorder)
            return root

        return helper(postorder)

class Solution(object):
    # STD ans
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        lookup = {}
        for i, num in enumerate(inorder):
            lookup[num] = i
        return self.buildTreeRecu(lookup, postorder, inorder, len(postorder), 0, len(inorder))

    def buildTreeRecu(self, lookup, postorder, inorder, post_end, in_start, in_end):
        if in_start == in_end:
            return None
        node = TreeNode(postorder[post_end - 1])
        i = lookup[postorder[post_end - 1]]
        node.left = self.buildTreeRecu(lookup, postorder, inorder, post_end - 1 - (in_end - i - 1), in_start, i)
        node.right = self.buildTreeRecu(lookup, postorder, inorder, post_end - 1, i + 1, in_end)
        return node


if __name__ == '__main__':
    assert not Solution().buildTree([],[]), 'Edge 0'
    assert Solution().buildTree([1],[1]) == genTree([1]), 'Edge 1'
    assert Solution().buildTree([9,3,15,20,7],[9,15,7,20,3]) == genTree([
        3,
        9,20,
        None,None,15,7
    ]), 'Example 1'

    print('all passed')