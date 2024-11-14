class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.last is None:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def dequeue(self):
        if self.first is None:
            return None
        previous_value = self.first.value
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return previous_value

    def is_empty(self):
        return self.first is None

    def peek(self):
        if self.first is None:
            return None
        return self.first.value

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                if current_node == self.head:
                    self.head = current_node.next
                if current_node == self.tail:
                    self.tail = current_node.prev
                return True
            current_node = current_node.next
        return False

    def display_forward(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=' ')
            current_node = current_node.next
        print()

    def display_backward(self):
        current_node = self.tail
        while current_node:
            print(current_node.value, end=' ')
            current_node = current_node.prev
        print()
