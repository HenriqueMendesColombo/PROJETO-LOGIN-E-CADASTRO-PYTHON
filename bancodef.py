import sqlite3 as sql
import bcrypt

connect = sql.connect("/home/henrique/Documents/banco.db")
cursor = connect.cursor()

def Tabela_SQL():
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS banco(
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               name TEXT NOT NULL, 
               email TEXT NOT NULL UNIQUE, 
               senha TEXT NOT NULL 
               )
               """)
        connect.commit()
    except sql.OperationalError as erro:
        print("Erro:", erro)

def Cadastrar():
    nome = str(input("Nome: ").strip())
    email = str(input("Email: ").strip())
    senha = str(input("Senha: ").strip())
    byte = senha.encode('utf-8')
    salt = bcrypt.gensalt()
    criptografia = bcrypt.hashpw(byte, salt)
    try:
        cursor.execute("INSERT INTO banco(name, email, senha) VALUES (?, ?, ?)", (nome, email, criptografia))
    except sql.IntegrityError as erro:
        print('Erro:', erro)
    else:
        connect.commit()
        print("Cadastrado com Sucesso!")
def Login():
    email = str(input("Email: ").strip())
    senha = str(input("Senha: ").strip())
    cursor.execute("SELECT email, senha FROM banco WHERE email = ?", (email,))
    email_senha_usuario = cursor.fetchone()
    try:
        hash_salvo = email_senha_usuario[1]
    except TypeError as erro:
        print('ERRO:', erro)
    else:
        chegagem_senha = bcrypt.checkpw(senha.encode('utf-8'), hash_salvo)
        if email == email_senha_usuario[0] and chegagem_senha == True:
            print('Logado com Sucesso!')
        else:
            print('Senha Incorreta!')