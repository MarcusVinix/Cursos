numeros = [30, 28, 43, 54, -1, -4, -6, -7, 8, 7, 9,]
print(numeros)
i = 0
for num in numeros:
    print("FOR sem enumerate: [%d] --> %d" % (i, num))
    #print("FOR sem enumerate: [", i, "] --> ", num)
    i += 1

i = 0
while i < len(numeros):
    print("While sem enumerate: [%d] --> [%d]" % (i, numeros[i]))
    i += 1

for i, num in enumerate(numeros):
    print("FOR com enumerate: [%d] --> %d" % (i, num))
