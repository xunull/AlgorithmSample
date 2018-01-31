package main

import (
	"fmt"
	"shuffle"
	"sort/utils"
)

type InsertionSort struct {
	utils.SortStruct
}

func (sort InsertionSort) sort() []int {
	origin := sort.Origin
	length := sort.Length()

	for i := 0; i < length-1; i++ {
		for j := i + 1; j > 0; j-- {
			if origin[j] < origin[j-1] {
				temp := origin[j-1]
				origin[j-1] = origin[j]
				origin[j] = temp
			} else {
				// 插入排序是用一个元素跟一个已经排序好的数组做比较
				// 因此一旦有个地方满足排序规则,就可以跳过了
				break
			}
		}
	}

	return origin
}

func main() {
	arr := shuffle.Shuffle1(54)
	fmt.Println("原始数组为")
	fmt.Println(arr)

	sorter := InsertionSort{utils.SortStruct{arr}}
	result := sorter.sort()

	fmt.Println("排序后为:")
	fmt.Println(result)
}
