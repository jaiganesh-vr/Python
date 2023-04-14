class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert_node(self,data):
        if self.data is not None:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert_node(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert_node(data)

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data),
        if self.right:
            self.right.printTree()

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res

    def postorderTraversal(self, root):
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data)
        return res

root = Node(5)
root.insert_node(3)
root.insert_node(6)
root.insert_node(2)
root.insert_node(1)
root.insert_node(7)

queue = [root]

while len(queue)>0:
    for i in queue:
        print(i.data)
    print(".....")
    current_node = queue.pop(0)
    if current_node.left is not None:
        queue.append(current_node.left)
    if current_node.right is not None:
        queue.append(current_node.right)

