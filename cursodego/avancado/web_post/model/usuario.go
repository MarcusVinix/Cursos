package model

//Usuario é o nome do usuario do sistema
type Usuario struct {
	ID   int    `json:"id"`
	Nome string `json:"nome"`
}
