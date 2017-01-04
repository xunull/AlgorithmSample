'''
字符串匹配,常规方法是遍历source的每一个位置,然后从该位置开始和target每一个开始匹配
这种方法的复杂度是O(mn),m是source的长度,n是target的长度

kmp算法通过一个O(m)的预处理,使匹配的复杂度将为O(n+m)
'''


def get_next(target):
    '''
    这里的代码是为了计算出当前要匹配的target的next数组
    next数组中的值表示的是 长度为i的字符串的前缀和后缀的最大公共长度
    下标从1开始后有效

    如果想求next[i+1]的长度时,如果位置i和位置next[i]处的两个字符相同,则next[i+1]等于next[i]+1
    如果两个字符不相等,则可以将长度为next[i]的字符串继续分割,获得其最大公共长度next[next[i]],
    然后在和位置i的字符相比较.
    这是因为长度为next[i]的前缀和后缀都可以分割成上部的构造,如果位置next[next[i]]和位置i的字符相同，
    则next[i+1]就等于next[next[i]]加1。
    如果不相等，就可以继续分割长度为next[next[i]]的字符串，直到字符串长度为0为止。
    '''

    j=0
    # next 表示长度为i的字符串前缀和后缀的最大公共部分,从1开始 (下标表示的是字符串的长度)
    next=[0,0]
    # i是字符串的下标,从1        开始
    for i in range(1,len(target)):
        # j在每次循环开始都表示next[i]的值,同时表示需要比较的下一个位置
        while(j>0 and target[i] != target[j]):
            j=next[j]
        if(target[i] == target[j]):
            j+=1
        next.append(j)

    return next

def index(source, target):

    j=0
    next=get_next(target)
    for i in range(0,len(source)):
        while(j>0 and source[i] != target[j]):
            j = next[j]
        if(source[i] == target[j]):
            j+=1
        if(j == len(target)):
            print(i-j+1)
            j=next[j]

# index('abc123abc','123')

index('abcabc123abc123','123')
