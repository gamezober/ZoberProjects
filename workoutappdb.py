#This module uses pyodbc to access a SQL Server Database to enter data inputed from workoutappgui

import pyodbc

connection = pyodbc.connect(driver='{SQL Server}', server='ZOBERPAD', database='dbWorkoutApp',               
               trusted_connection='yes')
c = connection.cursor()

#each function below adds data to respective table
def bSquatInsert(data):
    c.execute("INSERT INTO dbo.bSquat VALUES(?,?,?,?)", data)
    c.commit()

def benchInsert(data):
    c.execute("INSERT INTO dbo.bench VALUES(?,?,?,?)", data)
    c.commit()

def dLiftInsert(data):
    c.execute("INSERT INTO dbo.dLift VALUES(?,?,?,?)", data)
    c.commit()

def fSquatInsert(data):
    c.execute("INSERT INTO dbo.fSquat VALUES(?,?,?,?)", data)
    c.commit()

def pressInsert(data):
    c.execute("INSERT INTO dbo.bSquat VALUES(?,?,?,?)", data)
    c.commit()


