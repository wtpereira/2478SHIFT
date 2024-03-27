import csv
from pathlib import Path

from model.editora import Editora


def caminho_completo(nome_arquivo_csv):
    return f'{str(Path().absolute())}/{nome_arquivo_csv}.csv'


def ler_csv(nome_arquivo_csv: str) -> list:
    with open(caminho_completo(nome_arquivo_csv)) as arquivo_csv:
        lista_csv = list()
        csv_reader = csv.reader(arquivo_csv, delimiter=',')
        for linha in csv_reader:
            lista_csv.append(linha)

        return lista_csv


def ler_csv_e_gera_uma_lista_de_editoras(nome_arquivo_csv: str) -> list[dict]:
    with open(caminho_completo(nome_arquivo_csv)) as arquivo_csv:
        csv_reader = csv.DictReader(arquivo_csv, delimiter=',')
        lista_editoras = list()
        for dicionario in csv_reader:
            editora = Editora(nome=dicionario['nome'], endereco=dicionario['endereço'], telefone=dicionario['telefone'])
            lista_editoras.append(editora)

        return lista_editoras


if __name__ == '__main__':
    print(ler_csv('editoras'))
