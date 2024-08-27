from src.classes.database.database_controller import DatabaseController
from src.classes.datatypes.tag import Tag

db_controller = DatabaseController()

class TagsController:
    
    @staticmethod
    def add_tag(tag_name: str, tag_color: str):
        
        query = (
            '''
            SELECT * FROM add_tag(%s, %s)
            '''
        )
        args = [tag_name, tag_color]
        
        db_controller.execute_query(
            query=query,
            args=args
        )
    
    @staticmethod
    def get_tag(id) -> Tag:
        
        query = (
            '''
            SELECT * FROM get_tag(%s)
            '''
        )
        args = [id]
        
        callback_data = db_controller.execute_query(
            query=query,
            args=args,
            fetch_results=1
        )
        
        return Tag(callback_data)