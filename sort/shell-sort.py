import random

def shell_Sort(mylist):
	step = len(mylist) // 2
	while step > 0 :
		for i in range(step, len(mylist)):
			j = i
			while(j >= step and mylist[j - step] > mylist[j]):
				mylist[j], mylist[j - step] = mylist[j - step], mylist[j]
				j -= step
		step = step // 2

if __name__ == '__main__':
	mylist = [random.randint(1, 100) for i in range(10)]
	print(shell_Sort(mylist))
