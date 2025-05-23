
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
        

def boundaryTraversal(root):
    if not root:
        return []
    left_boundary = []
    right_boundary = []
    leaves = []

    def isLeaf(node):
        return not node.left and not node.right
    
    def addLeftBoundary(node,res):
        while node:
            if not isLeaf(node):
                res.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right
        return res
    
    def addRightBoundary(node,res):
        while node:
            if not isLeaf(node):
                res.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left
        return res[::-1]
    
    def addLeaves(node,res):
        if isLeaf(node):
            res.append(node.val)
        if node.left:
            addLeaves(node.left,res)
        if node.right:
            addLeaves(node.right,res)

    addLeftBoundary(root,left_boundary)

    addRightBoundary(root,right_boundary)

    addLeaves(root,leaves)

    return [*left_boundary,*leaves,*right_boundary]
    
                

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)