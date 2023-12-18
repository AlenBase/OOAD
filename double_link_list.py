class Node:
    def __init__(self, data=None):
        self._data = data
        self._next = None
        self._prev = None

    @property
    def data(self):
        return self._data

    @property
    def next(self):
        return self._next

    @property
    def prev(self):
        return self._prev

    @data.setter
    def data(self, new_data):
        self._data = new_data

    @next.setter
    def next(self, new_next):
        self._next = new_next

    @prev.setter
    def prev(self, new_prev):
        self._prev = new_prev


class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def is_empty(self):
        return self._head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node

    def delete(self, data):
        current = self._head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self._head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self._tail = current.prev

                return
            current = current.next

    def insert_after(self, target_data, data):
        current = self._head
        while current:
            if current.data == target_data:
                new_node = Node(data)
                new_node.prev = current
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                current.next = new_node

                if new_node.next is None:
                    self._tail = new_node

                return
            current = current.next

    def insert_before(self, target_data, data):
        current = self._head
        while current:
            if current.data == target_data:
                new_node = Node(data)
                new_node.next = current
                new_node.prev = current.prev
                if current.prev:
                    current.prev.next = new_node
                current.prev = new_node

                if new_node.prev is None:
                    self._head = new_node

                return
            current = current.next

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self._head

        if self._head:
            self._head.prev = new_node

        self._head = new_node

        if self._tail is None:
            self._tail = new_node

    def display(self):
        elements = []
        current = self._head
        while current:
            elements.append(current.data)
            current = current.next

        print("Doubly Linked List:", elements)





doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append(1)
doubly_linked_list.append(2)
doubly_linked_list.append(3)
doubly_linked_list.display()
doubly_linked_list.prepend(0)
doubly_linked_list.display()
doubly_linked_list.prepend(-1)
doubly_linked_list.display()
