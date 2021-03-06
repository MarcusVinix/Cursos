package main

import (
	"encoding/csv"
	"fmt"
	"os"
)

func main() {

	arquivo, err := os.Open("cidades.csv")
	if err != nil {
		fmt.Println("[main] Houve um erro ao abrir o arquivo. Erro: ", err.Error())
		return
	}

	/*scanner := bufio.NewScanner(arquivo)
	for scanner.Scan() {
		linha := scanner.Text()
		fmt.Println("O conteúdo da linha é: ", linha)
	}*/

	leitorCsv := csv.NewReader(arquivo)
	conteudo, err := leitorCsv.ReadAll()
	if err != nil {
		fmt.Println("[main] Houve um erro ao ler o arquivo com leitor CSV. Erro:", err.Error())
	}
	for indiceLinha, linha := range conteudo {
		fmt.Printf("Linha[%d] %s\r\n", indiceLinha, linha)
		for indiceItem, item := range linha {
			fmt.Printf("Item[%d] %s\r\n", indiceItem, item)
		}
	}
	arquivo.Close()
}
