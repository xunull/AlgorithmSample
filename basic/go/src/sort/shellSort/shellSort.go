package main

import (
	"fmt"
	"shuffle"
	"sort/utils"
)

type ShellSort struct {
	utils.SortStruct
}

func (sorter ShellSort) sort() []int {
	origin := sorter.Origin
	length := sorter.Length()

	// 分组
	for gap := length / 2; gap > 0; gap /= 2 {
		// 这个部分的代码本质是插入排序
		// i+=gap 是各个子数组
		for i := 0; i < length-gap; i += gap {
			// 在子数组中判断
			for j := i + gap; j > 0; j -= gap {
				if origin[j] < origin[j-gap] {
					temp := origin[j-gap]
					origin[j-gap] = origin[j]
					origin[j] = temp
				} else {
					// 插入排序是用一个元素跟一个已经排序好的数组做比较
					// 因此一旦有个地方满足排序规则,就可以跳过了
					break
				}
			}
		}
	}
	return origin
}

func main() {
	arr := shuffle.Shuffle1(54)
	fmt.Println("原始数组为")
	fmt.Println(arr)

	sorter := ShellSort{utils.SortStruct{arr}}
	result := sorter.sort()

	fmt.Println("排序后为:")
	fmt.Println(result)
}
