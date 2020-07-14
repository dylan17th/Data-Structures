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
        #current a new instance of listNode with value
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
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass




# if __name__ == '__main__':
    # my_list = DoublyLinkedList()
    # # my_list.add_to_tail(1)
    # # my_list.add_to_tail(3)
    # # print(my_list.length)
    # # print(my_list.tail.value)
    # # my_list.remove_from_tail()
    # print(my_list.tail)