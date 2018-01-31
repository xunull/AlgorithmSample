package utils

type SortStruct struct {
	// 属性如果小写不能跨包使用
	Origin []int
}

func (sort SortStruct) sort() (result []int) {
	return result
}

func (sort SortStruct) Length() int {
	return len(sort.Origin)
}

type Sort interface {
	sort()
}
