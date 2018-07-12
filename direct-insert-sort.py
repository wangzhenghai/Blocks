import random

def insert_Sort(mylist):
	length = len(mylist)
	for i in range(1, length):
		j = i - 1
		if(mylist[i] < mylist[j]):
			temp = mylist[i]
			mylist[i] = mylist[j]
			j -= 1
			while(j >= 0 and mylist[j] > temp):
				mylist[j + 1] = temp
				j -= 1
			mylist[j + 1] = temp

if __name__ == '__main__':
	mylist = [random.randint(1, 100) for i in range(10)]
	print(insert_Sort(mylist))
