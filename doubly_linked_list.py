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

    