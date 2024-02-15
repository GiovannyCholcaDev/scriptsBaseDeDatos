from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Clase para manejar la conexión a la base de datos
class Database:
    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self):
        return self.SessionLocal()

# Aquí definimos cómo conectarnos a nuestra base de datos MySQL. 
DATABASE_URL = "mysql+mysqlconnector://root:admin@localhost/instituto"
