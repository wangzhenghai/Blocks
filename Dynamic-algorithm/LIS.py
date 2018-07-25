def LIS(testlist):
    length = len(testlist)
    res = [1 for i in range(length)]
    for i in range(length):
        k = 0
        while k <= i:
            if (testlist[i] > testlist[k]) and (res[i] < res[k]  + 1):
                res[i] = res[k] + 1
            k += 1
    print(res)
    return max(res)

if __name__ == '__main__':
    import random
    testlist = [random.randint(1, 100) for i in range(10)]
    print(testlist)
    print(LIS(testlist))