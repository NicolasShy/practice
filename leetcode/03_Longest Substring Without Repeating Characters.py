import time


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1

        attr_set = set(s)

        print('需要查找的元素有：%d', attr_set)
        maxlen_c = 0
        while len(attr_set) > 0:
            c = attr_set.pop()
            print('弹出：' + c)
            print('current max len c: %d' %maxlen_c)
            # find the longest substring without repeating character starts with this character
            maxlen_c = max(self.wingman(c, s), maxlen_c)

        return maxlen_c

    def wingman(self, char, s):
        maxlen_c = 1
        i = s.find(char)
        print('element ' + char + ' start with index ' + str(i))
        while i + maxlen_c < len(s):
            print('the value of i: %d' % i)
            if (s[i] == char):
                # find the character and try to reach the right ones
                substring = ''
                j = i
                while True:
                    substring = s[i:j + 2]
                    # print("%d %d %s" % (i, j, substring))
                    if (len(set(substring)) == len(substring)):
                        j += 1
                    else:
                        j -= 1  #remove the last one
                        substring = substring[:-1]
                        break
                i += 1
                maxlen_c = len(substring)
                print('这个i查找完成，往后找')
                time.sleep(1)
            else:
                i += 1
                print('switch i')
                continue

        return maxlen_c


if __name__ == "__main__":
    a = 'pwwkew'
    b = Solution().lengthOfLongestSubstring(a)
    print(b)