package main

import (
	"math/rand"
	"golang.org/x/tour/pic"
)

func Pic(dx, dy int) [][]uint8 {
	dx_array := make([][]uint8, 0, dx)

	for i := 0; i < cap(dx_array); i++ {
		dy_array := make([]uint8, 0, dy)

		for y := 0; y < cap(dy_array); y++ {
			dy_array = append(dy_array, uint8(rand.Intn(255)))
		}

		dx_array = append(dx_array, dy_array)
	}

	return dx_array
}

func main() {
	pic.Show(Pic)
}
