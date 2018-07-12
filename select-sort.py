import random


def select_Sort(mylist):
	length = len(mylist)
	for i in range(0, length):
		min_index = i
		for j in range(i+1, length):
			if mylist[j] < mylist[min_index]:
				#mylist[j], mylist[min_index] = mylist[min_index], mylist[j]
				min_index = j
		if i != min_index:
			mylist[i], mylist[min_index] = mylist[min_index], mylist[i]
		print('Round', i, ':', mylist)

if __name__ == '__main__':
	mylist = [random.randint(1, 100) for i in range(10)]
	select_Sort(mylist)
