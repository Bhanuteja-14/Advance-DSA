class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
#Tree Structure
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

#Tree Traversal techniques
'''
1.DFS (Depth First Search) Traversal
    a) Preorder Traversal (Root, Left, Right)
    b) Inorder Traversal (Left, Root, Right)
    c) Postorder Traversal (Left, Right, Root)
2.BFS (Breadth First Search) Traversal
    a) Level Order Traversal (Level by Level)
    '''
def Pre_Order(root):
    if root:
        print(root.data, end="->")
        Pre_Order(root.left)
        Pre_Order(root.right) 
print("Pre_Order:")
Pre_Order(root)

def In_Order(root):
    if root:
        In_Order(root.left)
        print(root.data, end="->")
        In_Order(root.right)
print("\nIn_Order:")
In_Order(root)

def Post_Order(root):
    if root:
        Post_Order(root.left)
        Post_Order(root.right)
        print(root.data, end="->")
print("\nPost_Order:")
Post_Order(root)

from collections import deque
def Level_Order(root):
    if root is None:
        return
    d = deque([root])
    while d:
        node = d.popleft()
        print(node.data, end="->")
        if node.left:
            d.append(node.left)
        if node.right:
            d.append(node.right)
print("\nLevel_Order Traversal:")
Level_Order(root)