from src.classes.datatypes.base_type import BaseType

class Difficulty(BaseType):
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)
        
        self.__difficulty_name = kwargs.get("difficulty_name", "N/A")
        
    def get_name(self) -> str:
        return self.__difficulty_name