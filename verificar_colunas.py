import sqlite3

def listar_colunas():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("PRAGMA table_info(relatorios)")
    colunas = c.fetchall()
    conn.close()

    print("Colunas da tabela 'relatorios':")
    for coluna in colunas:
        print(coluna)

if __name__ == "__main__":
    listar_colunas()
