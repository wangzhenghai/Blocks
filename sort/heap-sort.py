import random

def max_Heap(heap, heapsize, root):
	left = 2 * root + 1
	right = left + 1
	larger = root 
	if left < heapsize and heap[larger] < heap[left]:
		larger = left 
	if right < heapsize and heap[larger] < heap[right]:
		larger = right 
	if larger != root:
		heap[larger], heap[root] = heap[root], heap[larger]
		max_Heap(heap, heapsize, larger)
		
def build_Heap(heap):
	heapsize = len(heap)
	for i in range((heapsize // 2 -1), -1, -1):
		max_Heap(heap, heapsize, i)
	
def heap_Sort(heap):
	build_Heap(heap)
	for i in range(len(heap))[::-1]:
	#for i in range(len(heap) - 1, -1, -1):
		heap[0], heap[i] = heap[i], heap[0]
		max_Heap(heap, i, 0)
	return heap
	
if __name__ == '__main__':
	mylist = [random.randint(1, 100) for i in range(10)]
	print(heap_Sort(mylist))