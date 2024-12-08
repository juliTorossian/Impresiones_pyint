import traceback
from ...config.conn_db import ConnDB


class FilamentoModel():

    def insertFilamento(filamento):
        conn = ConnDB()

        query = 'INSERT INTO filamento(tipo, color, detalle) VALUES (?, ?, ?);'
        params=(filamento.tipo, filamento.color, filamento.detalle)

        try:
            conn.cursor.execute(query, params)
            filamento.id = conn.cursor.lastrowid
        except Exception as e:
            print(e)
            print(traceback.format_exc())
        finally:
            conn.cerrar_conn()

        return filamento

    def getFilamentos():
        conn = ConnDB()
        filamentos = []

        query = 'SELECT * FROM filamento;'
        params=()

        try:
            conn.cursor.execute(query, params)
            filamentos = conn.cursor.fetchall()
        except Exception as e:
            print(e)
            print(traceback.format_exc())
        finally:
            conn.cerrar_conn()
        
        return filamentos

    def getFilamento(filamento_id):
        conn = ConnDB()
        filamento=None

        query = 'SELECT * FROM filamento WHERE id = ?;'
        params=[(filamento_id)]

        try:
            conn.cursor.execute(query, params)
            filamento = conn.cursor.fetchone()
        except Exception as e:
            print(e)
            print(traceback.format_exc())
        finally:
            conn.cerrar_conn()
        
        return filamento
    
    def updateFilamento(filamento):
        conn = ConnDB()

        query = '''
            UPDATE filamento
            SET tipo = ?,
                color = ?,
                detalle = ?
            WHERE id = ?
            '''
        params=(filamento.tipo, filamento.color, filamento.detalle, filamento.id)

        try:
            conn.cursor.execute(query, params)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
        finally:
            conn.cerrar_conn()
        
        return filamento
    
    def deleteFilamento(filamento_id):
        conn = ConnDB()

        query = '''
            DELETE FROM filamento
            WHERE id = ?
            '''
        params=[(filamento_id)]

        try:
            conn.cursor.execute(query, params)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
        finally:
            conn.cerrar_conn()
        
        return filamento_id



class Filamento:

    def __init__(self, id, tipo, color, detalle):
        self.id = id
        self.tipo = tipo
        self.color = color
        self.detalle = detalle

    def __str__(self):
        return f'Filamento[{self.id},{self.tipo},{self.color},{self.detalle}]'
    
    def is_valid(self):
        valid = True

        if (self.tipo == ''):
            valid = False
        if (self.color == ''):
            valid = False
        
        return valid