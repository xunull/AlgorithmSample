#!/usr/local/bin/lua

function split(str,delimiter)
  if str==nil or str=="" or delimiter==nil
  then
    return nil
  end
  local i=1
  local j=0
  local k=0
  local result={}
  while true do
    j,k=string.find(str,delimiter,i)
    if j == nil
    then
      break
    end
    -- print(string.sub(str,i,j))
    table.insert(result,string.sub(str,i,j))
    i=k+1
  end
  -- print(i)
  table.insert(result,string.sub(str,i))
  return result
end
-- split("1 1"," ")

mazeArr={}
bookArr={}
startCoord={}
targetCoord={}
head=1
tail=1
que={}
nextStep={{-1,0},{0,1},{1,0},{0,-1}}

function bfs()
  currentCoord = {que[head][1],que[head][2]}
  flag=false
  while head<tail do
    print("head"..head)
    print("tail"..tail)
    for i=1,4 do

      currentCoord[1]=que[head][1]+nextStep[i][1]
      currentCoord[2]=que[head][2]+nextStep[i][2]
      if currentCoord[1]<= 0 or currentCoord[1]>#mazeArr or currentCoord[2]<= 0 or currentCoord[2]>#mazeArr[1] then

      else
        print("c1:"..currentCoord[1])
        print("c2:"..currentCoord[2])
        print(mazeArr[currentCoord[1]][currentCoord[2]])
        print(bookArr[currentCoord[1]][currentCoord[2]])

        if mazeArr[currentCoord[1]][currentCoord[2]]-0==0 and bookArr[currentCoord[1]][currentCoord[2]] == 0 then
          -- 不是障碍物，并且没有走过
          bookArr[currentCoord[1]][currentCoord[2]]=1
          table.insert(que,{currentCoord[1],currentCoord[2],que[head][3]+1})
          tail=tail+1
        end
        if currentCoord[1]==targetCoord[1] and currentCoord[2]==targetCoord[2] then
            flag=true
            break
        end
      end
    end
    if flag then
        break
    end
    head=head+1
  end
  print('最少的步数为:')
  print(que[#que][3])
end



print("输入迷宫,0表示空,1表示有障碍物,以空行结束")
while true do
  temp=io.read("*line")
  if temp == "" then
    break
  end
  table.insert(mazeArr,split(temp," "))
end
print("输入起始点坐标:")
startCoord=split(io.read("*line")," ")
for i,v in ipairs(startCoord) do
	startCoord[i] = tonumber(v)
end
print("输入目标点坐标:")
targetCoord=split(io.read("*line")," ")
for i,v in ipairs(targetCoord) do
	targetCoord[i] = tonumber(v)
end
for i,v in ipairs(mazeArr) do
  tempArr={}
	for j,k in ipairs(v) do
    table.insert(tempArr,0)
  end
  table.insert(bookArr,tempArr)
end
table.insert(que,{startCoord[1],startCoord[2],0})
tail = tail+1

bfs()
