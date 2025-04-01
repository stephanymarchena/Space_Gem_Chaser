import sqlite3

class DBProxy:

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('''
            CREATE TABLE IF NOT EXISTS dados (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT NOT NULL, 
                score INTEGER NOT NULL, 
                date TEXT NOT NULL
            )
        ''')

    def save(self, score_dict: dict):
        """Salva a pontuação no banco de dados."""
        self.connection.execute('INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)', score_dict)
        self.connection.commit()

    def retrieve_top10(self) -> list:
        """Recupera os 10 melhores scores."""
        return self.connection.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()

    def close(self):
        """Fecha a conexão com o banco de dados."""
        try:
            self.connection.close()
        except Exception as e:
            print(f"Erro ao fechar a conexão com o banco de dados: {e}")
