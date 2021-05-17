import pymysql


class Database:
    def __init__(self, user, password):
        self._connection = pymysql.connect(
            host='localhost',
            user=user,
            password=password,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self._cursor = self._connection.cursor()

    @property
    def connection(self):
        return self._connection

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def select_database(self, name):
        self.connection.select_db(name)

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, query, params=None):
        self.cursor.execute(query, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
