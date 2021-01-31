#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:06:00 2020

@author: devinpowers
"""
"""
Creating a Database in SQlite 
"""


import sqlite3

# .connect("name_of_data_base_to_Create.db")

conn = sqlite3.connect('citi.db')

## Cursor enables traversal over the records in our database Cursor Objects
cur = conn.cursor()

# We create a table in our DataBase and label each of the headers
## For each column in our CSV File
sql = """
    CREATE TABLE CitiBikes (
        Trip_Duration INTEGER,
        StartTime TEXT,
        StopTime TEXT,
        StartStationID INTEGER,
        StartStationName TEXT,
        StartStationLat DECIMAL,
        StartStationLong DECIMAL,
        EndStationID INTEGER,
        EndStationName TEXT,
        EndStationLat DECIMAL,
        EndStationlog DECIMAL,
        BikeId INTEGAR,
        Usertype TEXT,
        Birthyear TEXT,
        Gender INTEGER
        
        )
    """
#execute our SQL statement
cur.execute(sql)
print('Database has been created')

# Commits Current transaction
conn.commit()
#Closes the connection to the DataBase
conn.close()
    
