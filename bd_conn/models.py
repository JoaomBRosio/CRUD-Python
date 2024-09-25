import psycopg2
from psycopg2 import sql

# conecta com o bd
def conectar_banco():
    conn = psycopg2.connect(
        host="localhost",
        database="python_conn",
        user="postgres",
        password="pg482"
    )
    return conn

# cria a tabela de usuarios (caso ela não exista)
def criar_banco():
    conn = conectar_banco()
    cursor = conn.cursor() # a var cursor é um objeto utilizado para interagir com o banco de dados
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id SERIAL PRIMARY KEY,
                        nome VARCHAR(100) NOT NULL,
                        email VARCHAR(100) NOT NULL UNIQUE,
                        senha VARCHAR(100) NOT NULL)''')
    conn.commit() # precisa usar depois de inserir, atualizar ou excluir dados no banco
    conn.close() # depois de usar o cursor tem que fechar

# função de cadastro de usuario
def cadastrar_usuario(nome, email, senha):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)', (nome, email, senha))
    conn.commit()
    conn.close()

# função de verificação de validação de login
def verificar_login(email, senha):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE email = %s AND senha = %s', (email, senha))
    usuario = cursor.fetchone() # é usado após uma consulta SELECT para buscar uma única linha dos resultados da consulta
    conn.close()
    return usuario

def buscar_usuario(id): # isso é usado no update
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE id = %s', (id,))
    usuario = cursor.fetchone()
    conn.close()
    return usuario
    
def editar_usuario(id, nome, email, senha):
    conn = conectar_banco()
    cursor = conn.cursor()
    query = '''
        UPDATE usuarios 
        SET nome = %s, email = %s, senha = %s 
        WHERE id = %s
    '''
    print(query, (nome, email, senha, id))  # mostra a consulta e os parâmetros
    cursor.execute(query, (nome, email, senha, id))
    conn.commit() # precisa usar depois de inserir, atualizar ou excluir dados no banco
    conn.close() # depois de usar o cursor tem que fechar