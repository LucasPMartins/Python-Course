# PyMySQL - um cliente MySQL feito em Python Puro
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import pymysql
import pymysql.cursors
import dotenv
import os

TABLE_NAME = 'customers'
CURRENT_CURSOR = pymysql.cursors.DictCursor

# Carrega as variáveis de ambiente
dotenv.load_dotenv()

# Conexão com o banco de dados
connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=CURRENT_CURSOR,
)

# Criação de tabelas
with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ( '
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(50) NOT NULL, '
            'age INT NOT NULL, '
            'PRIMARY KEY (id) '
            ') '
        )
        # Limpa a tabela
        cursor.execute(
            f'TRUNCATE TABLE {TABLE_NAME}'
        )
    connection.commit()
    
    # Manipulação de dados
    print('Inserindo registros:')
    with connection.cursor() as cursor:
        sql = f'INSERT INTO {TABLE_NAME} (name, age) VALUES (%s, %s)'
        result = cursor.executemany(
            sql,
            (('João', 30), ('Maria', 25), ('Helena', 40), ('Joana', 35))
        )
        print('Total inseridos:',result)
    connection.commit()

    print('Inserindo registros com dicionários:')
    with connection.cursor() as cursor:
        sql = f'INSERT INTO {TABLE_NAME} (name, age) VALUES (%(name)s, %(age)s)'
        data = {'name': 'Luiz', 'age': 30}
        result = cursor.execute(sql, data)
        print(sql)
        print(data)
        print(result)
    connection.commit()
    
    print('Todos os registros:')
    with connection.cursor() as cursor:
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
        )
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print(row)

    print('Registros com idade maior que 30:')
    with connection.cursor() as cursor:
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE age > 30'
        )
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print(row)
            
    print('Teste de SQL Injection:')
    with connection.cursor() as cursor:
        input_id = input('Digite o id do registro: ')
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            f'WHERE id = %s'
        )
        cursor.execute(sql,input_id)
        result = cursor.fetchall()
        for row in result:
            print(row)

    print('Deletando registros:')
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = 1'
        )
        cursor.execute(sql)
        connection.commit() 
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
        )
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print(row)

    print('Atualizando registros:')
    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET age = %s '
            'WHERE id = 2'
        )
        cursor.execute(sql,60)
        connection.commit()
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
        )
        result = cursor.execute(sql)
        print('Total de registros:',result)
        # Ou
        # print('Total de registros:',cursor.rowcount)
        # Ou
        # print('Total de registros:',len(cursor.fetchall()))
        for row in cursor.fetchall():
            print(row)
