# use list as stack
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print("Stack:", stack)
popped = stack.pop()
print("Popped:", popped)
print("Modified Stack:", stack)
# use list as queue
queue = [3, 4, 5]
queue.append(6)
queue.append(7)
print("Queue:", queue)
popped = queue.pop(0)
print("Popped:", popped)
print("Modified Queue:", queue)
# sequence, tuple in python
sequence = [3, 4, 5]
tuple_example = (3, 4, 5)
print("Sequence:", sequence)
print("Tuple:", tuple_example)