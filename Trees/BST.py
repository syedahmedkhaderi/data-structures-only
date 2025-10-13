class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.no_of_nodes = 0

    def search(self, data):
        if self.root is None:
            return "Tree Is Empty"
        else:
            curr = self.root
            while True:
                if curr is None:
                    return "Not Found"
                if curr.data == data:
                    return "Found"
                elif curr.data > data:
                    curr = curr.left
                elif curr.data < data:
                    curr = curr.right

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            self.no_of_nodes += 1
            return
        else:
            curr = self.root
            while True:
                if data < curr.data:
                    if curr.left is None:
                        curr.left = new_node
                        break
                    else:
                        curr = curr.left
                elif data > curr.data:
                    if curr.right is None:
                        curr.right = new_node
                        break
                    else:
                        curr = curr.right
                else:
                    # duplicate value — don't insert
                    break
            self.no_of_nodes += 1
            return

    def remove(self, data):
        # if tree is empty
        if self.root is None:
            return "Empty Tree"

        # Otherwise let's use 2 pointers to keep track of nodes
        curr = self.root
        parent = None

        # Let's traverse the BST
        while curr:
            # Compare data value

            if data > curr.data:
                parent = curr
                curr = curr.left

            elif data < curr.data:
                parent = curr
                curr = curr.right

            else:
            # If The deleting node is matched then you have to check different cases to rearrange.
            # curr is the value to delete and parent is above curr

            # Case 1: Has only Right Child
                if curr.left is None:
                    # check if your curr is root
                    if parent is None:
                        self.root = curr.left
                        return
                    else:
                    # You are deleting the curr here by pointing curr's parent to curr's child
                        if parent.data > curr.data:
                            parent.left = curr.left
                            return
                        else:
                            parent.right = curr.left
                            return

            # Case 2: Has Only Left Child
            # Same as above but just right and left are exchanged
                if curr.right is None:
                    if parent is None:
                        self.root = curr.left
                        return
                    else:
                        if parent.data > curr.data:
                            parent.left = curr.left
                            return
                        else:
                            parent.right = curr.left
                            return

            # Case 3: if no left or right node
                if curr.right and curr.left is None:
                    if parent is None:
                        curr = None
                        return

                    if parent.data > curr.data:
                        parent.left = None
                        return
                    else:
                        parent.right = None
                        return

            # Case 4: Both left and right child exists
                if curr.right and curr.left is not None:
                    # Creating 2 variable to Rearrange the In-order Successor.
                    deleting_node = curr.right
                    deleting_nodes_parent = curr.right

                    # Traversing to find the leftmost of the right subtree
                    while deleting_node.left is not None:
                        deleting_nodes_parent = deleting_node
                        deleting_node = deleting_node.left

                    # Now copy the leftmost of right subtree(In-order Successor) to curr. Basically replace curr
                    curr.data = deleting_node.data

                    '''
                    Now comes the special case where deleting_node is exact right child of curr then it
                    run the above while loop at all because 'Left is None'. In that case Just replace the
                    curr.right with deleting_node.right . Remember that the curr is already changed and has
                    the same value as deleting node now. So if the right child(deleting_node) has no child 
                    then it will be None or else it will just point to deleting_node.right
                    '''
                    if deleting_nodes_parent == deleting_node: # Means While Loop hasn't run.
                        curr.right = deleting_node.right
                        return

                    # Now comes another case where the leftmost has a right subtree

                    # If there is no subtree then just point it to None.
                    if deleting_node.right is None:
                        deleting_nodes_parent.left = None
                        return
                    # If there is then its value will always be less than the deleting_parent_node so it will
                    # come left side. Because thats how binary trees properties work.
                    else:
                        deleting_nodes_parent.left = deleting_node.right
                        return
        return "Not Found :("

    # This is a recursive function.
    def printt(self, curr):
        if curr is not None:
            self.printt(curr.left)
            print(str(curr.data))
            self.printt(curr.right)

    # This prints the whole tree.
    def print_tree(self):
        if self.root is not None:
            self.printt(self.root)

bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(6)
bst.insert(12)
bst.insert(8)

x = bst.search(6)
print(x)
y = bst.search(99)
print(y)

bst.print_tree()