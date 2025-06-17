def verificar_admin(usuario, senha):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('SELECT senha_hash FROM admin WHERE usuario=?', (usuario,))
    result = c.fetchone()
    conn.close()

    if result:
        hash_armazenado = result[0]

        # Compatível: BLOB ou TEXT
        if isinstance(hash_armazenado, str):
            hash_bytes = hash_armazenado.encode()
        else:
            hash_bytes = hash_armazenado

        if bcrypt.checkpw(senha.encode(), hash_bytes):
            return True
    return False


