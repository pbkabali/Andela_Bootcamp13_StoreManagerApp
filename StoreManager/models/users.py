
import psycopg2
from ..db.db import DbConnection



class User(DbConnection):
 
   
    def get_users(self):
        command = """SELECT * FROM users"""
        self.cursor.execute(command)
        users = self.cursor.fetchall()
        return users 

    def get_a_user(self, username):
        command = """SELECT * FROM users WHERE username = %s"""
        self.cursor.execute(command,[username])
        return self.cursor.fetchone()

    def addUser(self, first_name, last_name, username, password, role): 
        command = """INSERT INTO users (first_name, last_name, username, 
        password, role) VALUES ( %s, %s, %s,%s, %s) """
        self.cursor.execute(
            command, (first_name, last_name, username, password, role)                         
        )   

    def login(self, username, password):
        command = """SELECT * FROM users WHERE username = %s"""
        self.cursor.execute(command, [username])
        user = self.cursor.fetchone()
        if not user:
            response = "incorrect username"
        elif user['password'] != password:
            response = "incorrect password!"
        else:
            response = user['role']
        return response
