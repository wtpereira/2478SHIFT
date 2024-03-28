from database.client_factory import ClientFactory
from model.box import Box


class BoxDAO:

    def __init__(self):
        self.__client = ClientFactory()

    def listar(self) -> list[Box]:
        boxes = list()
        client = self.__client.get_client()
        db = client.livraria
        for documento in db.box.find():
            box = Box(documento['_id'], documento['nome'], documento['livros'])
            boxes.append(box)

        client.close()

        return boxes

    def adicionar(self, box: Box) -> None:
        client = self.__client.get_client()
        db = client.livraria
        result = db.box.insert_one({'nome': box.nome, 'livros': box.livros})
        print(f'Resultado do insert: {result}')
        client.close()
