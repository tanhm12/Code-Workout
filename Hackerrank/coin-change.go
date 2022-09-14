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
 * Complete the 'getWays' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. LONG_INTEGER_ARRAY c
 */

func getWays(n int32, c_arr []int64) int64 {
	c := c_arr[:]

	res := make([]int64, n+1)
	res[0] = 1

	for i := 0; i < len(c); i++ {
		for j := c[i]; j <= int64(n); j++ {
			res[j] += res[j-c[i]]
		}
	}

	return int64(res[n])
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	firstMultipleInput := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	nTemp, err := strconv.ParseInt(firstMultipleInput[0], 10, 64)
	checkError(err)
	n := int32(nTemp)

	mTemp, err := strconv.ParseInt(firstMultipleInput[1], 10, 64)
	checkError(err)
	m := int32(mTemp)

	cTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	var c []int64

	for i := 0; i < int(m); i++ {
		cItem, err := strconv.ParseInt(cTemp[i], 10, 64)
		checkError(err)
		c = append(c, cItem)
	}

	// Print the number of ways of making change for 'n' units using coins having the values given by 'c'

	ways := getWays(n, c)

	fmt.Fprintf(writer, "%d\n", ways)

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
