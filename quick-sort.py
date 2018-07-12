import random

def quick_Sort(mylist, l, r):
	if l < r:
		q = partition(mylist, l, r)
		quick_Sort(mylist, l, q - 1)
		quick_Sort(mylist, q + 1, r)
		
def partition(mylist, l, r):
	x = mylist[r]
	i = l - 1
	for j in range(l, r):
		if mylist[j] <= x:
			i += 1
			mylist[i], mylist[j] = mylist[j], mylist[i]
	mylist[i + 1], mylist[r] = mylist[r], mylist[i + 1]
	return i + 1
if __name__ == '__main__':
	mylist = [random.randint(1, 100) for i in range(10)]
	quick_Sort(mylist, 0, len(mylist) - 1)
	print(mylist)
	
