import random

def merge_Sort(mylist):
	if len(mylist) > 1:
		mid = len(mylist) // 2
		left = mylist[: mid]
		right = mylist[mid :]
		merge_Sort(left)
		merge_Sort(right)
		i = j = k = 0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				mylist[k] = left[i]
				i += 1
			else:
				mylist[k] = right[j]
				j += 1
			k += 1
		while i < len(left):
			mylist[k] = left[i]
			i += 1
			k += 1
		while j < len(right):
			mylist[k] = right[j]
			j += 1
			k += 1

mylist = [random.randint(1, 100) for i in range(5)]
print(mylist)
merge_Sort(mylist)
print(mylist)
