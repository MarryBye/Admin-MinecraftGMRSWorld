from src.classes.datatypes.base_type import BaseType

class Modpack(BaseType):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        
        self.__modpack_name = kwargs.get("modpack_name", "N/A")
        self.__modpack_description = kwargs.get("modpack_description", "N/A")
        self.__modpack_icon = kwargs.get("modpack_icon", "N/A")
        self.__modpack_url = kwargs.get("modpack_url", "N/A")
        self.__modpack_java = kwargs.get("modpack_java", -1)
        self.__modpack_type = kwargs.get("modpack_type", -1)
        self.__modpack_difficulty = kwargs.get("modpack_difficulty", -1)
        self.__modpack_tags = kwargs.get("modpack_tags", [])
        
    def get_name(self) -> str:
        return self.__modpack_name
    
    def get_description(self) -> str:
        return self.__modpack_description
    
    def get_icon(self) -> str:
        return self.__modpack_icon
    
    def get_url(self) -> str:
        return self.__modpack_url
    
    def get_java(self) -> int:
        return self.__modpack_java
    
    def get_type(self) -> int:
        return self.__modpack_type
    
    def get_difficulty(self) -> int:
        return self.__modpack_difficulty
    
    def get_tags(self) -> list:
        return self.__modpack_tags