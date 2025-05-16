class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
        
        

# We are going to use the line logic with a hashmap and a queue
# We will use the hashmap to store the line number and the node value
# We will use the queue to store the node and the line number
# We will traverse the tree level by level and add the node and the line number to the hashmap
# We will then return the hashmap values

def topView(root):
    if not root:
        return []
    hashMap = {}
    queue = [(root,0)]
    while queue:
        node, line = queue.pop(0)
        if node.left:
            queue.append((node.left,line-1))
        if node.right:
            queue.append((node.right,line+1))
        if line not in hashMap:
            hashMap[line] = node.val
    
    return sorted(hashMap.values())

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(topView(root))