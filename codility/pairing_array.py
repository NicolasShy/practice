
def solution1(A):
    # write your code in Python 3.6
    items = set(A)
    for i in items:
        item_count = A.count(i) 
        if item_count % 2 == 0:
            while item_count > 0:
                A.remove(i)
                item_count -= 1
        else:
            return i

def solution2(A):
    items = dict()
    for i in list(A):
        if not items.get(i):
            items[i] = 0
        items[i] += 1

    for i,j in items.items():
        if j % 2 != 0:
            return i 

if __name__ == "__main__":
    array1 = [9,3,4,5,9,3,5,4,188,12,12]
    print(solution2(array1))
    # print(solution2(array1))
