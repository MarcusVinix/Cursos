package operadora

import (
	"strconv"

	"github.com/cursodego/fundamentos/pacotes/prefixo"
)

//NomeOperadora representa o nome da operadora que se estar a usar
var NomeOperadora = "XPTO Telecom"

//PrefixoDaCapitalOperadora operadora e capital
var PrefixoDaCapitalOperadora = strconv.Itoa(prefixo.Capital) + " " + NomeOperadora
