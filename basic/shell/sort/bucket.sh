#!/bin/bash

echo '桶排序'

arr=(23 2 6 7 2 0 36 41 1)

function bucket() {

  # tempArr 是目标数组,resultArr 是经过排序后的数组
  # () 可以将字符串分割成数组
  tempArr=($*)
  resultArr=("${tempArr[@]}")

  # 计数数组
  bucketArr=()

  let max=0
  let min=0
  # 寻找出数组中的最大值和最小值
  for temp in ${tempArr[@]}
  do
    let temp=`expr $temp`
    if [ $temp -le $min ]
    then
      min=$temp
    fi
    if [ $temp -ge $max ]
    then
      max=$temp
    fi
  done

  # 计算出计数数组的长度，并将元素都初始化为0
  delt=`expr $max - $min + 1`
  tempNum=0
  while [ $tempNum -lt $delt ]
  do
    bucketArr[tempNum]=0
    tempNum=`expr $tempNum + 1`
  done

  # 排序部分，计算出各个元素出现的次数
  for temp in ${tempArr[@]}
  do
    tempIndex=`expr $temp - $min`
    bucketArr[tempIndex]=`expr ${bucketArr[$tempIndex]} + 1`
  done
  # echo "bucketArr is ${bucketArr[@]}"

  # ----------------------------------------------------------------------------
  # 以下都是为了输出结果数组

  # bucketArr 的下标
  let temp_0=0
  # resultArr 的下标
  let temp_1=0
  let bucketArrLength=${#bucketArr[@]}
  while [ $temp_0 -le $bucketArrLength ]
  do
    if [[ ${bucketArr[$temp_0]} -gt 0 ]]
    then
      # bucketArr 中某个元素的计数
      let temp2=0
      while [ $temp2 -lt ${bucketArr[$temp_0]} ]
      do
        resultArr[$temp_1]=`expr $temp_0 + $min`
        temp_1=`expr $temp_1 + 1`
        temp2=`expr $temp2 + 1`
      done
    fi
    temp_0=`expr $temp_0 + 1`
  done

  echo ${resultArr[@]}

}

bucket "${arr[@]}"
