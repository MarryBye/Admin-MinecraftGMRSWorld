from src.classes.database.database_controller import DatabaseController

from src.classes.datatypes.modpack import Modpack

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
        
        return Modpack(callback_data)
    
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
        
        callback_data = list(map(Modpack, callback_data))
        
        return callback_data
    
    