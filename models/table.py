from models.db import mysql    

def create_table():
    conn = mysql.connect()
    cursor = conn.cursor()

    query = (
        "CREATE TABLE IF NOT EXISTS contato ("
        "ID INT NOT NULL AUTO_INCREMENT,"
        "Nome VARCHAR(100) NOT NULL,"
        "Sobrenome VARCHAR(100) NOT NULL,"
        "Email VARCHAR(100) NOT NULL,"
        "Telefone VARCHAR(20) NOT NULL,"
        "PRIMARY KEY (ID))"
    )

    cursor.execute(query)

    conn.commit()
    cursor.close()
    conn.close()

    print("Table 'contato' created successfully!")