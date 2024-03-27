import json
from pathlib import Path

from model.editora import Editora


def caminho_completo(nome_arquivo_json):
    return f'{str(Path().absolute())}/{nome_arquivo_json}.json'


def ler_json(nome_arquivo_json) -> list[dict]:
    with (open(caminho_completo(nome_arquivo_json))) as arquivo_json:
        dados = json.load(arquivo_json)
        return dados


def ler_json_e_gera_uma_lista_de_editoras(nome_arquivo_json) -> list[Editora]:
    lista_editoras = list()
    with (open(caminho_completo(nome_arquivo_json))) as arquivo_json:
        dados = json.load(arquivo_json)
        for dicionario in dados:
            editora = Editora(nome=dicionario['nome'], endereco=dicionario['endereco'], telefone=dicionario['telefone'])
            lista_editoras.append(editora)

    return lista_editoras


def criando_json_usando_lista_de_dict(lista_dict, nome_novo_arquivo) -> None:
    with open(caminho_completo(nome_novo_arquivo), 'w', newline='') as novo_arquivo:
        json.dump(lista_dict, novo_arquivo, ensure_ascii=False, indent=4)

    print('Os dados foram carregados com sucesso!')


def criando_json_usando_lista_de_editoras(lista_editoras, nome_novo_arquivo) -> None:
    with open(caminho_completo(nome_novo_arquivo), 'w', newline='') as novo_arquivo:
        editoras_dict = list()
        for editora in lista_editoras:
            editoras_dict.append(editora.dump())

        json.dump(editoras_dict, novo_arquivo, ensure_ascii=False, indent=4)

    print('Os dados foram carregados com sucesso!')


if __name__ == '__main__':
    print(ler_json('editoras'))
    """
    lista_editoras = ler_json_e_gera_uma_lista_de_editoras('editoras')
    for edt in lista_editoras:
        print(f'{edt.nome} | {edt.endereco} | {edt.telefone}')
    lista_dict = ler_json('editoras')
    criando_json_usando_lista_de_dict(lista_dict, 'novo_arquivo_json')
    """
    lista_editoras = ler_json_e_gera_uma_lista_de_editoras('editoras')
    criando_json_usando_lista_de_editoras(lista_editoras, 'novo_arquivo_json')
