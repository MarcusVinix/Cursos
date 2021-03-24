pagina1 = open("pagina1.html", "w", encoding = "utf-8")
pagina1.write("""
<!DOCTYPE HTML>
<HTML lang="pt-br">
<HEAD>
<title>Professor Neri - html5</title>
</HEAD>
<BODY>
<h1>Videoaulas neri<h1><br>""")

for tabuada in range(1, 10):
    pagina1.write("9 * %d = %d <br>\n" % (tabuada, (9 * tabuada)))

pagina1.write("""
Prof Neri Aldoir Neitzke
</body>
</HTML>""")
pagina1.flush()
pagina1.close()
