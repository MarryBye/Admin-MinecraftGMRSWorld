from src.classes.database.database_controller import DatabaseController
from src.classes.datatypes.tag import Tag

db_controller = DatabaseController()

class TagsController:
    
    @staticmethod
    def add_tag(tag_name: str, tag_color: str):
        pass
    
    @staticmethod
    def get_tag(id) -> Tag:
        pass