import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='654321',
    database='SEU_BD',
)
cursor = conexao.cursor()

## CRUD ##

# CREATE
Nome_do_curso = "Curso de CSS"
Valor = 125
comando = f'INSERT INTO Cursos (Nome_do_curso, Valor) VALUES ("{Nome_do_curso}", {Valor})'
cursor.execute(comando)
conexao.commit() # edita o banco de dados

# READ
comando = f'SELECT * FROM Cursos'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados
print(resultado)

# UPDATE
Nome_do_curso = "Curso de Python"
Valor = 180
comando = f'UPDATE Cursos SET Valor = {Valor} WHERE Nome_do_curso = "{Nome_do_curso}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados


# DELETE
Nome_do_curso = "Curso de Python"
comando = f'DELETE FROM Cursos WHERE Nome_do_curso = "{Nome_do_curso}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados