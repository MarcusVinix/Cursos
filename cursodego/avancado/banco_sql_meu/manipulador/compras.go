package manipulador

import (
	"fmt"
	"net/http"
	"strconv"

	"github.com/cursodego/avancado/banco_sql_meu/model"
	"github.com/cursodego/avancado/banco_sql_meu/repo"
)

//Compradores é o manipulador da requisição de rota /compras/
func Compradores(w http.ResponseWriter, r *http.Request) {
	compras := model.Compradores{}
	codigoID, err := strconv.Atoi(r.URL.Path[9:])
	if err != nil {
		http.Error(w, "Não foi enviado um numero válido. Verifique.", http.StatusBadRequest)
		fmt.Println("[compras] Erro ao converter o numero enviado: ", err.Error())
		return
	}
	sql := "select id, nome, endereco, telefone from compradores where id = ?"
	linha, err := repo.Db.Queryx(sql, codigoID)
	if err != nil {
		http.Error(w, "Não foi possível pesquisar esse numero.", http.StatusInternalServerError)
		fmt.Println("[compras] nao foi possivel executar a query: ", sql, " Erro: ", err.Error())
		return
	}
	for linha.Next() {
		err = linha.StructScan(&compras)
		if err != nil {
			http.Error(w, "Não foi possível pesquisar esse numero.", http.StatusInternalServerError)
			fmt.Println("[compras] nao foi possivel fazer o binding dos dados do banco na struct: ", err.Error())
			return
		}
	}

	if err := ModeloComprador.ExecuteTemplate(w, "comprador.html", compras); err != nil {
		http.Error(w, "Houve um erro na rendereização da página.", http.StatusInternalServerError)
		fmt.Println("[compras] Erro na execucao do modelo:", err.Error())
	}

}
