import sqlite3

conn = sqlite3.connect('item.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    objeto TEXT NOT NULL,
    descricao TEXT NOT NULL,
    quantidade TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")
conn.commit()
conn.close()

print("Banco de dados e tabela 'itens' criados com sucesso!")