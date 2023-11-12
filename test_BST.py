import unittest
import io
import sys
from BST import validate_bst, build_bst, traverse, insert, delete, search, InvalidBinarySearchTreeException, ValueNotPresentException

class TestBST(unittest.TestCase):
    
    def capture_output(self, func, *args, **kwargs):
        # Helper function to capture print output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        func(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue().strip()

    def test_build_bst_valid(self):
        arr = [10, 5, 15, 2, 7, None, 18]
        root = build_bst(arr)
        self.assertIsNotNone(root)
        self.assertTrue(validate_bst(root))

    def test_build_bst_invalid(self):
        arr = [10, 15, 5, 2, 7, None, 18]
        with self.assertRaises(InvalidBinarySearchTreeException):
            build_bst(arr)

    def test_traversal_pre_order(self):
        arr = [10, 5, 15, 2, 7, None, 18]
        root = build_bst(arr)
        output = self.capture_output(traverse, 0, root)
        self.assertEqual(output, 'Pre Order Traversal -> 10 5 2 7 15 18')
    
    def test_traversal_in_order(self):
        arr = [10, 5, 15, 2, 7, None, 18]
        root = build_bst(arr)
        output = self.capture_output(traverse, 1, root)
        self.assertEqual(output, 'In Order Traversal -> 2 5 7 10 15 18')
    
    def test_traversal_post_order(self):
        arr = [10, 5, 15, 2, 7, None, 18]
        root = build_bst(arr)
        output = self.capture_output(traverse, 2, root)
        self.assertEqual(output, 'Post Order Traversal -> 2 7 5 18 15 10')

    def test_insert(self):
        arr = [10, 5, 15, 2, 7, None, 18]
        root = build_bst(arr)
        insert(root, 17)
        self.assertTrue(search(root, 17))
    
    def test_pre_order_after_insertion(self):
        arr = [10, 5, 15, 2, 7, None, 18]
        root = build_bst(arr)
        insert(root, 17)
        output = self.capture_output(traverse, 0, root)
        self.assertEqual(output, 'Pre Order Traversal -> 10 5 2 7 15 18 17')

    def test_search_found(self):
        arr = [10, 5, 15, 2, 7, None, 18]
        root = build_bst(arr)
        result = search(root, 7)
        self.assertEqual(result.val, 7)

    def test_search_not_found(self):
        arr = [10, 5, 15, 2, 7, None, 18]
        root = build_bst(arr)
        with self.assertRaises(ValueNotPresentException):
            search(root, 19)
            
    def test_delete_leaf_node(self):
        # Build a tree and delete a leaf node
        arr = [10, 5, 15, None, None, None, 20]  # 20 is a leaf
        root = build_bst(arr)
        root = delete(root, 20)
        # After deleting leaf node 20, it should not be found
        with self.assertRaises(ValueNotPresentException):
            search(root, 20)

    def test_delete_node_with_one_child(self):
        # Build a tree and delete a node with one child
        arr = [10, 5, 15, 2, 6, None, 20]  # Node 15 has one child 20
        root = build_bst(arr)
        root = delete(root, 15)
        # After deleting node 15, it should not be found
        with self.assertRaises(ValueNotPresentException):
            search(root, 15)
        # Child node 20 should still exist
        self.assertIsNotNone(search(root, 20))

    def test_delete_node_with_two_children(self):
        # Build a tree and delete a node with two children
        arr = [10, 5, 15, 2, 6, 12, 20]  # Node 10 has two children 5 and 15
        root = build_bst(arr)
        root = delete(root, 10)
        # After deleting node 10, it should not be found
        with self.assertRaises(ValueNotPresentException):
            search(root, 10)
        # Both children should still exist
        self.assertIsNotNone(search(root, 5))
        self.assertIsNotNone(search(root, 15))

if __name__ == '__main__':
    unittest.main()
