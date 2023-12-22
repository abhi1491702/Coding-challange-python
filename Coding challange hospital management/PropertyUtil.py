import configparser

class PropertyUtil:
    @staticmethod
    def get_property_string(file_name):
        config = configparser.ConfigParser()
        config.read(file_name)

        # Read database connection properties from the property file
        host = config.get('Database', 'host')
        user = config.get('Database', 'user')
        password = config.get('Database', 'password')
        database = config.get('Database', 'database')
        port = config.get('Database', 'port')

        connection_string = {
            'host': 'localhosthost',
            'user': 'root',
            'password': 'Ram@12345',
            'database': 'HospitalManagementSystem',
            'port': '3306'
        }

        return connection_string
