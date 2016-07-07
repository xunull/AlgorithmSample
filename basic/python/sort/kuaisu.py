def kuaisu(input,start=-1,end=-1):
    if start == -1:
        start=0
    if end == -1:
        end = len(input)
    '''
    时间复杂度，最坏的情况下跟冒泡法一样n的二次方
    平局复杂度nlogn
    快速排序是二分的思想
    '''
    benchmark=input[0]
    sentryA=input[0]
    sentryB=input[len(input)-1]

    for sentryAIndex in range(len(input)):
        for sentryBIndex in range(len(input)):
            pass

testArr=[2,3,4,56,1,25,34,6,12]

kuaisu(testArr)
