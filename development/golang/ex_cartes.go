package main

import (
	"strings"

	"golang.org/x/tour/wc"
)

func WordCount(s string) map[string]int {
	wordsCountMap := make(map[string]int)
	words := strings.Fields(s)

	for _, v := range words {
		_, ok := wordsCountMap[v]
		if ok {
			wordsCountMap[v] = wordsCountMap[v] + 1
		} else {
			wordsCountMap[v] = 1
		}
	}

	return wordsCountMap
}

func main() {
	wc.Test(WordCount)
}
