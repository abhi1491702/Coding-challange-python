import mysql.connector
from PropertyUtil import PropertyUtil

class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            try:
                # Get connection string from property file
                connection_string = PropertyUtil.get_property_string("db.properties")

                # Establish the database connection
                DBConnection.connection = mysql.connector.connect(**connection_string)
                print("Connected to the database")
            except mysql.connector.Error as err:
                print("Error:", err)
        return DBConnection.connection
