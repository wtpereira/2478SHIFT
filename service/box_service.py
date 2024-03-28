from dao.box_dao import BoxDAO
from dao.livro_dao import LivroDAO
from model.box import Box

from service.livro_service import LivroService


class BoxService:

    def __init__(self):
        self.__box_dao: BoxDAO = BoxDAO()
        self.__livro_dao: LivroDAO = LivroDAO()
        self.__livro_service: LivroService = LivroService()

    @property
    def categoria_dao(self) -> BoxDAO:
        return self.__box_dao

    def menu(self):
        print('[Box] Escolha uma das seguintes opções:\n'
                '1 - Listar todos os boxes de livros\n'
                '2 - Adicionar novo box de livros\n'
                '3 - Excluir box de livros\n'
                '4 - Ver box por Id\n'
                '0 - Voltar ao menu anterior\n')
        escolha = input('Digite a opção: ')

        if escolha == '0':
            return
        if escolha == '1':
            self.listar()
        elif escolha == '2':
            self.adicionar()
        elif escolha == '3':
            self.remover()
        elif escolha == '4':
            self.mostrar_por_id()
        else:
            print('Opção inválida! Por favor, tente novamente!')

        self.menu()

    def listar(self):
        print('\nListando boxes de livros...')

        try:
            boxes = self.__box_dao.listar()
            if len(boxes) == 0:
                print('Nenhum box de livro encontrado!')

            for box in boxes:
                print(f'{box.id} | {box.nome} | {box.livros}')
        except Exception as e:
            print(f'Erro ao exibir os boxes! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def adicionar(self):
        print('\nAdicionando um box de livros...')

        try:
            nome = input('Digite o nome do box: ')

            print('Livros disponíveis:')
            self.__livro_service.listar()

            ids_livros = input('Digite os IDs dos livros separados por vírgula: ')
            lista_de_ids = ids_livros.split(',')
            lista_de_livros = list()
            for id_livro in lista_de_ids:
                livro = self.__livro_dao.buscar_por_id(id_livro)
                if livro:
                    lista_de_livros.append(livro.dump())

            novo_box = Box(nome=nome, livros=lista_de_livros)
            self.__box_dao.adicionar(novo_box)
        except Exception as e:
            print(f'Erro ao inserir box: {e}')
            return
