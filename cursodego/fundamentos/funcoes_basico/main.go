package main

import (
	"fmt"

	"github.com/cursodego/fundamentos/funcoes_basico/matematica"
)

func main() {
	resultado := matematica.Calculo(matematica.Multiplicador, 2, 2)
	fmt.Printf("O resultado da multiplicacao foi: %d\r\n", resultado)
	resultado = matematica.Soma(3, 3)
	fmt.Printf("O resultado da soma foi: %d\r\n", resultado)
	resultado = matematica.Calculo(matematica.Divisor, 6, 2)
	fmt.Printf(" O resultado da divisao foi: %d\r\n", resultado)
	resultado = matematica.Calculo(matematica.Menos, 7, 4)
	fmt.Printf("O resultado da subtracao é: %d\r\n", resultado)
}
