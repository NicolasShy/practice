
def solution(A):
    a = set(A)
    b = set()
    length = len(A)
    for i in range(1, length + 2):
        b.add(i)

    return (b - a).pop()

if __name__ == "__main__":
    array1 = [3,4,5,1,2,6,8,9]
    # array1 = []
    print(solution(array1))