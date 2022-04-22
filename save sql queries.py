import pandas as pd
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=prod-sql01.pepperi.com;'
                      'Database=Max2000_1410;'
                      'Trusted_Connection=yes;')

sql_query = pd.read_sql_query(''' 
                              select top 10 * from dbo.Plnt_Items_Price PIP where  PIP.C =   61422985
                              '''
                              ,conn) # here, the 'conn' is the variable that contains your database connection information from step 2

df = pd.DataFrame(sql_query)
df.to_csv (r'C:\Temp\exported_data.csv', index = False) # place 'r' before the path name