from cmath import inf
import logging

class TreeNode:
    def __init__(self,value,index = None):
        self.left = None
        self.right = None
        self.val = value
        self.index = index
        
class InvalidBinarySearchTreeException(Exception):
    "Invalid Binary Search Tree!"
    pass

class ValueNotPresentException(Exception):
    "Value is not present within BST"
    pass

def pre_order(root):
    if root == None:
        return
    print(root.val,end=" ")
    pre_order(root.left)
    pre_order(root.right)
    
def in_order(root):
    if root == None:
        return
    in_order(root.left)
    print(root.val,end=" ")
    in_order(root.right)

def post_order(root):
    if root == None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val,end=" ")

def traverse(type,root):
    if type == 0:
        print("\nPre Order Traversal -> ",end="")
        pre_order(root)
    elif type == 1:
        print("\nIn Order Traversal -> ",end="")
        in_order(root)
    elif type == 2:
        print("\nPost Order Traversal -> ",end="")
        post_order(root)

def build_bst(arr):
    """
    Left Child (idx) = (2*idx + 1)
    Right Child (idx = (2*idx + 2)
    """
    if len(arr) == 0:
        raise InvalidBinarySearchTreeException
    
    stack = []
    root = TreeNode(arr[0],0)
    stack.append(root)
    
    while stack:
        curr = stack.pop()
        
        if 2*curr.index + 1 < len(arr) and arr[2*curr.index + 1] != None:
            curr.left = TreeNode(arr[2*curr.index + 1],2*curr.index + 1)
            stack.append(curr.left)
        
        if 2*curr.index + 2 < len(arr) and arr[2*curr.index + 2] != None:
            curr.right = TreeNode(arr[2*curr.index + 2],2*curr.index + 2)
            stack.append(curr.right)
    
    if not validate_bst(root):
        raise InvalidBinarySearchTreeException
    
    return root
    

def validate_bst(root,lower = -inf,upper = inf):
    if root is None:
        return True

    if not (lower < root.val < upper):
        return False

    if root.left != None:
        if not validate_bst(root.left,lower,root.val): return False
    if root.right != None:
        if not validate_bst(root.right,root.val,upper): return False
    
    return True


def insert(root,val):
    """
    How to use: 
    root = insert(root,val)
    """
    if root == None:
        return TreeNode(val)
    elif root.val < val:
        root.right = insert(root.right,val)
    elif root.val > val:
        root.left = insert(root.left,val)
    
    return root

def delete(root,val):
    """
    How to use: 
    root = the tree we choose to delete from
    val = the value within this tree we want to delete
    root = delete(root,x)
    """
    
    if root == None:
        return None
    
    if root.val == val:
        return delete_helper(root)
    elif root.val < val:
        root.right = delete(root.right,val)
    elif root.val > val:
        root.left = delete(root.left,val)
    
    return root

def delete_helper(root):
    if root.left == None and root.right == None:
        return None
    elif root.left != None and root.right == None:
        return root.left
    elif root.right != None and root.left == None:
        return root.right
    elif root.right != None and root.left != None:
        max_val = find_max(root.left)
        
        #delete leaf from left subtree
        #then set root val to max_val
        root.left = delete(root.left,max_val)
        root.val = max_val
        return root
        

def find_max(root):
    res = -1
    stack = [root]
    while stack:
        curr = stack.pop()
        res = max(res,curr.val)
        if curr.left != None:
            stack.append(curr.left)
        if curr.right != None:
            stack.append(curr.right)
    return res
        


def search(root,val):
    while root:
        if root.val == val:
            print(f'\nValue {val} is present within this BST!')
            return root
        elif val > root.val:
            root = root.right
        elif val < root.val:
            root = root.left
    
    raise ValueNotPresentException

def children_count(root):
    if root == None:
        return 0
    elif root.left != None and root.right != None:
        return 2
    elif root.left != None or root.right != None:
        return 1