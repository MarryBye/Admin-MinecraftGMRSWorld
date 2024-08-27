from src.classes.datatypes.base_type import BaseType

class Tag(BaseType):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        
        self.__tag_name = kwargs.get("tag_name", "N/A")
        self.__tag_color = kwargs.get("tag_color", "N/A")
        
    def get_name(self) -> str:
        return self.__tag_name
    
    def get_color(self) -> str:
        return self.__tag_color