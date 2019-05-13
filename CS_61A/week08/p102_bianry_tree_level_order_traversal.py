# P102 Binary Tree Level Order Traversal
# Medium


# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):

        def layer(T, L=1):
            if not T.val:
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


def genTree(lst):
    """
    generate a binary tree according to a non-empty list of values
    The lst must be all filled, even the branch is empty, then use None to suggest the empty treeNode
    """
    layers = []
    i, L = 0, 1
    while i != len(lst):
        layers.append(lst[i:i + L])
        i += L
        L *= 2
    pre_root = [TreeNode(i) for i in layers[0]]
    root_to_return = pre_root[0]

    for k in range(1, len(layers)):
        cur = [TreeNode(i) for i in layers[k]]
        for j in range(len(cur)):
            rt_idx, brc_side = divmod(j, 2)
            if brc_side == 0:
                pre_root[rt_idx].left = cur[j]
            else:
                pre_root[rt_idx].right = cur[j]
        pre_root = cur

    return root_to_return

class Solution:

    ### Same as Leetcode P107, use the showLayer to solve the problem
    def showLayer(self, root):
        """show layers of tree"""
        if root is None:
            return []

        result = []
        layer = [root]
        while layer:
            vals = []
            new_layer = []
            for i in layer:
                if i and i.val is not None:
                    vals.append(i.val)
                if i.left:
                    new_layer.append(i.left)
                if i.right:
                    new_layer.append(i.right)
            result.append(vals)
            layer = new_layer

        return result


    def levelOrder(self, root: TreeNode):
        return self.showLayer(root)



if __name__ == '__main__':
    A = None
    assert Solution().levelOrder(A) == [], 'Edge 0'

    A = genTree([1])
    assert Solution().levelOrder(A) == [[1]], 'Edge 1'

    A = genTree([3, 9, 20, None, None, 15, 7])
    assert Solution().levelOrder(A) == [
        [3],
        [9, 20],
        [15, 7],
    ], 'Example 1'

    A = genTree([
        0,
        2, 4,
        1, None, 3, -1,
        5, 1, None, 6, None, 8, None, None])
    assert Solution().levelOrder(A) == [
        [0],
        [2, 4],
        [1, 3, -1],
        [5, 1, 6, 8],
    ], 'Additional'

    print('All passed')