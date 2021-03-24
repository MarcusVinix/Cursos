#coding: utf-8
from datetime import date

mesPorExtenso = ["Janeiro", "Feveiro", "Março", "Abril","Maio","Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
diaDaSemana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
hoje = date.today()
dia = hoje.day
mes = hoje.month
ano = hoje.year
rodape = " %s, %d de %s de %d" % (diaDaSemana[hoje.weekday()], dia, mesPorExtenso[mes-1], ano)
def retornaData():
    return rodape