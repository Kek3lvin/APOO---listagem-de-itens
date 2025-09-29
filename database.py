from typing import List
import sqlite3
import pandas as pd
from model import Item 

class ItemDAO:
    
    def __init__(self, db_name: str = 'item.db'):
        self.DB_NAME = db_name
    
    def get_db_connection(self):
        """Cria e retorna uma conexão com o banco de dados."""
        conn = sqlite3.connect(self.DB_NAME)
        conn.row_factory = sqlite3.Row 
        return conn

    def add_item(self, item: Item):
        """Adiciona um objeto Post ao banco de dados."""
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO item (objeto, descricao, quantidade) VALUES (?, ?, ?)",
            (item.objeto, item.descricao, item.quantidade)
        )
        conn.commit()
        conn.close()

    def fetch_all_itens(self) -> List[Item]:
        """Busca todos os posts e retorna uma lista de objetos Post."""
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM item ORDER BY created_at DESC")
        
        rows = cursor.fetchall()
        conn.close()
        
        return [
            Item(
                id=row['id'], 
                objeto=row['objeto'], 
                descricao=row['descricao'], 
                quantidade=row['quantidade'],
            ) for row in rows
        ]

        

  