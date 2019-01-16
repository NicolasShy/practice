
def solution(A):
    N = len(A)
    sum = 0
    for i in A:
        sum += i

    min_difference = abs(sum - 2*A[0])
    left_sum = 0
    for p in range(1, N):
        left_sum = left_sum + A[p-1]
        min_difference = min(abs(2 * left_sum - sum), min_difference)
    return min_difference

if __name__ == "__main__":
    array1 = [10,1,2,3,4]
    array2 = [12,1]
    
    print(solution(array1))
    print(solution(array2))