import string

# 最小步数
# minStep

def init():
    '''
    深度优先算法
    迷宫路径搜索
    '''
    print('输入迷宫,0表示空,1表示有障碍物,以空行结束')
    mazeArr=[]
    while True:
        line=input()
        if line=='':
            break
        else:
            mazeArr.append(line.split(" "))
    startCoord=input('请输入起始坐标:')
    startCoord=startCoord.split(" ")
    targetCoord=input('请输入目标坐标:')
    targetCoord=targetCoord.split(" ")
    print(startCoord)
    print(targetCoord)
    arrATOI(mazeArr)
    arrATOI(startCoord)
    arrATOI(targetCoord)
    print(mazeArr)
    global minStep
    minStep=len(mazeArr)*len(mazeArr[0])

    recordCoords = list(mazeArr)
    recordCoords=[[1,0,0],[0,0,0],[0,0,0]]
    # for i in len(recordCoords):
    #     for j in len(recordCoords[i]):
    #         recordCoords[i][j]=0
    # recordCoords[startCoord[0]][startCoord[1]]=1
    print(recordCoords)

    # recordCoords=[len(mazeArr)][len(mazeArr[0])]
    # recordCoords=[[]]*len(mazeArr)
    # for i in range(len(mazeArr)):
    #     recordCoords[i]=[0]*len(mazeArr[0])
    # # for i in range(len(mazeArr)):
    # #     # recordCoords[i]=[]
    # #     for j in range(len(mazeArr[0])):
    # #         recordCoords[i][j]=0
    # recordCoords[startCoord[0]][startCoord[1]]=1

    dfs(mazeArr,0,startCoord,targetCoord,recordCoords)
    print("最短的步数为:")
    print(minStep)

# 将字符串数组转化为数值型
def arrATOI(arr):
    for i in range(len(arr)):
        if isinstance(arr[i],list):
            arrATOI(arr[i])
        else:
            # arr[i]=string.atoi(arr[i])
            arr[i]=int(arr[i])

nextStep=[[0,-1],[1,0],[0,1],[-1,0]]


def dfs(mazeArr,step ,startCoord,targetCoord,recordCoords,currentStep=0,currentCoord=-1):

    shangbian=0
    xiabian=len(mazeArr)-1
    zuobian=0
    youbian=len(mazeArr[0])-1
    if currentCoord == -1:
        currentCoord=[startCoord[0],startCoord[1]]

    print(currentCoord[0])
    print(currentCoord[1])
    print(currentStep)
    for i in range(4):
        if i == 0:
            # 上
            currentCoord[0]=startCoord[0]+nextStep[0][0]
            currentCoord[1]=startCoord[1]+nextStep[0][1]
        elif i == 1:
            # 右
            currentCoord[0]=startCoord[0]+nextStep[1][0]
            currentCoord[1]=startCoord[1]+nextStep[1][1]
        elif i == 2:
            # 下
            currentCoord[0]=startCoord[0]+nextStep[2][0]
            currentCoord[1]=startCoord[1]+nextStep[2][1]
        else:
            # 左
            currentCoord[0]=startCoord[0]+nextStep[3][0]
            currentCoord[1]=startCoord[1]+nextStep[3][1]

        # 先判断是否到达了目标位置
        if currentCoord[0]==targetCoord[0] and currentCoord[1]==targetCoord[1]:
            # 到达了目标位置
            currentStep+=1
            if currentStep<minStep:
                global minStep
                minStep=currentStep
                print("找到一个路径步数为")
                print(currentStep)
                print(recordCoords)
                return
        else:
            if currentCoord[0]<zuobian or currentCoord[0]>youbian or currentCoord[1]<shangbian or currentCoord[1]>xiabian:
                # 超出范围了
                # dfs(mazeArr,0,currentCoord,targetCoord,currentStep,currentCoord)
                # return
                pass
            else:
                if recordCoords[currentCoord[0]][currentCoord[1]] == 0:
                    if mazeArr[currentCoord[0]][currentCoord[1]] == 1:
                        # 障碍物
                        # dfs(mazeArr,0,currentCoord,targetCoord,currentStep,currentCoord)
                        # return
                        pass
                    else:
                        currentStep+=1
                        recordCoords[currentCoord[0]][currentCoord[1]] = 1
                        dfs(mazeArr,0,[currentCoord[0],currentCoord[1]],targetCoord,recordCoords,currentStep,[currentCoord[0],currentCoord[1]])
                        recordCoords[currentCoord[0]][currentCoord[1]] = 0




init()
