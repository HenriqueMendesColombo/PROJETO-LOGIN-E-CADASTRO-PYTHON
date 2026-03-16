import sqlite3 as sql
import bcrypt 
import bancodef as bc

connect = sql.connect("/home/henrique/Documents/banco.db")
cursor = connect.cursor()

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

while True:
    menu = int(input("""
CADASTRAR[1]
LOGIN[2]
SAIR[3]
                                      
// """))
    if menu == 3:
        break
    if menu == 1:
        bc.Cadastrar()
    elif menu == 2:
       bc.Login()
        
    else:
        print("Tente Novamente!")

connect.commit()
connect.close()