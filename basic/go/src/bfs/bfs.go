package main
import (
  "fmt"
  "bufio"
  "os"
  "strings"
  "strconv"
)

// 走下一步的坐标
var nextStep=[4][]int{{-1,0},{0,1},{1,0},{0,-1}}
// 最小步数
var minStep=0
var que [][]int
var head=0
var tail=0

func main(){
  var mazeArr [][]string
  var bookArr [][]int
  var startCoord []int
  var targetCoord []int
  fmt.Println("输入迷宫,0表示正常,1表示障碍物")
  reader:=bufio.NewReader(os.Stdin)
  for true {
    data,_,_:=reader.ReadLine()
    temp:=string(data)
    if temp == "" {
      break
    } else {
      mazeArr=append(mazeArr,strings.Split(temp," "))
    }
  }
  // fmt.Println(mazeArr)
  fmt.Println("输入起始点坐标:")
  data2,_,_:=reader.ReadLine()
  temp2:=string(data2)
  tempStrArr:=strings.Split(temp2," ")
  for i:=0;i< len(tempStrArr);i++ {
    tempInt,_:=strconv.Atoi(tempStrArr[i])
    startCoord=append(startCoord,tempInt)
  }
  fmt.Println("输入目标点坐标:")
  data3,_,_:=reader.ReadLine()
  temp3:=string(data3)
  tempStrArr=strings.Split(temp3," ")
  for i:=0;i< len(tempStrArr);i++ {
    tempInt,_:=strconv.Atoi(tempStrArr[i])
    targetCoord=append(targetCoord,tempInt)
  }
  // fmt.Println(startCoord)
  // fmt.Println(targetCoord)

  i:=0
  for i < len(mazeArr) {
    var tempArr []int
    j:=0
    for j < len(mazeArr[0]) {
      tempArr=append(tempArr,0)
      j++
    }
    bookArr=append(bookArr,tempArr)
    i++
  }
  // fmt.Println(bookArr)

  que=append(que,[]int{startCoord[0],startCoord[1],0})
  tail++

  bfs(mazeArr,bookArr,startCoord,targetCoord)
}

func bfs(mazeArr [][]string,bookArr [][]int,startCoord []int ,targetCoord []int) {
  currentStep:=0
  currentCoord:=[2]int{startCoord[0],startCoord[1]}
  flag:=false
  for head<tail {
    for i:=0;i<4;i++ {
        currentCoord[0]=nextStep[i][0]+que[head][0]
        currentCoord[1]=nextStep[i][1]+que[head][1]

        if currentCoord[0]<0 || currentCoord[0]> len(mazeArr)-1 || currentCoord[1]<0 || currentCoord[1]> len(mazeArr[0])-1 {
          continue
        } else {
          if mazeArr[currentCoord[0]][currentCoord[1]] == "0" && bookArr[currentCoord[0]][currentCoord[1]] == 0 {
            // 不是障碍物，并且没有走过
            bookArr[currentCoord[0]][currentCoord[1]]=1
            currentStep+=1
            que=append(que,[]int{currentCoord[0],currentCoord[1],que[head][2]+1})
            tail+=1
          }
          if currentCoord[0]==targetCoord[0] && currentCoord[1]==targetCoord[1] {
            flag=true
            break
          }
        }
    }
    if flag {
      break
    }
    head++
  }

  fmt.Println("最少的步数为:")
  fmt.Println(que[len(que)-1][2])
  fmt.Println(que)
}
