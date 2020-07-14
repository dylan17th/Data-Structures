"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
        
    def delete(self):
        pass
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1

        if self.head == None:
            self.head = new_node
            self.tail = new_node

        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length >= 1:

            self.length -= 1
            value = self.head.value
            if self.head is self.tail:
                self.head = None
                self.tail = None
                return value

            self.head.next.prev = self.head.prev
            self.head = self.head.next
            return value

        else:
            return None
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1

        if self.tail == None:
            self.head = new_node
            self.tail = new_node

        if self.tail:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length >= 1:

            self.length -= 1
            value = self.tail.value
            if self.tail is self.head:
                self.head = None
                self.tail = None
                return value

            self.tail.prev.next = self.tail.next
            self.tail = self.tail.prev
            return value
        else:
            return None
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.length == 2:
            self.head.next = None
            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head, self.tail = self.tail, self.head

        if self.length > 2:
            if node is not self.tail:
                node.prev.next = None
                self.tail = node.prev
                node.next = self.head
                node.prev = None
                self.head.prev = node
                self.head = node
            
            if node is self.tail:
                node.next.prev = node.prev
                node.prev.next = node.next
                self.head.previous = node
                node.next = self.head
                node.prev = None
                self.head = node

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):

        if self.length == 2:
            node.next = None
            self.tail.next = node
            node.prev = self.tail
            self.tail.prev = None
            self.head, self.tail = self.tail, self.head

        if self.length > 2:
            if node is self.head:
                node.next.prev = None
                node.prev = self.tail
                self.tail.next = node
                node.next = None
                self.tail = node

            if node is not self.head:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 1:
            self.length -= 1
            self.head = None 
            self.tail = None

        if self.length == 2:
            self.length -= 1
            if node is self.tail:
                node.prev.next = None
                self.tail = self.head
            if node is self.head:
                node.next.prev = None
                self.head = self.tail

        if self.length >= 3:
            self.length -= 1

            if node.prev == None:
                node.next.prev = None
                self.head = node.next

            if node.next == None:
                node.prev.next = None
                self.tail = node.prev

            if node.prev and node.next != None:
                node.prev.next = node.next
                node.next.prev = node.prev

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max_value = 0
        current_node = self.head
        while current_node != None:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next
        return max_value       