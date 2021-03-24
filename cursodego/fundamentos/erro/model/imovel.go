package model

import "errors"

//Imovel representa informaçãos de um imóvel
type Imovel struct {
	X     int    `json:"coordenada_x"`
	Y     int    `json:"coordenada_y"`
	Nome  string `json:"nome"`
	valor int
}

//ErrValorDeImovelMuitoBaixo é um erro que é apresentado quando é atribuido a imóvel um valor muito baixo
var ErrValorDeImovelMuitoBaixo = errors.New("O valor informado é muit baixo")

//ErrValorDeImovelMuitoAlto é um erro que é apresentao quando é atribuido ao imóvel um valor muito alto fora do mercado
var ErrValorDeImovelMuitoAlto = errors.New("O valor informado é muito alto")

//SetValor define o valor do imóvel
func (i *Imovel) SetValor(valor int) (err error) {
	err = nil
	if valor < 50000 {
		err = ErrValorDeImovelMuitoBaixo
		return
	} else if valor > 10000000 {
		err = ErrValorDeImovelMuitoAlto
		return
	}
	i.valor = valor
	return
}

//GetValor retorna o valor do imóvel
func (i *Imovel) GetValor() int {
	return i.valor
}

//GetName retorna o nome do imovel
func (i *Imovel) GetName() string {
	return i.Nome
}
