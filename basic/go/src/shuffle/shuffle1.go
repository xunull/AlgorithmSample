package shuffle

import (
	"math/rand"
	"time"
)

func getCards(length int) []int {
	cards := make([]int, length)
	for i := 1; i < length+1; i++ {
		cards[i-1] = i
	}
	return cards
}

func Shuffle1(length int) []int {
	cards := getCards(length)
	result := make([]int, length)
	for i := 0; i < 54; i++ {
		r := rand.New(rand.NewSource(time.Now().UnixNano()))
		number := r.Intn(54)
		for {
			if result[number] == 0 {
				result[number] = cards[i]
				break
			} else {
				number += 1
				if number == 54 {
					number = 0
				}
			}
		}
	}
	return result
}
