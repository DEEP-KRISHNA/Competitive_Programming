class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        # Your code goes here
        temp = self.preorder_search(self.root, find_val)
        if (temp == None):
            return False
        else:
            return temp
        # return self.preorder_search(self.root, find_val)
        # pass

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        # Your code goes here
        pass

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        # Your code goes here
        print(start.value)
        if (start.value == find_val):
            return True
        elif (start == None or (start.left==None and start.right==None)):
            return False
        if(start.left!=None):
            return self.preorder_search(start.left, find_val)
        if(start.right!=None):
            return self.preorder_search(start.right, find_val)
        # pass

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        # Your code goes here
        pass


if __name__ == "__main__":
    tree = BinaryTree(1)
    # print(tree.search(6))
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    print(tree.search(4))
