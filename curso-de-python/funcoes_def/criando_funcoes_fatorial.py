#fatorial de 3: 3 * 2 * 1 = 6
#fatorial de 4: 4 * 3 * 2 * 1 = 24
#fatorial de 5: 5 * 4 * 3 * 2 * 1 = 120

def fatorial(numero):
    f = 1
    while numero > 1:
        f *= numero
        numero -= 1
    return f

print(fatorial(3))
print(fatorial(4))
print(fatorial(5))
print(fatorial(6))

def fatorial1(numero):
    f = 1
    i = 1
    while i <= numero:
        f *= i
        i += 1
    return f

print(fatorial1(3))
print(fatorial1(4))
print(fatorial1(5))
print(fatorial1(6))
    