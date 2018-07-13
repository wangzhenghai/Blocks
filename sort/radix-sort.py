import random

def radix_Sort(mylist):
	def maxBit(mylist):
		max_data = max(mylist)
		bitnum = 0
		while max_data:
			bitnum += 1
			max_data //= 10
		return bitnum
	def digit(num, i):
		p = 1
		while i > 0:
			i -= 1
			p *= 10
			return num // p % 10
	if len(mylist) == 0:
		return []
	sorted_list = mylist
	length = len(sorted_list)
	bucket = [0] * length
	for j in range(1, maxBit(sorted_list) + 1):
		count = [0] * 10
		for i in range(0, length):
			count[digit(sorted_list[i], j)] += 1
		for i in range(1, 10):
			count[i] += count[i -1]
		for i in range(0, length)[:: -1]:
			k = digit(sorted_list[i], j)
			bucket[count[k] - 1] = sorted_list[i]
			count[k] -= 1
		for i in range(0, length):
			sorted_list[i] = bucket[i]
	return sorted_list

if __name__ == '__main__':
	mylist = [random.randint(1, 100) for i in range(10)]
	print(radix_Sort(mylist))
