from Components.Component import Component
import sqlite3
from datetime import datetime

class Database(Component):
    """
    A database class that implements database creation and methods to read and write from the database. Creates the following tables: 
    1. firstBoot
    2. picture
    3. attitudeDetermination
    4. data
    5. housekeeping
    """
    def __init__(self):
        """
        Initializes a Database object, calls the parent constructor, and connects to a sqlite3 database.
        """
        super().__init__("Database", 1)
        self.connection = sqlite3.connect('db.sqlite3')
        self.initdb()


    def update(self, context):
        """
        Concrete implementation of Component.update().
        Takes a dictionary (context) as a parameter, and writes it to a new row in the database.  
        """
        self.commitContext(context)


    def getFirstBoot(self):
        """
        Queries the firstBoot table in the database and returns the firstBoot value if it exists.
        If no firstBoot value exists, returns None.
        """
        cursor = self.connection.execute("SELECT * FROM first_boot")
        rows = cursor.fetchall()
        if len(rows) == 0:
            return None
        return rows[0][0]


    def setFirstBoot(self, time):
        """
        Takes a datetime string as a parameter and inserts
        it into the firstBoot table in the database.  
        """
        insertCommand = """INSERT INTO firstBoot VALUES (?);"""
        self.connection.execute("INSERT INTO first_boot VALUES(?)", (time,))
        self.connection.commit()


    def commitContext(self, context):
        """
        Commits context to the database for storage.
        """
        time = 0
        drvr_00 = 0
        drvr_01 = 0
        drvr_02 = 0
        drvr_03 = 0
        drvr_04 = 0
        drvr_05 = 0
        drvr_06 = 0
        drvr_07 = 0
        drvr_08 = 0
        drvr_09 = 0
        drvr_10 = 0
        drvr_11 = 0
        drvr_12 = 0
        drvr_13 = 0
        drvr_14 = 0
        drvr_15 = 0
        drvr_16 = 0
        drvr_17 = 0
        drvr_18 = 0
        drvr_19 = 0

        if ('clock' in context):
            time = context['clock']
        self.connection.execute("INSERT INTO data (time, drvr_00, drvr_01, drvr_02, drvr_03, drvr_04, drvr_05, drvr_06, drvr_07, drvr_08, drvr_09, drvr_10, drvr_11, drvr_12, drvr_13, drvr_14, drvr_15, drvr_16, drvr_17, drvr_18, drvr_19) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
        time,
        drvr_00,
        drvr_01,
        drvr_02,
        drvr_03,
        drvr_04,
        drvr_05,
        drvr_06,
        drvr_07,
        drvr_08,
        drvr_09,
        drvr_10,
        drvr_11,
        drvr_12,
        drvr_13,
        drvr_14,
        drvr_15,
        drvr_16,
        drvr_17,
        drvr_18,
        drvr_19))
        self.connection.commit()


    def initdb(self):
        """
        Creates database tables if they don't exist.
        1. A data table that stores datapoints taken by the hardware
        """
        cursor = self.connection.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS first_boot
            (time int PRIMARY KEY)''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS data
            (time int PRIMARY KEY,
            drvr_00 int,
            drvr_01 int,
            drvr_02 int,
            drvr_03 int,
            drvr_04 int,
            drvr_05 int,
            drvr_06 int,
            drvr_07 int,
            drvr_08 int,
            drvr_09 int,
            drvr_10 int,
            drvr_11 int,
            drvr_12 int,
            drvr_13 int,
            drvr_14 int,
            drvr_15 int,
            drvr_16 int,
            drvr_17 int,
            drvr_18 int,
            drvr_19 int)''')
        self.connection.commit()
