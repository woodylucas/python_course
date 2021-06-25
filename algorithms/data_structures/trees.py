# maximum depth of a binary tree
# pattern can solved with breadth first search template where we use a queue
# use the size to iterate over every node then we extract, the key to this problem
# we want to get to depth of the last child with no children

# recrusive, we can use depth first search, when we reach the leaf node of both directions
#  left and right we will return the max of each sides depth


def max_depth(root, depth=0):
    if root == None:
        return depth
    left = max_depth(root.left, depth + 1)
    right = max_depth(root.right, depth + 1)
    return max(left, right)
