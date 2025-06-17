import sqlite3
import bcrypt

# Conecta ao banco
conn = sqlite3.connect("database.db")
c = conn.cursor()

# Cria tabela de relatórios
c.execute("""
CREATE TABLE IF NOT EXISTS relatorios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    mes TEXT,
    participou INTEGER,
    estudos_biblicos INTEGER,
    horas INTEGER
)
""")

# Cria tabela de admin
c.execute("""
CREATE TABLE IF NOT EXISTS admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT UNIQUE,
    senha_hash BLOB
)
""")

# Cria um usuário admin padrão, se não existir
usuario_admin = "admin"
senha = "admin123"

# Verifica se já existe
c.execute("SELECT * FROM admin WHERE usuario = ?", (usuario_admin,))
if not c.fetchone():
    senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
    c.execute("INSERT INTO admin (usuario, senha_hash) VALUES (?, ?)", (usuario_admin, senha_hash))
    print(f"Usuário admin criado: {usuario_admin} / Senha: {senha}")
else:
    print("Usuário admin já existe.")

conn.commit()
conn.close()
