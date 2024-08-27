from src.classes.datatypes.base_type import BaseType

class Type(BaseType):
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)
        
        self.__type_name = kwargs.get("type_name", "N/A")
        
    def get_name(self) -> str:
        return self.__type_name