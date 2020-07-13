# import the modules
from pymysql import*
import xlwt
import pandas.io.sql as sql
import os
# connect the mysql with the python
def run(f):
    con=connect(user="be",password="blueeyes",host="localhost",database="mysqldb1",autocommit=True)

    # read the data
    df=sql.read_sql('select * from '+str(f),con)
    # print the data
    #print(df)

    # export the data into the excel sheet
    df.to_excel('ds_{}.xlsx'.format(str(f)))
    #print(os.getcwd + 'ds_{}.xlsx'.format(str(f)))
