#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:22:51 2020

@author: devinpowers
"""
import pandas, sqlite3, seaborn

db = sqlite3.connect('citi.db')

print(pandas.read_sql_query('select count(*) from CitiBikes', db))