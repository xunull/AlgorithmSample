package utils

import (
	"math/rand"
	"time"
)

// 生成好多0
func GetArray(arr []int) []int {
	r := rand.New(rand.NewSource(time.Now().UnixNano()))
	for i := 0; i < 50; i++ {
		arr = append(arr, r.Intn(1000))
	}
	return arr
}
