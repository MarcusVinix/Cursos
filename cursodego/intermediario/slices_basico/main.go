package main

import (
	"fmt"
)

func main() {
	var nums []int
	fmt.Println(nums, len(nums), cap(nums))
	nums = make([]int, 5)
	fmt.Println(nums, len(nums), cap(nums))
	capitais := []string{"Lisboa"}
	fmt.Println(capitais, len(capitais), cap(capitais))
	capitais = append(capitais, "Brasilia")
	fmt.Println(capitais, len(capitais), cap(capitais))
	cidades := make([]string, 4)
	cidades[0] = "Nova York"
	cidades[1] = "Londres"
	cidades[2] = "Tokio"
	cidades[3] = "Singapura"
	fmt.Println(cidades, len(cidades), cap(cidades))
	capitais[1] = "brasília"
	fmt.Println(capitais, len(capitais), cap(capitais))
	for indicie, cidade := range cidades {
		fmt.Printf("Cidades[%d] = %s\n\r", indicie, cidade)
	}
}
