import unittest
from doubly_linked_list import DoublyLinkedList
from node import node

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()
    
    def test_init(self):
        """Test initialization of empty list"""
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.assertEqual(self.dll.size, 0)
        self.assertTrue(self.dll.isEmpty())
    
    def test_append(self):
        """Test append operation"""
        self.dll.append(1)
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.tail.data, 1)
        self.assertEqual(self.dll.size, 1)
        
        self.dll.append(2)
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.tail.data, 2)
        self.assertEqual(self.dll.head.next.data, 2)
        self.assertEqual(self.dll.tail.prev.data, 1)
        self.assertEqual(self.dll.size, 2)
    
    def test_prepend(self):
        """Test prepend operation"""
        self.dll.prepend(1)
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.size, 1)
        
        self.dll.prepend(2)
        self.assertEqual(self.dll.head.data, 2)
        self.assertEqual(self.dll.head.next.data, 1)
        self.assertEqual(self.dll.tail.prev.data, 2)
        self.assertEqual(self.dll.size, 2)
    
    def test_delete(self):
        """Test delete operation"""
        # Test delete from empty list
        self.assertFalse(self.dll.delete(1))
        
        # Test delete the only element
        self.dll.append(1)
        self.assertTrue(self.dll.delete(1))
        self.assertTrue(self.dll.isEmpty())
        
        # Test delete first element
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertTrue(self.dll.delete(1))
        self.assertEqual(self.dll.head.data, 2)
        self.assertEqual(self.dll.size, 2)
        
        # Test delete middle element
        self.dll = DoublyLinkedList()
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertTrue(self.dll.delete(2))
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.head.next.data, 3)
        self.assertEqual(self.dll.tail.prev.data, 1)
        self.assertEqual(self.dll.size, 2)
        
        # Test delete last element
        self.dll = DoublyLinkedList()
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertTrue(self.dll.delete(3))
        self.assertEqual(self.dll.tail.data, 2)
        self.assertEqual(self.dll.size, 2)
        
        # Test delete non-existent element
        self.assertFalse(self.dll.delete(4))
    
    def test_insertAt(self):
        """Test insertAt operation"""
        # Test insert at beginning of empty list
        self.dll.insertAt(0, 1)
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.size, 1)
        
        # Test insert at beginning
        self.dll = DoublyLinkedList()
        self.dll.append(2)
        self.dll.insertAt(0, 1)
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.head.next.data, 2)
        self.assertEqual(self.dll.size, 2)
        
        # Test insert in middle
        self.dll.insertAt(1, 1.5)
        self.assertEqual(self.dll.head.next.data, 1.5)
        self.assertEqual(self.dll.size, 3)
        
        # Test insert at end
        self.dll.insertAt(3, 3)
        self.assertEqual(self.dll.tail.data, 3)
        self.assertEqual(self.dll.size, 4)
        
        # Test insert beyond bounds
        with self.assertRaises(IndexError):
            self.dll.insertAt(10, 10)
    
    def test_getAtt(self):
        """Test getAtt  operation"""
        # Test get from empty list
        with self.assertRaises(IndexError):
            self.dll.getAt(0)
        
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        
        # Test get first element
        self.assertEqual(self.dll.getAt(0), 1)
        
        # Test get middle element
        self.assertEqual(self.dll.getAt(1), 2)
        
        # Test get last element
        self.assertEqual(self.dll.getAt(2), 3)
        
        # Test get beyond bounds
        with self.assertRaises(IndexError):
            self.dll.getAt(3)
        with self.assertRaises(IndexError):
            self.dll.getAt(-1)
    
    def test_size_method(self):
        """Test size method"""
        self.assertEqual(self.dll.size, 0)
        
        self.dll.append(1)
        self.assertEqual(self.dll.size, 1)
        
        self.dll.append(2)
        self.assertEqual(self.dll.size, 2)
        
        self.dll.delete(1)
        self.assertEqual(self.dll.size, 1)
    
    def test_toList(self):
        """Test toList method"""
        self.assertEqual(self.dll.toList(), [])
        
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        
        self.assertEqual(self.dll.toList(), [1, 2, 3])
    
    def test_reverse(self):
        """Test reverse method"""
        self.dll.reverse()  # Should handle empty list
        
        self.dll.append(1)
        self.dll.reverse()  # Should handle single element
        self.assertEqual(self.dll.toList(), [1])
        
        self.dll.append(2)
        self.dll.append(3)
        self.dll.reverse()
        
        self.assertEqual(self.dll.toList(), [3, 2, 1])
        self.assertEqual(self.dll.head.data, 3)
        self.assertEqual(self.dll.tail.data, 1)
    
    def test_find(self):
        """Test find method"""
        self.assertEqual(self.dll.find(1), -1)  # Not found in empty list
        
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.dll.append(2)
        
        self.assertEqual(self.dll.find(1), 0)  # First element
        self.assertEqual(self.dll.find(2), 1)  # First occurrence of 2
        self.assertEqual(self.dll.find(3), 2)  # Middle element
        self.assertEqual(self.dll.find(4), -1)  # Not found
    
    def test_sort(self):
        """Test sort method"""
        self.dll.sort()  # Should handle empty list
        
        self.dll.append(3)
        self.dll.append(1)
        self.dll.append(4)
        self.dll.append(2)
        
        self.dll.sort()
        self.assertEqual(self.dll.toList(), [1, 2, 3, 4])
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.tail.data, 4)
    
    def test_forwardTraversal(self):
        """Test forward traversal"""
        self.assertEqual(self.dll.forwardTraversal(), [])
        
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        
        self.assertEqual(self.dll.forwardTraversal(), [1, 2, 3])
    
    def test_backwardTraversal(self):
        """Test backward traversal"""
        self.assertEqual(self.dll.backwardTraversal(), [])
        
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        
        self.assertEqual(self.dll.backwardTraversal(), [3, 2, 1])

if __name__ == '__main__':
    unittest.main()

