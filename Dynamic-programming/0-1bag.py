def bag(n, c, w, v):
#n is the number of items
#c is the volume of the bag
#w is the volume of the items
#v is the value of the items
        w.insert(0, 0)
        v.insert(0, 0)
        #'full' means just full to get the maximum
        #'none' means as long as to get the maximum 
        method = input('Please input the method: choices=[full, none]')
        if method == 'full':
                a = [[float('-inf')] * (c + 1) for j in range(n + 1)]
                for i in range(n + 1):
                        a[i][0] = 0
        if method == 'none':
                a = [[0] * (c + 1) for j in range(n + 1)]
        #res = [[0] * (c + 1) for j in range(n + 1)]
        #res = [[float('-inf')] * (c + 1) for j in range(n + 1)]
        #for i in range(n + 1):
                #res[i][0] = 0
        for i in range(1, n + 1):
                for j in range(1, c + 1):
                        if j < w[i]:
                                a[i][j] = a[i -1][j]
                        else:
                                a[i][j] = max(a[i - 1][j], a[i - 1][j - w[i]] + v[i])
        print(a)
        return a
        
def display(n, c, w, a):
        print('The most value is:', a[n][c])
        x = [False for i in range(n)]
        j = c
        for i in range(n, 0, -1):
                if a[i][j] > a[i - 1][j]:
                        x[i - 1] = True
                        j -= w[i]
        print('The item selected is:')
        for i in range(n):
                if x[i]:
                        print('NO.', i + 1)
                                
if __name__ == '__main__':
        test_n = 4
        test_c = 8
        test_w = [2, 3, 4, 5]
        test_v = [3, 4, 5, 6]
        a = bag(test_n, test_c, test_w, test_v)
        display(test_n, test_c, test_w, test_a)

