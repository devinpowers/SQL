#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:06:00 2020

@author: devinpowers
"""


import sqlite3, csv

conn = sqlite3.connect('citi.db')
cur = conn.cursor()


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
        t INTEGAR,
        Usertype TEXT,
        Birthyear TEXT,
        Gender INTEGER
        
        )
    """
    
cur.execute(sql)
print('Database has been created')

conn.commit()
conn.close()
    