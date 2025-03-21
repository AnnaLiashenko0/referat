Порушується:
class MySQLDatabase:
    def connect(self):
        print("Connecting to MySQL database")

class Service:
    def __init__(self):
        self.db = MySQLDatabase()  # Пряме створення залежності

    def perform_task(self):
        self.db.connect()
        print("Performing task")

# Високорівневий клас залежить від низькорівневої реалізації бази даних








Приклад застосування в Python:
class Database:
    def connect(self):
        pass

class MongoDB(Database):
    def connect(self):
        print("Connecting to MongoDB")

class MySQL(Database):
    def connect(self):
        print("Connecting to MySQL")

class Application:
    def __init__(self, db: Database):
        self.db = db

    def start(self):
        self.db.connect()

app = Application(MongoDB())
app.start()
