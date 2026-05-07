import sqlite3

def inicializar_banco():
    conn = sqlite3.connect('cinemas.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cinemas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            capacidade_maxima INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cinema_id INTEGER,
            filme_titulo TEXT NOT NULL,
            publico_registrado INTEGER DEFAULT 0,
            FOREIGN KEY (cinema_id) REFERENCES cinemas (id)
        )
    ''')

    cursor.execute("SELECT COUNT(*) FROM cinemas")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO cinemas (nome, capacidade_maxima) VALUES ('Cine Centro', 100)")
        cursor.execute("INSERT INTO sessoes (cinema_id, filme_titulo) VALUES (1, 'O Poderoso Chefão')")
        print("Banco inicializado com dados de teste!")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    inicializar_banco()