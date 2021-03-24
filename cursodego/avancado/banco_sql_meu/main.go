package main

import (
	"fmt"
	"net/http"

	"github.com/cursodego/avancado/banco_sql_meu/manipulador"
	"github.com/cursodego/avancado/banco_sql_meu/repo"
)

func init() {
	fmt.Println("Vamos começar a subir o servidor...")
}

func main() {

	err := repo.AbreConexaoComBancoDeDadosSQL()
	if err != nil {
		fmt.Println("Parando a carga do servidor. Erro ao abrir o bando de dados: ", err.Error())
		return
	}

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintln(w, "Olá Mundo!")
	})
	fmt.Println("Estou escutando comandante...")

	http.HandleFunc("/funcao", manipulador.Funcao)
	http.HandleFunc("/ola", manipulador.Ola)
	http.HandleFunc("/compras/", manipulador.Compradores)
	http.ListenAndServe(":8181", nil)

}
