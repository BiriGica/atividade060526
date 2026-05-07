import sqlite3

class RegistroPublicoRepository:
    def __init__(self):
        self.db_name = 'cinemas.db'

    def buscar_dados_sessao_e_cinema(self, sessao_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        query = '''
            SELECT s.id, s.publico_registrado, c.capacidade_maxima 
            FROM sessoes s
            JOIN cinemas c ON s.cinema_id = c.id
            WHERE s.id = ?
        '''
        cursor.execute(query, (sessao_id,))
        resultado = cursor.fetchone()
        conn.close()
        
        if resultado:
            return {
                "id": resultado[0],
                "publico_registrado": resultado[1],
                "capacidade_maxima": resultado[2]
            }
        return None

    def atualizar_publico(self, sessao_id, novo_total):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE sessoes SET publico_registrado = ? WHERE id = ?", (novo_total, sessao_id))
            conn.commit()
            return True
        except:
            return False
        finally:
            conn.close()