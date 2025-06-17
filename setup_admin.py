import sqlite3
import bcrypt

def criar_admin(usuario, senha):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    # Limpa a tabela de admin para evitar duplicidade
    c.execute("DELETE FROM admin")

    # Gera o hash e transforma para str para salvar como TEXT
    senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

    # Insere
    c.execute(
        "INSERT INTO admin (usuario, senha_hash) VALUES (?, ?)",
        (usuario, senha_hash)
    )

    conn.commit()
    conn.close()
    print(f"✅ Admin '{usuario}' criado com sucesso!")

if __name__ == "__main__":
    usuario = "admin"
    senha = "minhasenha123"
    criar_admin(usuario, senha)
