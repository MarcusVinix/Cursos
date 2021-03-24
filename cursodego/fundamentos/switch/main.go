package main

import (
	"fmt"
	"runtime"
	"time"
)

func main() {

	numero := 3
	fmt.Print("O numero ", numero, " se escreve assim : ")
	switch numero {
	case 1:
		fmt.Println("Um.")
	case 2:
		fmt.Println("Dois.")
	case 3:
		fmt.Println("Três.")
	}

	fmt.Println("Você é da família do Unix?")
	switch runtime.GOOS {
	case "darwin":
		fallthrough
	case "freebsd":
		fallthrough
	case "Linux":
		fmt.Println("Sim!!")
	default:
		fmt.Println("Deixa essa pergunta para lá...")
	}
	switch time.Now().Weekday() {
	case time.Saturday, time.Sunday:
		fmt.Println("Ok, você pode dormir até mais tarde.")
	default:
		fmt.Println("Vamos lá que é dia de trabalho")

	}

	numero = 10
	fmt.Println("Este numero cabe num dígito?")
	switch {
	case numero < 10:
		fmt.Println("SIM")
	case numero >= 10 && numero < 100:
		fmt.Println("Serve dois dígitos...")
	case numero > 100:
		fmt.Println("Não dá o numero é muito grande")

	}

}
