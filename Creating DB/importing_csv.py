#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:48:37 2020

@author: devinpowers
"""


import sqlite3, csv, pandas

connection  = sqlite3.connect('citi.db')
cursor = connection.cursor()

with open('citibike.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO CitiBikes VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row.split(","))
        
        connection.commit()
        no_records +=1
        
connection.close()
print('\n{} Records Transferred'.format(no_records))

pandas.read_sql_query('SELECT count * FROM CitiBikes ')