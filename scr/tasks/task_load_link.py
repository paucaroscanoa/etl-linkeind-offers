from mysql.connector import (connection)
from prefect import task

@task(name="Carga de data en base de datos")
def task_load_link(offer_lists):
    try:
        conn = connection.MySQLConnection(
            user='root', 
            password='Mario4190&$',
            host='127.0.0.1',
            database='mpbase'
            )
        cursor = conn.cursor()
        
        query_table = """CREATE TABLE IF NOT EXISTS offer_lists(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            location VARCHAR(255),
            url_value TEXT,
            skill VARCHAR(255)
        )"""
        cursor.execute(query_table)
        
        query_insert = "INSERT INTO offer_lists(title, location, url_value,skill) VALUES (%s, %s, %s,%s)"
        
        for offer_list in offer_lists:
            cursor.execute(query_insert, (offer_lists['title'], offer_lists['location'], offer_lists['url_value'],offer_lists['skill']))
        
        conn.commit()
        cursor.close()
        conn.close()
        print("datos guardados en bd...")
    except mysql.connector.Error as error:
        print("Failed to insert record into Laptop table {}".format(error))