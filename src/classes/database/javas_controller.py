from src.classes.database.database_controller import DatabaseController
from src.classes.datatypes.java import Java

db_controller = DatabaseController()

class JavasController:
    
    @staticmethod
    def add_java(java_version: str, java_url: str):
        
        query = (
            '''
            SELECT * FROM add_java(%s, %s)
            '''
        )
        args = [java_version, java_url]
        
        db_controller.execute_query(
            query=query,
            args=args
        )
    
    @staticmethod
    def get_java(id) -> Java:
        
        query = (
            '''
            SELECT * FROM get_java(%s)
            '''
        )
        args = [id]
        
        callback_data = db_controller.execute_query(
            query=query,
            args=args,
            fetch_results=1
        )
        
        return Java(**callback_data)