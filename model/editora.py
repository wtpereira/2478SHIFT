class Editora:

    def __init__(self, id: int = None, nome: str = None, endereco: str = None, telefone: str = None):
        self.__id: int = id
        self.__nome: str = nome
        self.__endereco: str = endereco
        self.__telefone: str = telefone

    def __str__(self) -> str:
        return f'{self.id} | {self.nome} | {self.endereco} | {self.telefone}'

    def __repr__(self) -> str:
        return f'{self.id} | {self.nome} | {self.endereco} | {self.telefone}'

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
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    def dump(self) -> dict:
        if self.__id:
            return {'id': self.__id, 'nome': self.__nome, 'endereco': self.__endereco, 'telefone': self.__telefone}

        return {'nome': self.__nome, 'endereco': self.__endereco, 'telefone': self.__telefone}
