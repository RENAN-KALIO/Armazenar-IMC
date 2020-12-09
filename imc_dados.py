# -*- coding: utf-8 -*-
import sqlite3

peso = float(input('Qual o seu peso atual?'))
autura = float(input('Qual a sua autura?'))

imc = peso / (autura ** 2)
print(imc)

# criando uma conexão e um cursor
con = sqlite3.connect('Calculos_imc')
cursor = con.cursor()

# sentença SQL para inserir registro
sql = 'insert into Calculos_imc values (imc)'

# dados

recset = [imc]


# Confirma a transação
con.commit()

# Fechar a conexão
con.close()