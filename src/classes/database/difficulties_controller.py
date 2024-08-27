from src.classes.database.database_controller import DatabaseController
from src.classes.datatypes.difficulty import Difficulty

db_controller = DatabaseController()

class DifficultiesController:
    
    @staticmethod
    def add_difficulty(difficulty_name: str):
        
        query = (
            '''
            SELECT * FROM add_difficulty(%s)
            '''
        )
        args = [difficulty_name]
        
        db_controller.execute_query(
            query=query, 
            args=args
        )
    
    @staticmethod
    def get_difficulty(id) -> Difficulty:
        
        query = (
            '''
            SELECT * FROM get_defficulty(%s)
            '''
        )
        args = [id]
        
        callback_data = db_controller.execute_query(
            query=query,
            args=args,
            fetch_results=1
        )
        
        return Difficulty(**callback_data)