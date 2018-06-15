var a []int
// append works on nil slices.
a = append(a, 0)

// the slice grows as needed.
a = append(a, 1)

// we can add more than one element at a time.
a = append(a, 2, 3, 4)

// Work with tranche
var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}
for i, v := range pow {
  fmt.Printf("2**%d = %d\n", i, v)
}

// Gamme poursuivi
pow := make([]int, 10)
for i := range pow {
	pow[i] = 1 << uint(i)
}
for _, value := range pow {
	fmt.Printf("%d\n", value)
}
