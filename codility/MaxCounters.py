

def solution(N, A):
    max_counter = 0
    result = N * [0]

    max_counter_flag = True
    for i in A:
        if not i == N + 1:
            max_counter_flag = False
            break
    
    if max_counter_flag:
        return [0] * N

    for i in A:
        if i >= 1 and i <= N:
            result[i-1] += 1
            max_counter = max(max_counter, result[i-1])
        else:
            result = [max_counter] * N
        
    return result



if __name__ == "__main__":
    array1 = [3,4,4,6,1,4,4]
    n = 5
    print(solution(n, array1))