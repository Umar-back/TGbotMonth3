import sqlite3
from database import sql_queries

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()
        self.sql_create_tables()  # Вызовите метод для создания таблиц при инициализации

    def sql_create_tables(self):
        if self.connection:
            print("DB connected success!")

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.commit()

    def sql_insert_user_query(self, telegram_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_NAME,
            (None, telegram_id, username, first_name, last_name,)
        )
        self.connection.commit()
