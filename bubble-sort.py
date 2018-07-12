import random

def bubble_Sort(mylist):
	for i in range(len(mylist) - 1):
		for j in range(len(mylist) - i -1):
			if(mylist[j] > mylist[j + 1]):
				mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
			j += 1
		i += 1

if __name__ == '__main__':
	mylist = [random.randint(1, 100) for i in range(10)]
	print(bubble_Sort(mylist))