try:
    print(6/2)
    print(1/0)
except ZeroDivisionError:
    print("Atenção, o numero não pode ser dividido por zero(0)")

try:
    arquivo = open("cursos.txt")
    try:
        print(arquivo.readline())
        print(arquivo.readline())
    finally:
        print("FINAL")
        arquivo.close()
except FileNotFoundError:
    print("Atenção, esse arquivo não existe")
