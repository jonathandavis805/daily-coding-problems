from typing import TypeVar


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while current_node is not None and position + 1 != index:
                position = position + 1
                current_node = current_node.next

            if current_node is not None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while current_node is not None and position != index:
                position = position + 1
                current_node = current_node.next

            if current_node is not None:
                current_node.data = val
            else:
                print("Index not present")

    def remove_first_node(self):
        if self.head is None:
            return

        self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def remove_at_index(self, index):
        if self.head is None:
            return
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while current_node is not None and position + 1 != index:
                position = position + 1
                current_node = current_node.next

            if current_node is not None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    # Method to remove a node from linked list
    def remove_node(self, data):
        current_node = self.head

        if current_node.data == data:
            self.remove_first_node()
            return

        while current_node is not None and current_node.next.data != data:
            current_node = current_node.next

        if current_node is None:
            return
        else:
            current_node.next = current_node.next.next

    # Print the size of linked list
    def sizeOfLL(self):
        size = 0
        if self.head:
            current_node = self.head
            while current_node:
                size = size + 1
                current_node = current_node.next
            return size
        else:
            return 0

    # print method for the linked list
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def reverse_in_place(self):
        if self.head is None:
            return
        current_node = self.head
        self.head = current_node
        prev = None
        while current_node:
            next = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next
        self.head = prev
        print(prev)
        print(self.head)
        current_node = self.head
        while current_node.next:
            print(current_node.data)
            current_node = current_node.next
    
        

    def visualize(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                if type(current.data) == int:
                    print("█" * current.data)
                else:
                    print(current)
                current = current.next



def merge_2_sorted(list_1: LinkedList, list_2: LinkedList):
    result = LinkedList()
    if list_2.head.data > list_1.head.data:
        result.head = list_1.head
        list_1.head = list_1.head.next 
    else:
        result.head = list_2.head
        list_2.head = list_2.head.next 
    current = result.head
    while list_1.head or list_2.head:
        if list_2.head is None:
            current.next = list_1.head
            list_1.head = list_1.head.next
        elif list_1.head is None:
            current.next = list_2.head
            list_2.head = list_2.head.next 
        elif list_2.head.data > list_1.head.data:
            current.next = list_1.head
            list_1.head = list_1.head.next 
        else:
            current.next = list_2.head
            list_2.head = list_2.head.next 
        current = current.next
    
    return result
        
def merge_sorted(lists: list[LinkedList]):
    quantity = len(lists)
    quantity % 2
    lists[0]
