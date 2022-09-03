from dataclasses import dataclass
import sqlite3
class Database:
    def __init__(self,DatabaseName):
        self.conn = sqlite3.connect(DatabaseName+".db")
        self.conn.execute('CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT,content TEXT NOT NULL);')
        #self.conn.execute("INSERT INTO dados_pessoais (nome_da_rua,cpf) VALUES ('R. Quatá','123.456.789-00');""")
    def add(self,note):
        self.conn.execute(f"INSERT INTO note (title,content) VALUES ('{note.title}','{note.content}');")
        self.conn.commit()
    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        return [Note(linha[0],linha[1],linha[2])for linha in cursor]

    def update(self,note):
        self.conn.execute(f"UPDATE note SET title = '{note.title}' WHERE id = '{note.id}'")
        self.conn.execute(f"UPDATE note SET content = '{note.content}' WHERE id = '{note.id}'")
        self.conn.commit()

    def delete(self, note_id):
        self.conn.execute(f"DELETE FROM note WHERE id = '{note_id}';")
        self.conn.commit()
        
@dataclass
class Note:
    def __init__(self, id=None, title=None,content=''):
        self.id = id
        self.title = title
        self.content = content
