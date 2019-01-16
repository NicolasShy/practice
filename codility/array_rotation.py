# -*- encoding:utf-8 -*-

def solution(A, K):
    # write your code in Python 3.6
    if len(A) == 0:
        return A
    k = K % len(A)
    array_temp = len(A)*[None] 
    for i,j in enumerate(A):
        key = (i + k) % len(A)
        array_temp[key] = j
    return array_temp

if __name__ == "__main__":
    array1 = ['a','b','c','d','e','f','g']
    k1 = -3
    print(solution(array1, k1))