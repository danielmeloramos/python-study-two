from long_name_exception import LongNameException

#1- lancamento de excecoes
x = -1

if x < 0:
    raise Exception("O número é menor que 0")

#2 Criando excecoes
long_name = "Está é uma string muito longa para um nome de alguém"

if len(long_name) > 50:
    raise LongNameException("O nome é muito longo")