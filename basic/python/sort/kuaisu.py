def kuaisu(input,start=-1,end=-1):

    if start == -1:
        start=0
    if end == -1:
        end = len(input)-1
    if start == end:
        return
    '''
    时间复杂度，最坏的情况下跟冒泡法一样n的二次方
    平局复杂度nlogn
    快速排序是二分的思想
    '''
    benchmark=input[start]
    # sentryA=input[start+1]
    sentryAIndex=start
    sentryBIndex=end
    # sentryB=input[end]

    for i in range(start,end):
        if input[sentryBIndex-(i-start)]<benchmark:
            sentryBIndex=i
            for j in range(sentryAIndex,sentryBIndex):
                if input[j]>benchmark:
                    sentryAIndex=j
                    temp=input[sentryBIndex]
                    input[sentryBIndex]=input[sentryAIndex]
                    input[sentryAIndex]=temp
                    break
                else:
                    pass
            if sentryAIndex == sentryBIndex:
                kuaisu(input,start,sentryBIndex)
                kuaisu(input,sentryBIndex,end)
        else:
            pass

testArr=[2,3,4,56,1,25,34,6,12]

kuaisu(testArr)
print(testArr)
