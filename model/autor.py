class Autor:

    def __init__(self, id: int = None, nome: str = None, email: str = None, telefone: str = None, bio: str = None):
        self.__id: int = id
        self.__nome: str = nome
        self.__email: str = email
        self.__telefone: str = telefone
        self.__bio: str = bio

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
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone

    @property
    def bio(self) -> str:
        return self.__bio

    @bio.setter
    def bio(self, bio: str):
        self.__bio = bio

    def dump(self) -> dict:
        if self.__id:
            return {'id': self.__id, 'nome': self.__nome, 'email': self.__email}

        return {'nome': self.__nome, 'email': self.__email}
