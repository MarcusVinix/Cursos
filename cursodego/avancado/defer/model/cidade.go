package model

//Cidade é a cidade e o estado do brasil
type Cidade struct {
	Nome   string `json:"nome"`
	Estado string `json:"estado"`
}
