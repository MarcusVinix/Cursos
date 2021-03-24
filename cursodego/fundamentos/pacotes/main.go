package main

import (
	"fmt"

	"github.com/cursodego/fundamentos/pacotes/operadora"
	"github.com/cursodego/fundamentos/pacotes/prefixo"
)

//NomeDoUsuario é o nome do usuário do sistema
var NomeDoUsuario = "Marcus"

func main() {
	fmt.Printf("Nome do usuario: %s\r\n", NomeDoUsuario)
	fmt.Printf("Prefixo da Capital: %d\r\n", prefixo.Capital)
	fmt.Printf("Nome da Operadora: %s\r\n", operadora.NomeOperadora)
	fmt.Printf("O valor de teste é: %s\r\n", prefixo.TesteComPrefixo)
}
