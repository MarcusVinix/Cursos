package main

import (
	"fmt"
	"net/http"

	"github.com/cursodego/avancado/servidor_web/manipulador"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintln(w, "Olá Mundo!")
	})
	fmt.Println("Estou escutando comandante...")

	http.HandleFunc("/funcao", manipulador.Funcao)
	http.HandleFunc("/ola", manipulador.Ola)
	http.ListenAndServe(":8181", nil)

}
