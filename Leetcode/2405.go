package main

func partitionString(s string) int {
	res := 0
	bit_mark := 0
	for _, runeValue := range s {
		pos := 1 << (int(runeValue) - 97)
		// fmt.Println(pos, runeValue)
		if bit_mark&pos != 0 {
			res += 1
			bit_mark = 0
		}
		bit_mark |= pos
	}
	if bit_mark > 0 {
		res += 1
	}
	return res
}

func main() {
	s := "abababa"
	partitionString(s)
}
