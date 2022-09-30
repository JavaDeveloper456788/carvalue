import imp
import mysql.connector
import consts
import os

# This class handles the database and communicates with backend
class DBHandler:
    def __init__(self):
        # connecting with database
        self.mydb = mysql.connector.connect(
            host=os.environ["searchtool_mysql_host"],
            user=os.environ["searchtool_mysql_user"],
            password=os.environ["searchtool_mysql_password"]
        )
        self.mycursor = self.mydb.cursor()
    
    # main search function without mileage
    def search(self, year, make, model):
        self.mycursor.execute(consts.SEARCH_QUERY, (make, model, year))
        return self.mycursor.fetchall()
    
    # function to search database with mileage filter
    
    def searchMileage(self, year, make, model, mileage):
        self.mycursor.execute(consts.SEARCH_QUERY_MILEAGE, (make, model, year, mileage - consts.MILEAGE_DIFF, mileage + consts.MILEAGE_DIFF))
        return self.mycursor.fetchall()
