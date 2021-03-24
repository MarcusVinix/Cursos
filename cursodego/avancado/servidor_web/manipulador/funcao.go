package manipulador

import (
	"fmt"
	"net/http"
)

//Funcao è manipulador de requisicao HTTP na rota/funcao
func Funcao(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Aqui é um manipulador usando uma função num pacote")
}
