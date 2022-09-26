package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

/*
 * Complete the 'strangeCounter' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts LONG_INTEGER t as parameter.
 */

func calMark(i int64) int64 {
	return 3*(i-1) + 1
}

func strangeCounter(t int64) int64 {
	var prev_pow int64 = 1
	var time_prev int64 = calMark(prev_pow)

	var new_pow, new_time int64

	for i := 1; i < 42; i++ {
		new_pow = prev_pow * 2
		new_time = calMark(new_pow)

		if time_prev <= t && t < new_time {
			return 3*prev_pow - (t - time_prev)
		}
		prev_pow = new_pow
		time_prev = new_time
	}

	return 0
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create("tmp_out.txt")
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	t, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)

	result := strangeCounter(t)

	fmt.Fprintf(writer, "%d\n", result)

	writer.Flush()
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
