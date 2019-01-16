# -*- encoding: utf-8 -*-

a = [
        [5,10,15,20,25],
        [4,9,14,19,24],
        [3,8,13,17,23],
        [1,6,12,16,21]
        ]

def find_x(x, n, m):
    i = n - 1
    j = 0

    while True:
        temp = a[i][j]
        if x >= a[i-1][j] and i >= 0:
            i = i - 1
        elif x >= a[i][j+1] and j < m - 1:
            j = j + 1
        else:
            break

    if temp == x:
        return True
    else:
        return False

if __name__ == "__main__":
    print(a)
    result = find_x(12, 4, 5)
    print(result)
