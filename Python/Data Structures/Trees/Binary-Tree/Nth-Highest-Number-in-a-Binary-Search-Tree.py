from binary_tree import *
from binary_tree_node import *
current_count = 0

def find_nth_highest_in_bst_rec(node, n):
    # Base case: we return None if the current node is None
    if not node:
        return None

    # Checking for nth highest node in right subtree
    result = find_nth_highest_in_bst_rec(node.right, n)
    
    # If we find the nth highest node in the right subtree we return it
    if result:
        return result

    # Update the current count of nodes visited in reverse in-order
    global current_count
    current_count = current_count + 1

    # When the current count equals n, then we have found the nth highest
    # value node and return it	
    if n == current_count:
        return node

    # Checking for nth highest node in left subtree
    result = find_nth_highest_in_bst_rec(node.left, n)
    
    # If we find the nth highest node in the left subtree we return it
    if result:
        return result
    
    # Function to find the nth highest node
    return None

# Function to find the nth highest node
def find_nth_highest_in_bst(root, n):
    # Reset the current count to zero
    global current_count
    current_count = 0

    # Return None if the tree itself is None
    if not root:
        return None

    # Making the first recursive call
    return find_nth_highest_in_bst_rec(root, n)

