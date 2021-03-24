package model

//Compradores armazena os dados dos compradores da tabela
type Compradores struct {
	ID       int    `json:"INT" db:"id"`
	Nome     string `json:"nome" db:"nome"`
	Endereco string `json:"cod_telefone" db:"endereco"`
	Telefone string `json:"Telefone" db:"telefone"`
}
