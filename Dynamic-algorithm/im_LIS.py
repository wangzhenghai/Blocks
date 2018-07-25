def search(testdata, start, end, key):
    if start == end:
        return start
    mid = (start + end) // 2
    if testdata[mid] == key:
        return mid
    elif testdata[mid] > mid:
        return search(testdata, start, mid, key)
    else:
        return search(testdata, mid + 1, end, key)

def im_LIS(testdata):
    length = len(testdata)
    lis = [1 for i in range(length)]
    tmp = [0 for i in range(length)]
    num = 0
    for i in range(length):
        j = search(tmp, 0, num, testdata[i])
        if testdata[i] > tmp[j]:
            lis[i] = j + 1
        elif j > 1:
            lis[i] = j
        if lis[i] > num:
            num = lis[i]
            tmp[lis[i]] = testdata[i]
        elif (testdata[i] > tmp[j]) and (testdata[i] > tmp[j + 1]):
            tmp[j + 1] = testdata[i]
    return max(lis)

if __name__ == '__main__':
    import random
    testdata = [random.randint(1, 100) for i in range(10)]
    print(testdata)
    print(im_LIS(testdata))