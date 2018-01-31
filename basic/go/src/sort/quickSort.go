package main

import "fmt"

var arr = []int{1,2,3,4,5,6,7,8,9,10}

func main() {
	fmt.Println(arr)
	fmt.Println("排序后的数组为")
	fmt.Println(quickSort(arr, 0, len(arr)));
}

func quickSort(arr []int, start int, end int) []int {
	if(end <= start) {
		return arr
	}
	targetIndex := start
	targetValue := arr[targetIndex]
	prefix := targetIndex
	suffix := end

	for prefix < suffix {
		var suffixFlag, prefixFlag bool = true, true
		for i := suffix -1; i > prefix; i-- {
			if (suffixFlag && arr[i] > targetValue ) {
				arr[prefix] = arr[i]
				suffix = i
				targetIndex = i
				fmt.Println("suffix")
				fmt.Println(suffix)
				fmt.Println(suffixFlag)
				suffixFlag = false
			}	
		}
		for i := prefix; i < suffix; i++ {
			if (prefixFlag && arr[i] < targetValue ) {
				arr[suffix] = arr[i]
				prefix = i
				targetIndex = i
				fmt.Println("prefix")
				fmt.Println(prefix)
				fmt.Println(prefixFlag)
				prefixFlag = false
			}
		}
	}
	arr[targetIndex] = targetValue
	// fmt.Println("接着排序 ", start, " ", prefix)
	// quickSort(arr, start, prefix);
	// fmt.Println("接着排序 ", suffix, " ", end)
	// quickSort(arr, suffix, end);
	return arr
}
