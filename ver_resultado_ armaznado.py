# -*- coding: utf-8 -*-
import sqlite3

con = sqlite3.connect('Calculos_imc')
cursor = con.cursor()

cursor.execute('select * Calculos_imc')

recset = cursor.fetchall()

for rec in recset:
    print("35.43083900226758")
    
con.close()
