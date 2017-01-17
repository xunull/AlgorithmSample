

def get_next(target):
    '''
    这里的代码是为了计算出当前要匹配的target的next数组
    '''
    i=1
    j=0
    # next=[]
    next=[0,0]

    for i in range(1,len(target)):
        while(j>0 and target[i] != target[j]):
            j=next[j]
        if(target[i] == target[j]):
            j+=1
        # next[i+1]=j
        next.append(j)

    # while i < len(target):
    #     if( j==0 or target[i] == target[j]):
    #         # target[i] 表示后缀的单个字符
    #         # target[j] 表示前缀的单个字符
    #         i+=1
    #         j+=1
    #         # next[i]=j
    #         next.append(j)
    #     else:
    #         j=next[j] # 若字符不相同,j值回溯
    return next

def index(source, target):
    # i=0
    # j=0
    # next=get_next(target)
    # print(next)
    # while (i<len(source) and j < len(target)):
    #     if(source[i] == target[i]):
    #         # 两个字母如果相等,则继续向下判断
    #         # 与普通的相比较 增加了 j=0
    #         i+=1
    #         j+=1
    #     else:
    #         # j 退回到合适的位置,i值不变
    #         j=next[j]
    #
    # if j >= len(target):
    #     print(i)
    #     return i - len(target)
    # else:
    #     return -1


    j=0
    next=get_next(target)
    for i in range(0,len(source)):
        while(j>0 and source[i] != target[j]):
            j = next[j]
        if(source[i] == target[j]):
            j+=1
        if(j == len(target)):
            print(i-j)
            j=next[j]


result = index('abc123abc','123')
print(result)
