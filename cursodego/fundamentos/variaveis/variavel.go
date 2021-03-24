package main

import "fmt"

var (
	//Endereco é um valor importante e tem de ser publico
	Endereco string //endereco =""
	//Telefone é um valor importante para nossa aula
	Telefone            string
	quantidade, estoque int     //quantidade = 0
	comprou             bool    //comprou = false
	valor               float64 //valor = 0.00
	palavras            rune
)

func main() {
	teste := "Valor de teste"
	Telefone = "(11)94241-8283"
	fmt.Printf("endereco: %s\r\n", Endereco)
	fmt.Printf("quantidade: %d\r\n", quantidade)
	fmt.Printf("comprou: %v\r\n", comprou)
	fmt.Printf("palavras: %v\r\n", palavras)
	fmt.Printf("O valor de teste é: %v\r\n", teste)
	fmt.Printf("O telefone é: %s\r\n", Telefone)
}
