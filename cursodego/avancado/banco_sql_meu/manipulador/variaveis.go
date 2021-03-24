package manipulador

import "html/template"

//ModeloOla armazena o modelo de pagina ola
var ModeloOla = template.Must(template.ParseFiles("html/ola.html"))

//ModeloComprador armazena o modelo de pagina compras
var ModeloComprador = template.Must(template.ParseFiles("html/comprador.html"))
