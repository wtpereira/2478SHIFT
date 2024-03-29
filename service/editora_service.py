from dao.editora_dao import EditoraDAO
from model.editora import Editora
from utils import editoras_csv, editoras_json

class EditoraService:

    def __init__(self):
        self.__editora_dao: EditoraDAO = EditoraDAO()

    @property
    def editora_dao(self) -> EditoraDAO:
        return self.__editora_dao

    def menu(self):
        print('[Editoras] Escolha uma das seguintes opções:\n'
                '1 - Listar todas as editoras\n'
                '2 - Adicionar nova editora\n'
                '3 - Excluir editora\n'
                '4 - Ver editora por Id\n'
                '5 - Importar editoras do arquivo CSV\n'
                '6 - Importar editoras do arquivo JSON\n'
                '7 - Exportar editoras para arquivo JSON\n'
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
        elif escolha == '5':
            self.inserir_csv()
        elif escolha == '6':
            self.inserir_json()
        elif escolha == '7':
            self.exportar_json()
        else:
            print('Opção inválida! Por favor, tente novamente!')

        self.menu()

    def listar(self):
        print('\nListando editoras...')

        try:
            editoras = self.__editora_dao.listar()
            if len(editoras) == 0:
                print('Nenhuma editora encontrada!')

            for editora in editoras:
                print(f'{editora.id} | {editora.nome} | {editora.endereco} | {editora.telefone}')
        except Exception as e:
            print(f'Erro ao exibir as editoras! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def adicionar(self):
        print('\nAdicionando editora...')

        try:
            nome = input('Digite o nome da editora: ')
            endereco = input('Digite o endereço da editora: ')
            telefone = input('Digite o telefone da editora: ')
            nova_editora = Editora(id, nome, endereco, telefone)

            self.__editora_dao.adicionar(nova_editora)
            print('Editora adicionada com sucesso!')
        except Exception as e:
            print(f'Erro ao inserir editora! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def remover(self):
        print('\nRemovendo editora...')

        try:
            editora_id = int(input('Digite o ID da excluir para excluir: '))
            if (self.__editora_dao.remover(editora_id)):
                print('Editora excluída com sucesso!')
            else:
                print('Editora não encontrada!')
        except Exception as e:
            print(f'Erro ao excluir editora! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def mostrar_por_id(self):
        print('\Editora por Id...')

        try:
            id = int(input('Digite o Id da editora para buscar: '))
            edt = self.__editora_dao.buscar_por_id(id)

            if edt is None:
                print('Editora não encontrada!')
            else:
                print(f'{edt.id} | {edt.nome} | {edt.endereco} | {edt.telefone}')
        except Exception as e:
            print(f'Erro ao exibir editora! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def inserir_csv(self):
        print('Inserir editoras CSV...')

        try:
            nome_arquivo = input('Digite o nome do arquivo CSV (Precisa estar na raiz do projeto): ')
            lista_editoras = editoras_csv.ler_csv_e_gera_uma_lista_de_editoras(nome_arquivo)
            self.__editora_dao.adicionar_muitos(lista_editoras)
            print('Editoras do CSV adicionados com sucesso!')
        except Exception as e:
            print(f'Erro ao inserir CSV de editoras: - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def inserir_json(self):
        print('Inserir editoras JSON...')

        try:
            nome_arquivo = input('Digite o nome do arquivo JSON (Precisa estar na raiz do projeto): ')
            lista_editoras = editoras_json.ler_json_e_gera_uma_lista_de_editoras(nome_arquivo)
            self.__editora_dao.adicionar_muitos(lista_editoras)
            print('Editoras do JSON adicionados com sucesso!')
        except Exception as e:
            print(f'Erro ao inserir JSON de editoras: - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def exportar_json(self):
        print('Exportando editoras JSON...')
        try:
            nome_arquivo = input('Digite o nome para o novo arquivo JSON (será gerado na pasta raiz do projeto): ')
            lista_de_editoras = self.__editora_dao.listar()
            editoras_json.criando_json_usando_lista_de_editoras(lista_de_editoras, nome_arquivo)
            print('JSON de editoras gerado com sucesso!')
        except Exception as e:
            print(f'Erro ao gerar JSON de editoras: {e}')
            return

        input('Pressione uma tecla para continuar...')
