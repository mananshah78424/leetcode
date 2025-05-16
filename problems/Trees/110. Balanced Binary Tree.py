class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    if not root:
        return 0
    left = isBalanced(root.left)
    if left == -1:
        return -1
    right = isBalanced(root.right)
    if right == -1:
        return -1
    if abs(left-right)>1:
        return -1
    return max(left,right)+1




root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(isBalanced(root)!=-1)