#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:48:37 2020

@author: devinpowers
"""


import sqlite3, csv, pandas

#Connect to the DataBase
connection  = sqlite3.connect('citi.db')
cursor = connection.cursor()

#Open the CSV file were working with
with open('citibike.csv', 'r') as file:
    no_records = 0
    next(file) ## skip header row
    for row in file:
        
        cursor.execute("INSERT INTO CitiBikes VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row.split(","))
        
        connection.commit()
        
        no_records +=1
        
connection.close()

print('\n{} Records Transferred'.format(no_records))
