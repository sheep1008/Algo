import sys
sys.setrecursionlimit(10000)

class Node:
    def __init__(self, x, y, key):
        self.x = x
        self.y = y
        self.val = key
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, x, y, key):
        if not self.root:
            self.root = Node(x, y, key)
            return
        
        current_node = self.root
        while True:
            if current_node.x > x:
                if not current_node.left:
                    current_node.left = Node(x, y, key)
                    return
                current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = Node(x, y, key)
                    return
                current_node = current_node.right

def preorder(node, result):
    if node is None:
        return
    result.append(node.val)
    preorder(node.left, result)
    preorder(node.right, result)

def postorder(node, result):
    if node is None:
        return
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.val)

def solution(nodeinfo):
    node_list = []
    bst = BST()
    for index, (x, y) in enumerate(nodeinfo):
        node_list.append((index + 1, x, y))
    node_list.sort(key=lambda node: -node[2])
    
    for node_number, x, y in node_list:
        bst.insert(x, y, node_number)
        
    preorder_result = []
    postorder_result = []
    preorder(bst.root, preorder_result)
    postorder(bst.root, postorder_result)
    
    return [preorder_result, postorder_result]