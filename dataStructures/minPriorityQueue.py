class MinPriorityQueue():
	'''
		Min-Priority-Queue data structure, to be used in Prim's Algorithm for MST and Dijkstra's Algorithm
		Not implementing all functions - only those needed in Prim's
	'''
	def __init__(self, arr):
		'''
			arr - The array containing the tuples (priority, item) to be used for heap
			heapSize - The maximum size of the heap
		'''
		self.heapSize = len(arr)
		self.heap = arr
		# maintains item -> index relation
		self.index = {}
		for i in range(self.heapSize):
			self.index[self.heap[i][1]] = i
		self.buildMinHeap(arr)

	def _parent(self, i):
		'''
			Returns the parent of node at index i
		'''
		return (i-1) // 2

	def _left(self, i):
		'''
			Returns the index of the left child of node at index i
		'''
		return 2*i + 1

	def _right(self, i):
		'''
			Returns the index of the left child of node at index i
		'''
		return 2*i + 2

	def buildMinHeap(self, arr):
		'''
			Adds the elements of arr into a heap satisfying the min-heap property
			Stores the minHeap in self.heap
		'''
		# i needs to go from the last node with children to 0
		# so starting value of i is parent(n-1) = (n-1-1)//2 = n//2 - 1
		for i in range (self.heapSize//2 - 1, -1, -1):
			self._minHeapify(i)

	def _minHeapify(self, i):
		'''
			Restores the max-heap property at the subtree rooted at node i
		'''
		l = self._left(i)
		r = self._right(i)

		if l < self.heapSize and self.heap[l][0] < self.heap[i][0]:
			smallest = l
		else:
			smallest = i

		if r < self.heapSize and self.heap[r][0] < self.heap[smallest][0]:
			smallest = r

		if smallest != i:
			self.index[self.heap[i][1]] = smallest
			self.index[self.heap[smallest][1]] = i
			self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
			self._minHeapify(smallest)

	def heapExtractMin(self):
		if not self.heap:
			raise Exception("Heap Underflow")

		minimum = self.heap[0]
		self.index.pop(minimum[1])
		self.index[self.heap[self.heapSize-1][1]] = 0
		self.heap[self.heapSize-1], self.heap[0] = \
			self.heap[0], self.heap[self.heapSize-1]
		self.heapSize -= 1
		self._minHeapify(0)
		return self.heap.pop()             # actually removing the element

	def heapDecreaseKey(self, item, key):
		'''
			Decrease the priority of item to key (index not specified)
		'''
		i = self.index[item]
		if key > self.heap[i][0]:
			raise Exception("New key cannot be less than current key")

		# optimised implementation - CLRS Ex 6.5-6
		while i > 0 and self.heap[self._parent(i)][0] > key:
			self.heap[i] = self.heap[self._parent(i)]
			self.index[self.heap[i][1]] = i
			i = self._parent(i)
		self.heap[i] = (key, item)
		self.index[self.heap[i][1]] = i

	def isEmpty(self):
		if self.heapSize == 0:
			return True
		return False

	def containsItem(self, item):
		if item in self.index:
			return True
		return False

	def itemKey(self, item):
		'''
			Return the current priority of a given item
		'''
		if self.containsItem(item):
			return self.heap[self.index[item]][0]
		raise Exception("Item not in the heap.")

	def printHeap(self):
		print (self.heap)


if __name__ == "__main__":
	arr = [5,13,2,25,7,17,20,8,4]
	for i in range(len(arr)):
		arr[i] = (arr[i], i)

	print ("\nBuilding min priority queue...")
	heap = MinPriorityQueue(arr)
	heap.printHeap()

	print ("\nExtracting min...")
	heap.heapExtractMin()
	heap.printHeap()
	print (heap.index)

	print ("\nDecreasing value of item 7 to 2...")
	heap.heapDecreaseKey(7, 2)
	heap.printHeap()
	print (heap.index)

	print ("\n2 in the priority queue: {}".format(heap.containsItem(2)))
	print ("6 in the priority queue: {}".format(heap.containsItem(6)))

	print ("\nPriority of item 4: {}".format(heap.itemKey(4)))
	print ("Priority of item 7: {}".format(heap.itemKey(7)))
	print ("Priority of item 2: {}".format(heap.itemKey(2)))
