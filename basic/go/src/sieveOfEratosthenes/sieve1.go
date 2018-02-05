package main

import (
	"fmt"
	"math"
)

const limit = 120

func Sieve1() []int {
	var result []int

	max := int(math.Ceil(math.Sqrt(limit)))

	origin := make([]int, limit, limit)

	for i := 0; i < limit; i++ {
		origin[i] = i + 1
	}

	origin = origin[1:]
	temp := make([]int, 0, len(origin))
	for i := 2; i < max; {
		i = origin[0]
		result = append(result, i)
		temp = make([]int, 0, len(origin))
		for _, num := range origin {
			if num%i != 0 {
				temp = append(temp, num)
			}
		}
		origin = temp[:]

	}

	for _, num := range temp {
		result = append(result, num)
	}

	return result
}

func main() {

	fmt.Println(Sieve1())
}
