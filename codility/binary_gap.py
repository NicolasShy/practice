def solution(N):

    cnt = 0
    result = 0
    found_one = False
    i = N
    while i:
        print(i)
        print(cnt)
        print(result)
        print("***")
        if i & 1 == 1:
            if (found_one == False):
                found_one = True
            else:
                result = max(result,cnt)
            cnt = 0
        else:
            cnt += 1
        i >>= 1
    return result

def my_solution(N):
    # write your code in Python 3.6
    current = 0
    result = 0
    n = N
    while n & 1 == 0:
        n >>= 1
    list_n = list(bin(n))[2:]

    for i in list_n:
        if i == '0':
            current = current + 1
            result = max(result, current)
            print(result)
        else:
            current = 0
            
    return result

if __name__ == "__main__":
    print(my_solution(529))