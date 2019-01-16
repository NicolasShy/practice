#-*- encoding: utf-8 -*-
import time

def time_check(func):

    def wrapper(s,p):
        start_time = time.clock()
        result = func(s,p)
        end_time = time.clock()
        print end_time - start_time
        return result

    return wrapper

@time_check
def hello(s, p):
    print s
    print p
    print s + p
    return '1'

@time_check
def naive_match(s, p):
    m = len(s); n = len(p)
    for i in range(m-n+1):#起始指针i
        if s[i:i+n] == p:
            return True
    return False

#KMP
@time_check
def kmp_match(s, p):
    m = len(s); n = len(p)
    cur = 0#起始指针cur
    table = partial_table(p)
    while cur<=m-n:
        for i in range(n):
            if s[i+cur]!=p[i]:
                cur += max(i - table[i-1], 1)#有了部分匹配表,我们不只是单纯的1位1位往右移,可以一次移动多位
                break
        else:
            return True
    return False
 
#部分匹配表
def partial_table(p):
    '''partial_table("ABCDABD") -> [0, 0, 0, 0, 1, 2, 0]'''
    prefix = set()
    postfix = set()
    ret = [0]
    for i in range(1,len(p)):
        prefix.add(p[:i])
        postfix = {p[j:i+1] for j in range(1,i+1)}
        ret.append(len((prefix&postfix or {''}).pop()))
    return ret

if __name__ == "__main__":
    print naive_match("BBC ABCDAB ABCDABCDABDE", "ABCDABD")
    print partial_table("ABCDABD")
    print kmp_match("BBC ABCDAB ABCDABCDABDE", "ABCDABD")

    # b = hello("BBC ABCDAB ABCDABCDABDE", "ABCDABD")
    