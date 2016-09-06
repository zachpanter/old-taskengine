#!/usr/bin/python
from __future__ import division

#IMPORT THE MYSQL MODULES
import mysql.connector
from mysql.connector import errorcode

#IMPORT THE RegEx MODULE
import re

#IMPORT DATETIME
from datetime import date, timedelta



# CREATE A DATABASE CONNECTION
config = {
    'user': 'zpanter',
    'password': 'qmszach!',
    'host': 'qmsdbprod',
    'database': 'complaints',
    'raise_on_warnings': True,
}
cnx = mysql.connector.connect(**config)

# CREATE A DATABASE CURSOR
cursor = cnx.cursor()