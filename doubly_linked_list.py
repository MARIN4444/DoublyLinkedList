from node import node
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    
    def isEmpty(self):
        return self.size == 0

    def append(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.size += 1


    def prepend(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size += 1

    
    def delete(self, data):
        if self.isEmpty():
            return False
        current = self.head
        if current.data == data:
            self.head = current.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self.size -= 1
            return True
        while current and current.data != data:
            current = current.next
        if not current:
            return False
        if current.next:
            current.next.prev = current.prev  
        else:
            self.tail = current.prev
        if current.prev:
            current.prev.next = current.next
        self.size -= 1  
        return True

    
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
        self.size += 1


    def getAt(self, index):
        if index < 0:
            raise IndexError("Index out of bounds")
        current = self.head
        for i in range(index):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next
        if current is None:
            raise IndexError("Index out of bounds")
        return current.data 
     
    
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
        index = 0
        while current:
            if current.data == data:
                return index
            index += 1
            current = current.next
        return -1
    
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



test_dll = DoublyLinkedList()
test_dll.append(1)  
