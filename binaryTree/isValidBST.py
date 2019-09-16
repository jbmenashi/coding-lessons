class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isValidBST(root):
    if not root:
        return True

    if not root.left and not root.right:
        return True

    if root.left.val < root.val and root.right.val > root.val:
        return isValidBST(root.left) and isValidBST(root.right)
    return False
