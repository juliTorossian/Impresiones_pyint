import traceback
from ...config.conn_db import ConnDB


class ModeloModel():

    def insertModelo(modelo):
        conn = ConnDB()

        query = 'INSERT INTO modelo(nombre) VALUES (?);'
        params=[(modelo.nombre)]

        try:
            conn.cursor.execute(query, params)
            modelo.id = conn.cursor.lastrowid
        except Exception as e:
            print(e)
            print(traceback.format_exc())
        finally:
            conn.cerrar_conn()

        return modelo

    def getModelos():
        conn = ConnDB()
        modelos = []

        query = 'SELECT * FROM modelo;'
        params=()

        try:
            conn.cursor.execute(query, params)
            modelos = conn.cursor.fetchall()
        except Exception as e:
            print(e)
            print(traceback.format_exc())
        finally:
            conn.cerrar_conn()
        
        return modelos

    def getModelo(modelo_id):
        conn = ConnDB()
        modelo=None

        query = 'SELECT * FROM modelo WHERE id = ?;'
        params=[(modelo_id)]

        try:
            conn.cursor.execute(query, params)
            modelo = conn.cursor.fetchone()
        except Exception as e:
            print(e)
            print(traceback.format_exc())
        finally:
            conn.cerrar_conn()
        
        return modelo
    
    def updateModelo(modelo):
        conn = ConnDB()

        query = '''
            UPDATE modelo
            SET nombre = ?
            WHERE id = ?
            '''
        params=(modelo.nombre, modelo.id)

        try:
            conn.cursor.execute(query, params)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
        finally:
            conn.cerrar_conn()
        
        return modelo
    
    def deleteModelo(modelo_id):
        conn = ConnDB()

        query = '''
            DELETE FROM modelo
            WHERE id = ?
            '''
        params=[(modelo_id)]

        try:
            conn.cursor.execute(query, params)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
        finally:
            conn.cerrar_conn()
        
        return modelo_id



class Modelo:

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return f'Modelo[{self.id},{self.nombre}]'
    
    def is_valid(self):
        valid = True

        if (self.nombre == ''):
            valid = False
        
        return valid