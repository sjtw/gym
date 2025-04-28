class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root: TreeNode) -> int:
    if not root:
        return 0

    l = max_depth(root.left)
    r = max_depth(root.right)

    return max(l, r) + 1