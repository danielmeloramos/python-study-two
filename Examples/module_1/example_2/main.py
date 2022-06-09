from long_name_exception import LongNameException

#1- Criando excecoes
long_name = "Está é uma string muito longa para um nome de alguém"

if len(long_name) > 50:
    raise LongNameException("O nome é muito longo")