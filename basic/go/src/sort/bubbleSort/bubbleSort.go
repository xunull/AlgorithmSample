package main

// 改进的地方，记录最后一次交换的位置

import (
	"fmt"
	"shuffle"
)

var origin = []int{12, 64, 35, 74, 37, 49, 40, 18, 83}

func bubbleSort(origin []int) []int {
	length := len(origin)

	for i := 0; i < length; i++ {
		for j := 0; j < length-1; j++ {
			if origin[j] > origin[j+1] {
				temp := origin[j]
				origin[j] = origin[j+1]
				origin[j+1] = temp
			}
		}
	}
	return origin
}

func main() {
	// arr := utils.GetArray(make([]int, 50))
	arr := shuffle.Shuffle1(54)
	fmt.Println("原始数组为")
	fmt.Println(arr)
	result := bubbleSort(arr)
	fmt.Println("排序后为:")
	fmt.Println(result)
}
