# -*- encoding: utf-8 -*-

# 
# def no_name(a, b):
#     if len(a) != len(b):
#         return False
# 
#     for x in enumerate(a):
#         print x
# 

def no_name(str1, str2):
    if len(str1) != len(str2):
        return False
    list1 = list(str1)
    list2 = list(str2)
    for i in list(list1):
        if i in list2:
            list1.remove(i)
            list2.remove(i)
        else:
            return False
    return True

if __name__ == "__main__":
    # str1 = ['a','b','c','d','e','f','g']
    # str2 = ['s','i','j','k','l','f','g']
    
    # str3 = str1[1:2]
    # no_name(str1, str2)
    
    str1 = "abcdefg"
    str2 = "bcdefga"
    str3 = "abcdeff"
    result = no_name(str1, str2)
    print(result)

    # a = list("abcdeeefsdhfigashdfohoifh")
    # print(len(a))
    # print("*****")
    # b = list()
    # for j in list(a):
    #     b.append(j)
    #     a.remove(j)
    #     print(j)
    #     print(len(a))
    #     print(a)
