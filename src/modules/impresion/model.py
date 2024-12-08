import traceback
from ...config.conn_db import ConnDB


class ImpresionModel():

    def insertImpresion(impresion):
        conn = ConnDB()
        print(impresion)

        query = 'INSERT INTO impresion(modelo, t_impresion_est, t_impresion_fin, filamento, gr_consu, parametros) VALUES (?, ?, ?, ?, ?, ?);'
        params=(impresion.modelo, impresion.t_impresion_est, impresion.t_impresion_fin, impresion.filamento, impresion.gr_consumidos, impresion.parametros)

        try:
            conn.cursor.execute(query, params)
            impresion.id = conn.cursor.lastrowid
        except Exception as e:
            print(e)
            print(traceback.format_exc())
        finally:
            conn.cerrar_conn()

        return impresion

    def getImpresiones():
        conn = ConnDB()
        impresiones = []

        query = 'SELECT * FROM impresion;'
        params=()

        try:
            conn.cursor.execute(query, params)
            impresiones = conn.cursor.fetchall()
        except Exception as e:
            print(e)
            print(traceback.format_exc())
        finally:
            conn.cerrar_conn()
        
        return impresiones

    def getImpresion(impresion_id):
        conn = ConnDB()
        impresion=None

        query = 'SELECT * FROM impresion WHERE id = ?;'
        params=[(impresion_id)]

        try:
            conn.cursor.execute(query, params)
            impresion = conn.cursor.fetchone()
        except Exception as e:
            print(e)
            print(traceback.format_exc())
        finally:
            conn.cerrar_conn()
        
        return impresion
    
    def updateImpresion(impresion):
        conn = ConnDB()

        query = '''
            UPDATE impresion
            SET modelo = ?,
                t_impresion_est = ?,
                t_impresion_fin = ?,
                filamento = ?,
                gr_consu = ?,
                parametros = ?
            WHERE id = ?
            '''
        params=(impresion.modelo, impresion.t_impresion_est, impresion.t_impresion_fin, impresion.filamento, impresion.gr_consumidos, impresion.parametros, impresion.id)

        try:
            conn.cursor.execute(query, params)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
        finally:
            conn.cerrar_conn()
        
        return impresion
    
    def deleteImpresion(impresion_id):
        conn = ConnDB()

        query = '''
            DELETE FROM impresion
            WHERE id = ?
            '''
        params=[(impresion_id)]

        try:
            conn.cursor.execute(query, params)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
        finally:
            conn.cerrar_conn()
        
        return impresion_id



class Impresion:

    def __init__(self, id, modelo, t_impresion_est, t_impresion_fin, filamento, gr_consumidos, parametros):
        self.id = id
        self.modelo = modelo
        self.t_impresion_est = t_impresion_est
        self.t_impresion_fin = t_impresion_fin
        self.filamento = filamento
        self.gr_consumidos = gr_consumidos
        self.parametros = parametros


    def __str__(self):
        return f'Impresion[{self.id},{self.modelo},{self.t_impresion_est},{self.t_impresion_fin},{self.filamento},{self.gr_consumidos},{self.parametros}]'
    
    def is_valid(self):
        valid = True

        if (self.modelo <= 0):
            valid = False
        if (self.t_impresion_est <= 0):
            valid = False
        if (self.t_impresion_fin <= 0):
            valid = False
        if (self.filamento <= 0):
            valid = False
        if (self.gr_consumidos <= 0):
            valid = False
        if (self.parametros == ''):
            valid = False
        
        return valid