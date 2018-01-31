// 不写包会报错
package main

import "fmt"
// 数组是{}
var arr = []int{23,2,6,7,2,0,36,41,1}

func main() {
    fmt.Println(arr)
    fmt.Println("排序后的数组为:")
    fmt.Println(bucketSort(arr))
}

func bucketSort(originArr []int) []int {
  originArrLength:=len(originArr)
  // 复制一个数组，该数组作为排序后的结果使用
  resultArr:=originArr[:]
  max:=0
  min:=0
  // 获取数组中的最大值和最小值，判断出最大值和最小值的差值
  for i:=0;i<originArrLength;i++ {
    if max<originArr[i] {
      max=originArr[i]
    }
    if min>originArr[i] {
      min=originArr[i]
    }
  }
  delta:=max-min+1

  // tempArr 保存目标数组的计数结果
  var tempArr =[]int{}
  for i:=0;i<delta;i++ {
    tempArr=append(tempArr,0)
  }
  // 计数
  for i:=0;i<originArrLength;i++ {
    tempArr[originArr[i]-min]=tempArr[originArr[i]-min]+1
  }

  // 得出排序后的数组
  resultIndex:=0
  tempArrLength:=len(tempArr)
  for i:=0;i<tempArrLength;i++ {
    if tempArr[i]>0 {
      for j:=0;j<tempArr[i];j++ {
        resultArr[resultIndex]=i+min
        resultIndex+=1
      }
    }
  }

  return resultArr;
}
