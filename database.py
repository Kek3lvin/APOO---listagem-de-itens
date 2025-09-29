from typing import List
import sqlite3
import pandas as pd
from model import Item 
class ItemDAO:
    
    def __init__(self, db_name: str = 'itens.db'):
        self.DB_NAME = db_name
    
    def get_db_connection(self):

        conn = sqlite3.connect(self.DB_NAME)
        conn.row_factory = sqlite3.Row 
        return conn

    def add_item(self, item: Item):

        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(

            (item.nome, item.descricao, item.quantidade)
        )
        conn.commit()
        conn.close()

    def fetch_all_itens(self) -> List[Item]:
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM itens ORDER BY created_at DESC")
        
        rows = cursor.fetchall()
        conn.close()
        
        return [
            Item(
                id=row['id'],
                nome=row['nome'], 
                quantidade=row['quantidade'], 
                descricao=row['descricao'], 
            ) for row in rows
        
        conn = sqlite3.connect('itens.db')

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS itens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL,
            quantidade TEXT NOT NULL
        );
        """)

        conn.commit()
        conn.close()

print("Banco de dados e tabela 'itens' criados com sucesso!")
        ]

        