import sqlite3
import bcrypt

def create_tables():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS admin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT,
            senha_hash TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS relatorios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            mes TEXT,
            ministerio INTEGER,
            estudos INTEGER,
            horas INTEGER,
            data TEXT
        )
    ''')
    conn.commit()
    conn.close()

def criar_admin(usuario, senha):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    # Gera o hash e converte para string
    senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

    c.execute(
        'INSERT INTO admin (usuario, senha_hash) VALUES (?, ?)',
        (usuario, senha_hash)
    )

    conn.commit()
    conn.close()


def verificar_admin(usuario, senha):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT senha_hash FROM admin WHERE usuario=?", (usuario,))
    result = c.fetchone()
    conn.close()
    if result and bcrypt.checkpw(senha.encode(), result[0]):
        return True
    return False
