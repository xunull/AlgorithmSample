#!/bin/bash
mazeArrindex=()
mazeArr=(1 2 3)

bookArr=()
bookArrIndex=()

# 参数是数组,怎么获取数组的长度。。。
# 怎么传递引用
# arrsetByRow(arr,arrindex,i,colArr)
arrsetByRow() {
  echo $1
  local arr=($1)
  # local arrindex=

  local arrLength=${#arr[@]}
  echo $arrLength
  local colArrLength=${#$4[*]}
  local i=0
  $2[$3*2]=$arrLength
  $2[$3*2+1]=$arrLength+$colArrLength
  for value in ${$4[@]}
  do
    $1[$arrLength+i]=$value
    i=$i+1
  done
}

# arrset(arr,arrindex,i,j,value)
# arrset() {
#
#
#
# }
#
# arrget() {
#
# }

echo '输入迷宫,0表示空,1表示有障碍物,以空行结束'
i=0
while [ true ]
do
  read temp
  if [ "$temp" == "" ]
  then
    break
  fi
  arr=(${temp// / })
  echo ${mazeArr[@]}
  arrsetByRow $mazeArr $mazeArrindex $i $arr
  for val in ${mazeArr[@]}
  do
    echo $val
  done

  # for i in ${arr[@]}
  # do
  #   echo $i
  # done
  i=$i+1
done

echo '输入起始点位置:'
read startCoord
echo '输入目标点位置:'
read targetCoord1
