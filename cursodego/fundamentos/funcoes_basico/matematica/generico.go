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

//Divisor divide o x pelo y
func Divisor(x int, y int) int {
	return x / y
}

//Menos subtrai o x pelo y
func Menos(x int, y int) int {
	return x - y
}
