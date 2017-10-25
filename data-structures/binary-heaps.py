# Binary heaps (min-heaps, max-heaps)
# complete binary treee

# MIN-HEAP:
	# each node smaller than it children
	# root = min element
	# key operations:
		# insert
		# extract min
			
class MinHeap:
	def __init__(self):
		self.keys = []
	def insert(self, key):
		self.keys.append(key)
		self.swap()
	def size(self):
		return len(self.keys)
	def swap(self):
		counter = self.size() 
		while counter//2 > 0:
			if self.keys[counter-1] < self.keys[(counter//2)-1]:
				old = self.keys[(counter//2)-1]
				self.keys[(counter//2)-1] = self.keys[counter-1]
				self.keys[counter-1] = old
			counter = counter // 2
	def del_min(self):
		self.keys[0] = self.keys[self.size()-1]
		self.keys.pop()
		self.trickle_down()
	def trickle_down(self):
		counter = 0
		while (2*counter+2) in range(self.size()):
			if self.keys[2*counter + 1] > self.keys[2*counter + 2]:
				byebye = self.keys[counter]
				self.keys[counter] = self.keys[2*counter+2]
				self.keys[2*counter+2] = byebye
				counter = 2 * counter + 2
			elif self.keys[2*counter + 1] < self.keys[2*counter + 2]:
				byebye = self.keys[counter]
				self.keys[counter] = self.keys[2*counter+1]
				self.keys[2*counter+1] = byebye
				counter = 2 * counter + 1
		
# H = MinHeap()
# H.insert(5)
# H.insert(1)
# H.insert(11)
# H.insert(8)
# H.insert(3)
# H.insert(10)
# H.insert(30)
# H.insert(7)
# H.insert(37)
# print(H.keys)
# H.del_min()
# print(H.keys)


# MAX-HEAP:
	# each node bigger than it children
	# root = mmax element
	# key operations:
		# insert
		# extract max

class MaxHeap:
	def __init__(self):
		self.keys = []
	def size(self):
		return len(self.keys)
	def insert(self, element):
		self.keys.append(element)
		print(M.keys)
		self.order()
	def order(self):
		counter = self.size()
		while counter//2 > 0:
			if self.keys[counter-1] > self.keys[(counter//2)-1]:
				adios = self.keys[(counter//2)-1]
				self.keys[(counter//2)-1] = self.keys[counter-1]
				self.keys[counter-1] = adios
			counter = counter//2
	def del_max(self):
		self.keys[0] = self.keys[self.size()-1]
		self.keys.pop()
		self.trinkle_down()

	def trinkle_down(self):
		counter = 0
		while (2*counter+2) in range(self.size()):
			if self.keys[2*counter + 1] > self.keys[2*counter+2]:
				swappo = self.keys[2*counter +1]
				self.keys[2*counter + 1] = self.keys[counter]
				self.keys[counter] = swappo
				counter = 2*counter + 1
			elif self.keys[2*counter + 1] < self.keys[2*counter+2]:
				swappo = self.keys[2*counter+2]
				self.keys[2*counter+2] = self.keys[counter]
				self.keys[counter] = swappo
				counter = 2*counter+2
M = MaxHeap()
M.insert(5)
M.insert(10)
M.insert(11)
M.insert(8)
M.insert(30)
M.insert(35)
M.insert(38)
M.insert(39)
print(M.keys)

M.del_max()
print(M.keys)


