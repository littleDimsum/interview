# Stack: stack of data
# LIFO ordering: last in, first out (most recent items: first items removed)
	# pop(): remove top item from stack | constant time
	# push(item): add item to top of stack | constant time
	# peek(): return the top of stack
	# isEmpty(): Return true iff stack is empty
	# no constant-time access to ith item

class Stacktime:
	def __init__(self):
		self.items = []
	def pop(self):
		self.items.pop()
	def push(self, item):
		self.items.append(item)
	def peek(self):
		return self.items[-1]
	def isEmpty(self):
		if len(self.items) == 0:
			return True
		else:
			return False
	def size(self):
		return len(self.items)

# good exercise: take a simple recursive algo and implement iteratively

S = Stacktime()
S.push(5)
S.push(8)
F = Stacktime()
print(S.peek())
print(F.isEmpty())
print(S.isEmpty())

# Queues
# FIFO: first in, first out
	# add(item): add to end 
	# remove(): remove first item
	# peek(): return top of queue
	# isEmpty(): return True iff queue empty

class QueueTime:
	# implement a front pointer (rather than shifting all items down by one with remove())
	# implement a count (# of items)
	def __init__(self):
		self.items = []
		self.count = len(self.items)
		#self.front = self.items[0]
	def size(self): 
		return len(self.items)
	def enqueue(self, item):
		self.count += 1
		self.items.append(item)
	def dequeue(self):
		self.count -= 1
		self.items = self.items[1:]
	def peek(self):
		return self.items[-1]
	def isEmpty(self):
		return len(self.items) == 0

Q = QueueTime()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
print(Q.items)
print(len(Q.items))
print(Q.dequeue())
print(Q.dequeue())
print(Q.peek())
print(Q.items)
