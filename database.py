import sqlite3

#DDL
# def ddl():
#     query =  """CREATE TABLE IF NOT EXISTS livros(
#     isbn TEXT PRIMARY KEY,
#     titulo TEXT,
#     autor TEXT
#     );
#     """
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute(query)
#     conn.commit()
#     conn.close()

# #DML
# def dml():
#     query = """INSERT INTO livros (isbn, titulo, autor)
#     VALUES ('qualquer', 'qualquer titulo', 'qualquer autor');
#     """
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute(query)
#     conn.commit()
#     conn.close()

# def dql():
#     query = """SELECT * FROM livros WHERE isbn = 'qualquer';
#     """
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute(query)
#     # result = cursor.fetchone() # Mostra um Registro
#     result = cursor.fetchall()
#     print(result)
#     conn.close()

# if __name__ == '__main__' :
#     query = """INSERT INTO alunos (numero, nome, turma)
#     VALUES ({}, '{}', '{}');
#     """.format(2, "Lemos", "3B2")
#     """CREATE TABLE alunos (
#         numero INT PRIMARY KEY,
#         nome TEXT NOT NULL,
#         turma TEXT NOT NULL
#     );"""
#     atualiza_banco(query)


def atualiza_banco(query):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

def dql():
    query = """SELECT * FROM livros;
    """
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(query)
    # result = cursor.fetchone() # Mostra um registro
    result = cursor.fetchall()
    print(result)
    conn.close()

if __name__ == '__main__':
    query = """INSERT INTO alunos (numero, nome, turma)
    VALUES ({}, '{}', '{}');
    """.format(2, "Lemos", "3B2")
    """CREATE TABLE ALUNOS (
        numero INT PRIMARY KEY,
        nome TEXT NOT NULL,
        turma TEXT NOT NULL
    );"""
    atualiza_banco(query)
