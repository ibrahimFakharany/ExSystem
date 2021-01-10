import pyodbc
import sqlalchemy as sal 
from sqlalchemy import create_engine
class Database_connection:     
    def __init__(self):
        server = 'DESKTOP-DSS0C9T'
        database = 'ExaminationsSystemDB'
        driver = 'SQL Server Native Client 11.0'
        self.cnxn = pyodbc.connect(driver='{SQL Server Native Client 11.0}',
                            server=server, 
                            database=database,               
                            trusted_connection='yes')

        self.engine = sal.create_engine(f'mssql+pyodbc://{server}/{database}?driver={driver}?trusted_connection=yes')
        self.sql_alchemy_connection = self.engine.connect()
        