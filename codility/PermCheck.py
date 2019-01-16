

def solution(A):
    # write your code in Python 3.6
    checkTable = [False]*len(A)
    for value in A:
        if value < 1 or value > len(A):
            return 0
        checkTable[value-1] = True
    
    for flag in checkTable:
        if not flag:
            return 0
    
    return 1

def my_solution(A):

    N = len(A)
    set_main = set(range(1, N + 1))
    set_a = set(A)
    if (not set_main.difference(set_a)) and (not set_a.difference(set_main)):
        return 1
    else:
        return 0

if __name__ == "__main__":
    array1 = [1]
    array2 = [3,4,5,1,2,7]
    array3 = [1,2,3,4,5,6]
    array4 = [4,1,3,2]
    print(my_solution(array1))
    print(my_solution(array2))
    print(my_solution(array3))
    print(my_solution(array4))
