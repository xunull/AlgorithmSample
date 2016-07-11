def dfs(count,step=1,arr=-1,record=-1):
    '''
    深度优先搜索
    '''
    if arr == -1:
        arr=[0]*(count+1)
        record=[0]*(count+1)
        for temp in range(1,count):
            arr[temp]=temp+1
    for i in range(1,count+1):
        if step == count+1:
            # 输出数组的切片,数组第一个位置是0
            print(arr[1:])
            return
        if record[i]==0:
            # 第i个数字没有被使用过
            arr[step]=i
            record[i]=1
            dfs(count,step+1,arr,record)
            record[i]=0

dfs(4)
