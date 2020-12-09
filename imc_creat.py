# -*- coding: utf-8 -*-
import sqlite3

# criando uma conexão e um cursor

con = sqlite3.connect('Calculos_imc')
cursor = con.cursor()

# cria uma tabela

def create_table():
      'create table Calculos\
      (IMC floate'\

create_table()


peso = float(input('Qual o seu peso atual?'))
autura = float(input('Qual a sua autura?'))

imc = peso / (autura ** 2)

# criando uma conexão e um cursor
con = sqlite3.connect('Calculos_imc')
cursor = con.cursor()

# sentença SQL para inserir registro
sql = 'insert into Calculos_imc values ()'

# dados

recset = [(imc)]

# Insere os registros
for rec in recset:
    cursor.execute(sql, rec)

# Confirma a transação
con.commit()



