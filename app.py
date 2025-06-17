import streamlit as st
import sqlite3
from datetime import datetime


# Função para criar tabela com coluna 'ano'
def criar_tabela():
    with sqlite3.connect("database.db") as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS relatorios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                mes TEXT,
                ano INTEGER,
                participou INTEGER,
                estudos_biblicos INTEGER,
                horas INTEGER,
                data_envio TEXT
            )
        """)
        conn.commit()

# Função para inserir relatório com ano atual e data/hora atual
def inserir_relatorio(nome, mes, participou, estudos_biblicos, horas):
    ano = datetime.now().year
    data_envio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with sqlite3.connect("database.db") as conn:
        c = conn.cursor()
        c.execute("""
            INSERT INTO relatorios (nome, mes, ano, participou, estudos_biblicos, horas, data_envio)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (nome, mes, ano, int(participou), estudos_biblicos, horas, data_envio))
        conn.commit()

# --- Streamlit ---

st.title("📄 Enviar Relatório")

criar_tabela()

nome = st.text_input("Nome")
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]
mes = st.selectbox("Mês de referência", meses)

participou = st.checkbox("Marque se participou do ministério")

estudos_biblicos = st.number_input("Número de Estudos Bíblicos", min_value=0, step=1)
horas = st.number_input("Horas", min_value=0, step=1)

if st.button("Enviar Relatório"):
    if nome.strip() == "":
        st.error("Por favor, preencha o nome.")
    else:
        inserir_relatorio(nome, mes, participou, estudos_biblicos, horas)
        st.success("✅ Relatório enviado com sucesso!")

