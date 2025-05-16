class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
        

def rightSideView(root):
    if not root:
        return []
    queue = [(root,0)]
    hashMap={}
    while queue:
        node, line = queue.pop(0)
        if node.left:
            queue.append((node.left,line+1))
        if node.right:
            queue.append((node.right,line+1))
        hashMap[line]=node.val
    return hashMap.values()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(rightSideView(root))