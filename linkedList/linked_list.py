class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        try:
            new_node = Node(value)
            if not self.head:
                self.head = self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            self.size += 1
        except Exception as e:
            print(f"Error adding value: {e}")

    def insert(self, index, value):
        try:
            if index < 0 or index > self.size:
                raise IndexError("Index out of range")
            new_node = Node(value)
            if index == 0:
                if not self.head:
                    self.head = self.tail = new_node
                else:
                    new_node.next = self.head
                    self.head.prev = new_node
                    self.head = new_node
            elif index == self.size:
                self.add(value)
            else:
                current = self.head
                for _ in range(index):
                    current = current.next
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = new_node
            self.size += 1
        except IndexError as e:
            print(f"Error inserting value: {e}")
        except Exception as e:
            print(f"General error: {e}")

    def remove(self, index):
        try:
            if index < 0 or index >= self.size:
                raise IndexError("Index out of range")
            if index == 0:
                if self.head == self.tail:
                    self.head = self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif index == self.size - 1:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                current = self.head
                for _ in range(index):
                    current = current.next
                current.prev.next = current.next
                current.next.prev = current.prev
            self.size -= 1
        except IndexError as e:
            print(f"Error removing element: {e}")
        except Exception as e:
            print(f"General error: {e}")

    def clear(self):
        try:
            self.head = self.tail = None
            self.size = 0
        except Exception as e:
            print(f"Error clearing linked list: {e}")

    def read_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    self.add(line.strip())
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except Exception as e:
            print(f"Error reading from file: {e}")

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return str(values)


linked_list = LinkedList()

linked_list.read_from_file("LinkedList.txt")
linked_list.remove(3)
linked_list.add(2)
linked_list.insert(1, 9)

print("LinkedList:")
print(linked_list)
