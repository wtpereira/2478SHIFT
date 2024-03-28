import csv

from model.editora import Editora
from database.conexao_factory import ConexaoFactory


def ler_csv_primeiro() -> None:
    arquivo_csv = open('editoras.csv')
    csv_reader = csv.reader(arquivo_csv, delimiter=',')
    for linha in csv_reader:
        print(linha)

    arquivo_csv.close()


def ler_csv() -> list:
    with open('editoras.csv') as arquivo_csv:
        lista_csv = list()
        csv_reader = csv.reader(arquivo_csv, delimiter=',')
        for linha in csv_reader:
            lista_csv.append(linha)

        return lista_csv


def ler_csv_e_criando_uma_lista() -> list:
    with open('editoras.csv') as arquivo_csv:
        csv_reader = csv.reader(arquivo_csv, delimiter=',')
        lista_csv = list(csv_reader)
        return lista_csv


def ler_csv_e_cria_uma_lista_de_editoras() -> list:
    with open('editoras.csv') as arquivo_csv:
        csv_reader = csv.reader(arquivo_csv, delimiter=',')
        lista_csv = list(csv_reader)

        estou_na_primeira_linha = True
        lista_editoras = list()
        for item in lista_csv:
            if estou_na_primeira_linha:  # ignorar a primeira linha do arquivo csv.
                estou_na_primeira_linha = False
            else:
                editora = Editora(nome=item[0], endereco=item[1], telefone=item[2])
                lista_editoras.append(editora)

        return lista_editoras


def ler_csv_e_gera_uma_lista_de_dict() -> list[dict]:
    with open('editoras.csv') as arquivo_csv:
        csv_reader = csv.DictReader(arquivo_csv, delimiter=',')
        list_dict_csv = list()
        for dicionario in csv_reader:
            list_dict_csv.append(dicionario)

        return list_dict_csv


def ler_csv_e_gera_uma_lista_de_editoras() -> list[dict]:
    with open('editoras.csv') as arquivo_csv:
        csv_reader = csv.DictReader(arquivo_csv, delimiter=',')
        lista_editoras = list()
        for dicionario in csv_reader:
            editora = Editora(nome=dicionario['nome'], endereco=dicionario['endereço'], telefone=dicionario['telefone'])
            lista_editoras.append(editora)

        return lista_editoras


# ********************************************************************

def criando_csv_usando_lista(lista) -> None:
    with open('novo_editoras.csv', 'w', newline='') as novo_arquivo:
        escritor = csv.writer(novo_arquivo)
        escritor.writerow(lista[0])
        escritor.writerows(lista[1:])

    print('Os dados foram salvos com sucesso!')


def criando_csv_usando_lista_de_editoras(lista_editoras) -> None:
    with open('novo_editoras.csv', 'w', newline='') as novo_arquivo:
        escritor = csv.writer(novo_arquivo)
        escritor.writerow(['nome', 'endereco', 'telefone'])
        for editora in lista_editoras:
            escritor.writerow([editora.nome, editora.endereco, editora.telefone])

    print('Os dados foram salvos com sucesso!')


"""
if __name__ == '__main__':
    minha_lista = [['nome', 'endereço', 'telefone'],
                   ['Globinho', '736 José Antônio - Sanharó, RS / 23766-854', '(69) 2859-6853'],
                   ['Maurício de Souza', '895 Itaguaçu - Nova Esperança do Sudoeste, AM / 40261-910', '(88) 1234-7895'],
                   ['Martis Fontes', '64222 João Maranhão - Miracatu, MA / 47884-229', '(11)4568-9876']]
    lista_editoras = ler_csv_e_gera_uma_lista_de_editoras()
    for editora in lista_editoras:
        print(editora)
"""


class ConexaoFactoryHandler(object):
    def __init__(self):
        self.__conexao_factory = ConexaoFactory()

    def __enter__(self):
        self.conexao = self.__conexao_factory.get_conexao()
        self.cursor = self.conexao.cursor()
        return self.cursor

    def __exit__(self, *args):
        self.cursor.close()
        self.conexao.close()
        print("Tudo fechado!!!")


if __name__ == '__main__':
    criando_csv_usando_lista_de_editoras(ler_csv_e_gera_uma_lista_de_editoras())
