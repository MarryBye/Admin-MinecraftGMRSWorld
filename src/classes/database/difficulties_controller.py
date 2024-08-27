from src.classes.database.database_controller import DatabaseController
from src.classes.datatypes.difficulty import Difficulty

db_controller = DatabaseController()

class DifficultiesController:
    
    @staticmethod
    def add_difficulty(difficulty_name: str):
        pass
    
    @staticmethod
    def get_difficulty(id) -> Difficulty:
        pass