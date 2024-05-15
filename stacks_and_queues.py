'''Creating stacks and queues in python'''
# stacks, last-in/first-out, are built-in without a library 
my_stack = [0,]
my_stack.append(1)
my_stack.append(2)
my_stack.append(3)
print(my_stack)
print("Popping", my_stack.pop())
print("Popping", my_stack.pop())
print(my_stack)

# queues, first-in/first-out, uses collections.deque
from collections import deque
my_queue = deque([0,])
my_queue.append(1)
my_queue.append(2)
my_queue.append(3)
print(my_queue)
print("Queuing", my_queue.popleft())
print("Queuing", my_queue.popleft())
print(my_queue)

