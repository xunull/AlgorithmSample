def init():
    # 迷宫列表
    mazeArr=[]
    # 标记列表
    bookArr=[]

    print('输入迷宫,0表示空,1表示有障碍物,以空行结束')
    while True:
        line = input()
        if line == "":
            break
        else:
            tempArr = arrATOI(line.split(" "))
            mazeArr.append(tempArr)

    # print(mazeArr)
    bookArr=[0]*len(mazeArr)
    for i in range(len(mazeArr)):
        bookArr[i]=[0]*len(mazeArr[i])
    startCoord=arrATOI(input("输入起始坐标(第一个坐标是y坐标): ").split(" "))
    targetCoord = arrATOI(input('输入目标坐标(第一个坐标是y坐标): ').split(" "))
    global que
    global head
    global tail
    que.append([startCoord[0],startCoord[1],0])
    tail+=1
    bfs(mazeArr,bookArr,startCoord,targetCoord)

# 走下一步的坐标
nextStep={0:[-1,0],1:[0,1],2:[1,0],3:[0,-1]}
# 最小步数
minStep=0
que=[]
head=0
tail=0

def bfs(mazeArr,bookArr,startCoord,targetCoord,currentStep=0):
    currentCoord=[startCoord[0],startCoord[1]]
    global head
    global tail
    global que
    # 是否到达目标点的标记
    flag=False
    while head<tail:
        for i in range(4):
            currentCoord[0]=que[head][0]+nextStep.get(i)[0]
            currentCoord[1]=que[head][1]+nextStep.get(i)[1]

            if currentCoord[0]<0 or currentCoord[0]>len(mazeArr)-1 or currentCoord[1]<0 or currentCoord[1]>len(mazeArr[0])-1:
                # 超出了迷宫的范围
                continue
            else:
                if mazeArr[currentCoord[0]][currentCoord[1]] == 0 and bookArr[currentCoord[0]][currentCoord[1]] == 0:
                    # 不是障碍物，并且没有走过
                    bookArr[currentCoord[0]][currentCoord[1]]=1
                    currentStep+=1
                    que.append([currentCoord[0],currentCoord[1],que[head][2]+1])
                    tail+=1

                if currentCoord[0]==targetCoord[0] and currentCoord[1]==targetCoord[1]:
                    flag=True
                    break
        if flag:
            break
        head+=1
    print('最少的步数为:')
    print(que[len(que)-1][2])
    print(que)

# 将字符串转化为数字
def arrATOI(arr):
    for i in range(len(arr)):
        if isinstance(arr[i],list):
            arrATOI(arr[i])
        else:
            arr[i]=int(arr[i])
    return arr

init()
