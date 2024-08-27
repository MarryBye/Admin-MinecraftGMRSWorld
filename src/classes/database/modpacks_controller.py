from src.classes.database.database_controller import DatabaseController

from src.classes.datatypes.modpack import Modpack
from src.classes.datatypes.tag import Tag

db_controller = DatabaseController()

class ModpacksController:
    @staticmethod
    
    def get_modpack(id: int) -> Modpack:
        
        query = (
            '''
            SELECT * FROM get_modpack(%s)
            '''
        )
        args = [id]
        
        callback_data = db_controller.execute_query(
            query=query, 
            args=args, 
            fetch_results=1
        )
        
        return Modpack(**callback_data)
    
    @staticmethod
    def add_modpack(modpack_name: str, modpack_description: str, modpack_icon: str, modpack_url: str, modpack_java: int, modpack_type: int, modpack_difficulty: int):
        
        query = (
            '''
            SELECT * FROM add_modpack(%s, %s, %s, %s, %s, %s, %s)
            '''
        )
        args = [
            modpack_name, 
            modpack_description, 
            modpack_icon, 
            modpack_url, 
            modpack_java, 
            modpack_type, 
            modpack_difficulty
        ]
        
        db_controller.execute_query(
            query=query,
            args=args
        )
    
    @staticmethod
    def get_all_modpacks() -> list[Modpack]:
        
        query = (
            '''
            SELECT * FROM get_modpacks()
            '''
        )
        
        callback_data = db_controller.execute_query(
            query=query, 
        )
        
        callback_data = [Modpack(**data) for data in callback_data]
        
        return callback_data
    
    @staticmethod
    def add_modpack_tag(modpack_id, tag_id):
        
        query = (
            '''
            SELECT * FROM add_modpack_tag(%s, %s)
            '''
        )
        args = [modpack_id, tag_id]
        
        db_controller.execute_query(
            query=query,
            args=args
        )
        
    @staticmethod
    def get_modpack_tags(id) -> list[Tag]:
        
        query = (
            '''
            SELECT * FROM get_modpack_tags(%s)
            '''
        )
        args = [id]
        
        callback_data = db_controller.execute_query(
            query=query,
            args=args,
        )
        
        callback_data = [Tag(**data) for data in callback_data]
        
        return callback_data
    