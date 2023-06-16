'''
This class will connect to a specified database in the local SQL server.

'''



import mysql.connector


class contactInfo_SQL:
    def __init__(self, database_name, host, port, username, password):
        self.database_name = database_name
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connection = None
        self.cursor = None
        
        self.connect()
        
        if not self.table_exists('contact_info'):
            self.create_table()
        
        
        
    def connect(self):
        # Connect to the MySQL server without specifying a database
        self.connection = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.username,
            password=self.password
        )
        
        if self.connection.is_connected():
            print("Connected to local MySQL server -- {}".format(self.database_name))
            self.cursor = self.connection.cursor()
            
            # Check if the database exists
            if not self.database_exists():
                self.create_database()
            
            # Connect to the specified database
            self.connection.database = self.database_name
            
            
    def disconnect(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Disconnected from contact info server")
            

    def database_exists(self):
        # Check if the database exists
        self.cursor.execute("SHOW DATABASES LIKE %s", (self.database_name,))
        return self.cursor.fetchone() is not None
    

    def create_database(self):
        # Create the database
        self.cursor.execute(f"CREATE DATABASE {self.database_name}")
        print(f"Database '{self.database_name}' created.")
    

    def table_exists(self, table_name):
        query = f"SHOW TABLES LIKE '{table_name}'"
        self.cursor.execute(query)
        return self.cursor.fetchone() is not None
    

    def create_table(self):
        create_table_query = """
            CREATE TABLE contact_info (
                first_name VARCHAR(100),
                last_name VARCHAR(100),
                phone_number VARCHAR(100),
                email VARCHAR(100),
                date_of_birth VARCHAR(100)
            )
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()
        
        
    def store_contact(self,table_name,first_name,last_name,phone,email,dob):
        insert_query = """
            INSERT INTO {} (first_name, last_name, phone_number, email, date_of_birth)
            VALUES (%s, %s, %s, %s, %s)
        """.format(table_name)
        self.cursor.execute(insert_query, (first_name, last_name, phone, email, dob))
        self.connection.commit()
        
        
    def search_contacts(self,table_name, first_name, last_name, email):
        select_query = """
            SELECT * FROM {} WHERE first_name = %s OR last_name = %s OR email = %s
        """.format(table_name)
        self.cursor.execute(select_query, (first_name, last_name, email))
        result = self.cursor.fetchall()
        return result
    
    def select_all_contacts(self,table_name):
        select_query = f"SELECT * FROM {table_name}"
        self.cursor.execute(select_query)
        result = self.cursor.fetchall()
        return result


        
        
#--------------------------------------------------

if __name__ == '__main__':
    database = contactInfo_SQL(database_name='contact_info_db',
                               host='localhost',
                               port='3306',
                               username='root',
                               password='rocketJA17$',
                               )
    
    #print(database.search_contacts('contact_info','Nick','Colan',''))
    if not database.search_contacts('contact_info','Joe','Smith',''):
        print('No contacts with that info')
    
    

    

    
    
    

        