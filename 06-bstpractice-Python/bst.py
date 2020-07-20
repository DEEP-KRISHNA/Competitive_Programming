class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        temproot = self.root
        while (temproot != None):
            if (new_val > temproot.value):
                # print(temproot.value)
                temproot = temproot.right
            else:
                print(temproot.value)
                temproot = temproot.left
        temproot = Node(new_val)

    def printSelf(self):
        # Your code goes here
        pass
        
    def search(self, find_val):
        # Your code goes here
        # pass
        temproot = self.root
        while (temproot != None):
            print(temproot.value)
            if (temproot.value == find_val):
                return True
            if (find_val > temproot.value):
                temproot = temproot.right
            else:
                temproot = temproot.left
        return False

if __name__ == "__main__":
    tree = BST(4)
    # print(tree.search(4))
    # print(tree.search(6))
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)
    # print(tree.search(5))
    # print(tree.search(6))
