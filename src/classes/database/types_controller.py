from src.classes.database.database_controller import DatabaseController
from src.classes.datatypes.type import Type

db_controller = DatabaseController()

class TypesController:
    
    @staticmethod
    def add_type(type_name: str):
        
        query = (
            '''
            SELECT * FROM add_type(%s)
            '''
        )
        args = [type_name]
        
        db_controller.execute_query(
            query=query,
            args=args
        )
    
    @staticmethod
    def get_type(id) -> Type:
        
        query = (
            '''
            SELECT * FROM get_type(%s)
            '''
        )
        args = [id]
        
        callback_data = db_controller.execute_query(
            query=query,
            args=args,
            fetch_results=1
        )
        
        return Type(**callback_data)