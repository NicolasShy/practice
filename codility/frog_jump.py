
def solution(X, Y, D):
    if X == Y:
        return 0
    distence = Y - X
    if distence > D:
        if distence % D == 0:
            times = distence/D
        else:
            times = distence/D + 1
    else:
        times = 1 
    return int(times)

if __name__ == "__main__":
    x = 12
    y = 14
    d = 1
    print(solution(x,y,d))