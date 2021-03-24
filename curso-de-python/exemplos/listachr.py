i = 1
while i < 255:
    print(i, "-->", chr(i))
    i += 1

codigoAscii = []
i = 1
while i < 255:
    codigoAscii += (i, "-->", chr(i))
    i += 1
print(codigoAscii)
