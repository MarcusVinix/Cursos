package matematica

/*
Calculo executa qualquer tipo de calculo basta enviar a funcao desejada
*/
func Calculo(funcao func(int, int) int, numeroA int, numeroB int) int {
	return funcao(numeroA, numeroB)
}

//Multiplicador multiplica x vezes o y
func Multiplicador(x int, y int) int {
	return x * y
}

//Divisor efetua a divisao do numeroA pelo numeroB
func Divisor(numeroA int, numeroB int) (resultado int) {
	resultado = numeroA / numeroB
	return
}

//Menos subtrai o x pelo y
func Menos(x int, y int) int {
	return x - y
}

//DivisorComResto efetua a divisao do numeroA pelo numeroB
//retorno o resultado e tambem o resto da divisao
func DivisorComResto(numeroA int, numeroB int) (resultado int, resto int) {
	resultado = numeroA / numeroB
	resto = numeroA % numeroB
	return
}
