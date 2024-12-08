import sqlite3

class ConnDB():
    def __init__(self):
        self.base_datos = './ddbb/db.db'
        self.conn = sqlite3.connect(self.base_datos)
        self.cursor = self.conn.cursor()

    def cerrar_conn(self):
        self.conn.commit()
        self.conn.close()