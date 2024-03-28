class Box:

    def __init__(self, id: int = None, nome: str = None, livros: dict = None):
        self.__id: int = id
        self.__nome: str = nome
        self.__livros: dict = livros

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def livros(self) -> dict:
        return self.__livros

    @livros.setter
    def livros(self, livros: dict):
        self.__livros = livros
