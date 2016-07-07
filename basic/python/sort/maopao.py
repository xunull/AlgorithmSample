def maopao(input):
    '''
    冒泡排序时间复杂度是n的二次方

    假如我们的计算机每秒钟可以运行 10 亿次,
    那么对 1 亿个数进行排序,桶排序只需要 0.1 秒,
    而冒 泡排序则需要 1 千万秒,达到 115 天之久
    '''
    for i in range(len(input)):
        for j in range(len(input)-i-1):
            if input[j]<input[j+1]:
                temp=input[j+1]
                input[j+1]=input[j]
                input[j]=temp

    print(input)

testArr=[2,3,4,56,1,25,34,6,12]

maopao(testArr)
