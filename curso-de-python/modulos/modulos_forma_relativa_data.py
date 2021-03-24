from datetime import date

mesPorExtenso = ["Janeiro", "Feveiro", "Março", "Abril","Maio","Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
diaDaSemana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
hoje = date.today()
dia = hoje.day
mes = hoje.month
ano = hoje.year
rodape = "Carazinho, %s, %d de %s de %d" % (diaDaSemana[hoje.weekday()], dia, mesPorExtenso[mes-1], ano)
print(hoje)
print("mes: ", mes)
print("Dia: ", dia)
print("Ano: ", ano)
print(rodape)
print("Daqui a 40 será: ", date.fromordinal(hoje.toordinal() + 40))
print("Dia da semana: ", hoje.weekday())
