import types
def mostraTipo(dado):
    tipo = type(dado)
    if tipo == str:
        return ("String")
    elif tipo == int:
        return ("inteiro")
    elif tipo == list:
        return ("Lista")
    elif tipo == dict:
        return ("Dicionario")
    elif tipo == float:
        return ("Numero decimal")
    elif tipo == bool:
        return ("Booleano")
    elif tipo == types.BuiltinFunctionType:
        return ("Função interna")
    elif tipo == types.FunctionType:
        return ("Função")
    else:
        return (str(tipo))

print(mostraTipo("Marcus"))
print(mostraTipo(28))
print(mostraTipo(78.8))
print(mostraTipo([5,7,8]))
print(mostraTipo({"Python":120, "Go":130}))
print(mostraTipo(print))
print(mostraTipo(None))