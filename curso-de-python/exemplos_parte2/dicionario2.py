dicionarioCursos = {"python":[130, "Básico", "Desktop"],
                    "java":[110, "Intermediario", "Desktop e Web"],
                    "arduino":[90, "Avançado", "Robótica"]}

print("Dados de Java (usando get): ", dicionarioCursos.get("java"))
print("Dados de java (usando setdefault): ", dicionarioCursos.setdefault("java"))

for chave, informacaoes in dicionarioCursos.items():
    print("Curso: ", chave)
    print("Valor: %5.2f" % informacaoes[0])
    print("Nível: ", informacaoes[1])
    print("Observação: ", informacaoes[2])
    print("\n")

copiaDicionarioCursos = dicionarioCursos
#ou fazer assim
copia2DicionarioCursos = dicionarioCursos.copy()

print("copiaDicionarioCursos = ", copiaDicionarioCursos)
print("copia2DicionarioCursos = ", copia2DicionarioCursos)
print(dicionarioCursos)
dicionarioCursos.clear()
print("Depois de clear: ", dicionarioCursos)
