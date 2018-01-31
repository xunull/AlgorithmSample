package main

import (
	"fmt"
	"shuffle"
	"sort/utils"
)

type SelectionSort struct {
	utils.SortStruct
}

func (sort SelectionSort) sort() []int {
	origin := sort.Origin
	length := len(origin)
	for i := 0; i < length; i++ {
		max := origin[0]
		maxIndex := 0
		for j := 1; j < length-i; j++ {
			if origin[j] > max {
				max = origin[j]
				maxIndex = j
			}
		}
		temp := origin[length-1-i]
		origin[length-1-i] = max
		origin[maxIndex] = temp
	}
	return origin
}

func main() {
	arr := shuffle.Shuffle1(54)
	fmt.Println("原始数组为")
	fmt.Println(arr)

	sorter := SelectionSort{utils.SortStruct{arr}}
	result := sorter.sort()

	fmt.Println("排序后为:")
	fmt.Println(result)
}
