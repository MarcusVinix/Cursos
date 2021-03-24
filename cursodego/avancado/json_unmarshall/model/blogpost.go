package model

//BlogPost armazena dados de um post
type BlogPost struct {
	UsuarioID int    `json:"userId"`
	ID        int    `json:"id"`
	Titulo    string `json:"title"`
	Texto     bool   `json:"completed"`
}
