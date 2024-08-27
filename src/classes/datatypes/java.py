from src.classes.datatypes.base_type import BaseType

class Java(BaseType):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.__java_version = kwargs.get("java_version", "N/A")
        self.__java_url = kwargs.get("java_url", "N/A")
        
    def get_version(self) -> str:
        return self.__java_version
    
    def get_url(self) -> str:
        return self.__java_url