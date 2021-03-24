palavra = "Marcus Vinicius Souza"
print("startswith=retorna verdadeiro se a string inicia com uma substring: ", palavra.startswith("Marcus"))
print("stripe elimina espaços em branco a esquerda e a direita: ", ".", "   Marcus Vinicius      ".strip(), ".")
print("lstripe elimina espaços em branco a esquerda: ", ".", "   Marcus Vinicius      ".lstrip(), ".")
print("rstripe elimina espaços em branco a direita: ", ".", "   Marcus Vinicius      ".rstrip(), ".")
print("zfill preenche a esquerda com zero (0) ", "465".zfill(8))
print("swapcase - inverte caracteres ", "Marcus Vinicius ".swapcase())