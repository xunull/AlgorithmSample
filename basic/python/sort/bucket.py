def bucketSort(input):
    '''简单的桶排序
    时间复杂度可以,但是浪费空间'''
    min=input[0]
    max=input[0]
    for temp1 in input:
        if temp1>max:
            max=temp1
        if temp1<min:
            min=temp1
    tempArr=[0]*(max+1)
    #print(tempArr)
    for temp2 in input:
        tempArr[temp2]+=1
    print(tempArr)
    for temp3 in range(len(tempArr)):
        for index in range(tempArr[temp3]):
            print(temp3)



testArr=[2,3,4,56,1,25,34,6,12]
# 输出方法的说明
print(bucketSort.__doc__)
bucketSort(testArr)
