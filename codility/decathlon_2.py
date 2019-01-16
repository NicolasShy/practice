# -*- encoding:utf-8 -*-
def solution(A):

    if len(A) < 3:
        return -1
    else:
        min_triplet = 0
        N = len(A)

        diff_list = list()
        diff_temp = 0
        flag = True
        for i in range(1, N):
            if A[i] > A[i-1] and flag == True:
                diff_temp += A[i] - A[i-1]
            elif A[i] < A[i-1] and flag == False:
                diff_temp += A[i] - A[i-1]
            elif A[i] > A[i-1] and flag == False:
                flag = True
                diff_list.append(diff_temp)
                diff_temp = A[i] - A[i-1]
            else:
                flag = False
                if len(diff_list) != 0:
                    diff_list.append(diff_temp)
                diff_temp = A[i] - A[i-1]
        diff_list.append(diff_temp)
        len_diff = len(diff_list)
        if len_diff == 1:
            return -1
        if len_diff == 2 and diff_list[0] > 0:
            return -1

        if diff_list[0] > 0:
            for i in range(1, len_diff-1, 2):
                min_triplet = min(abs(diff_list[i]), diff_list[i+1])
            return min_triplet
            
        if diff_list[0] < 0:
            for i in range(0, len_diff-1, 2):
                min_triplet = min(abs(diff_list[i]), diff_list[i+1])
            return min_triplet
        

if __name__ == "__main__":
    array1 = [0,1,3,-2,0,1,0,-3,2,3]
    array2 = [0,1,3,-2,0,1,0,-3]
    array3 = [0,1] 
    array4 = [8]
    array5 = [1,7,-1]
    array6 = [1,-5,3]

    print(solution(array1))
    print(solution(array2))
    print(solution(array3))
    print(solution(array4))
    print(solution(array5))
    print(solution(array6))