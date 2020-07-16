from singly_linked_list2 import LinkedList


"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = [] #initializing the storge state
#     def __len__(self):
#         return len(self.storage) #returning the length of the storage state

#     def enqueue(self, value):
#         self.storage.insert(0, value) # inserting the value passes asd the parameter into the 0 index and moving other elements down
        
#     def dequeue(self):
#         if len(self.storage) == 0:
#             return None
#         else: 
#             last_element = self.storage[-1] #setting the number getting dequeued to last_element
#             self.storage = self.storage[:-1] #setting the array to itself minus the last element in the array
#             return last_element 

class Queue:
    def __init__(self):
        self.size = 0
        self.my_queue = LinkedList()
    def __len__(self):
        return self.size
    def enqueue(self, value):
        self.size += 1
        self.my_queue.add_to_tail(value)
    def dequeue(self):
        if self.size:
            self.size -= 1
            return self.my_queue.remove_head()
