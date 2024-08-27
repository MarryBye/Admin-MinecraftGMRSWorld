class BaseType:
    def __init__(self, **kwargs):
        self.__id = kwargs.get("id", -1)
        
    def get_id(self) -> int:
        return self.__id