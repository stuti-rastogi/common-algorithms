class MaxHeap():
	def __init__(self, arr):
		'''
			arr - The array containing the elements to be used for heap
			heapSize - The maximum size of the heap
		'''
		self.heapSize = len(arr)
		self.heap = arr
		self.buildMaxHeap(arr)

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

	def buildMaxHeap(self, arr):
		'''
			Adds the elements of arr into a heap satisfying the max-heap property
			Stores the maxHeap in self.heap
		'''
		# i needs to go from the last node with children to 0
		# so starting value of i is parent(n-1) = (n-1-1)//2 = n//2 - 1
		for i in range (self.heapSize//2 - 1, -1, -1):
			self._maxHeapify(i)

	def _maxHeapify(self, i):
		'''
			Restores the max-heap property at the subtree rooted at node i
		'''
		l = self._left(i)
		r = self._right(i)

		if l < self.heapSize and self.heap[l] > self.heap[i]:
			largest = l
		else:
			largest = i

		if r < self.heapSize and self.heap[r] > self.heap[largest]:
			largest = r

		if largest != i:
			self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
			self._maxHeapify(largest)

	def heapSort(self):
		self.buildMaxHeap(self.heap)
		for i in range(self.heapSize-1, 0, -1):
			self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
			self.heapSize -= 1
			self._maxHeapify(0)

	############### PRIORITY QUEUE METHODS ###############

	def heapMaximum(self):
		return self.heap[0]

	def heapExtractMax(self):
		if not self.heap:
			raise Exception("Heap Underflow")

		maximum = self.heap[0]
		self.heap[self.heapSize-1], self.heap[0] = \
			self.heap[0], self.heap[self.heapSize-1]
		self.heapSize -= 1
		self._maxHeapify(0)
		self.heap.pop()             # actually removing the element

	def heapIncreaseKey(self, i, key):
		if key < self.heap[i]:
			raise Exception("New key cannot be less than current key")

		# optimised implementation - CLRS Ex 6.5-6
		while i > 0 and self.heap[self._parent(i)] < key:
			self.heap[i] = self.heap[self._parent(i)]
			i = self._parent(i)
		self.heap[i] = key

	def maxHeapInsert(self, key):
		self.heapSize = self.heapSize + 1
		self.heap.append(float("-inf"))
		self.heapIncreaseKey(self.heapSize-1, key)

	def printHeap(self):
		print (self.heap)


if __name__ == "__main__":
	arrA = [5,13,2,25,7,17,20,8,4]
	print ("\nBuilding max heap...")
	heapA = MaxHeap(arrA)
	heapA.printHeap()

	# print ("\nPerforming heapSort...")
	# heapA.heapSort()
	# heapA.printHeap()

	print ("\nExtracting max...")
	heapA.heapExtractMax()
	heapA.printHeap()

	print ("\nIncreasing value at index 4 to 50...")
	heapA.heapIncreaseKey(4, 50)
	heapA.printHeap()

	print ("\nInserting value of 25 in the heap...")
	heapA.maxHeapInsert(25)
	heapA.printHeap()
