class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def delete(self, key):
        current = self.head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next
    
    def insertAt(self, index, data):
        if index == 0:
            self.prepend(data)
            return
        new_node = node(data)
        current = self.head
        for i in range(index - 1):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        else:
            self.tail = new_node
        current.next = new_node

    def getAt(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next
        return current.data if current else None

    def isEmpty(self):
        return self.head is None   
    
    def toList(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def reverse(self):
        current = self.head
        prev = None
        while current:
            prev = current.prev
            current.prev = current.next
            current.next = prev
            current = current.prev
        if prev:
            self.head = prev.prev
        if self.head:
            self.tail = self.head
            while self.tail.next:
                self.tail = self.tail.next  

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None
    
    def sort(self):
        if self.head is None:
            return
        current = self.head
        while current:
            index = current.next
            while index:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                index = index.next
            current = current.next

    def forwardTraversal(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def backwardTraversal(self):
        result = []
        current = self.tail
        while current:
            result.append(current.data)
            current = current.prev
        return result

import unittest
from doubly_linked_list import DoublyLinkedList, Node

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
    
    def test_getAt(self):
        """Test getAt  operation"""
        # Test get from empty list
        with self.assertRaises(IndexError):
            self.dll.getAt(0)
        
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        
        # Test get first element
        self.assertEqual(self.dll.getA(0), 1)
        
        # Test get middle element
        self.assertEqual(self.dll.getA(1), 2)
        
        # Test get last element
        self.assertEqual(self.dll.getA(2), 3)
        
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