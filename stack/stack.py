from singly_linked_list2 import LinkedList
from singly_linked_list2 import Node


"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        current_node = self.storage.head
        length_of_storage = 0
        while current_node:
            length_of_storage = length_of_storage + 1
            current_node = current_node.get_next()
        return length_of_storage
    def push(self, value):
        self.storage.add_to_tail(value)
    def pop(self):
        return self.storage.remove_tail()


# Using an array
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)
#     def pop(self):
#         if len(self.storage) == 0:
#             return None
#         else:
#             last_element = self.storage[-1]
#             self.storage.pop()
#             return last_element



if __name__ == '__main__':
    my_stack = Stack()
    print(len(my_stack))
    my_stack.push(1)
    my_stack.push(2)
    # my_stack.push(3)
    print(len(my_stack))
    my_stack.pop()
    print(len(my_stack))