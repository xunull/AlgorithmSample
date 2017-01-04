# 这里实现的不是kmp 算法,是最简单的匹配字符串的方法


def index(source,target,pos):
    i = pos
    j = 0

    while (i < len(source) and j < len(target)):

        if(source[i] == target[j]):
            i+=1
            j+=1
        else:
            i = i-j+1 # i 返回到上次匹配首位的下一位 (i 的回溯, 每次回溯 就是一次重新匹配子串)
            j = 0

    if j >= len(target):
        return i-len(target) # 已经成功的找到了子串的位置
    else:
        return -1 # 没有找到目录的子串

result = index('abc123abc','123',0)
print(result)
