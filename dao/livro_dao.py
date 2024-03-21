from database.conexao_factory import ConexaoFactory
from model.livro import Livro

from dao.autor_dao import AutorDAO
from dao.categoria_dao import CategoriaDAO
from dao.editora_dao import EditoraDAO


class LivroDAO:

    def __init__(self):
        self.__conexao_factory = ConexaoFactory()
        self.__autor_dao: AutorDAO = AutorDAO()
        self.__categoria_dao: CategoriaDAO = CategoriaDAO()
        self.__editora_dao: EditoraDAO = EditoraDAO()
        self.__livros: list[Livro] = list()

    def listar(self) -> list[Livro]:
        livros = list()
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, titulo, resumo, ano, paginas, isbn, categoria_id, editora_id, autor_id FROM livros")
        resultados = cursor.fetchall()
        for resultado in resultados:
            cat = self.__categoria_dao.buscar_por_id(resultado[6])
            edt = self.__editora_dao.buscar_por_id(resultado[7])
            aut = self.__autor_dao.buscar_por_id(resultado[8])

            livro = Livro(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], cat, edt, aut)
            livros.append(livro)
        cursor.close()
        conexao.close()

        return livros

    def adicionar(self, livro: Livro) -> None:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO livros (titulo, resumo, ano, paginas, isbn, categoria_id, editora_id, autor_id) VALUES (%(titulo)s, %(resumo)s, %(ano)s, %(paginas)s, %(isbn)s, %(categoria_id)s, %(editora_id)s, %(autor_id)s)",
            ({'titulo': livro.titulo, 'resumo': livro.resumo, 'ano': livro.ano, 'paginas': livro.paginas, 'isbn': livro.isbn, 'categoria_id': livro.categoria.id, 'editora_id': livro.editora.id, 'autor_id': livro.autor.id, })
        )
        conexao.commit()
        cursor.close()
        conexao.close()

    def remover(self, livro_id: int) -> bool:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM livros WHERE id = {livro_id}")
        livros_removidos = cursor.rowcount
        conexao.commit()
        cursor.close()
        conexao.close()

        if livros_removidos == 0:
            return False

        return True

    def buscar_por_id(self, livro_id) -> Livro:
        livro = None
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT id, titulo, resumo, ano, paginas, isbn, categoria_id, editora_id, autor_id FROM livros WHERE id = {livro_id}")
        resultado = cursor.fetchone()
        if resultado:
            cat = self.__categoria_dao.buscar_por_id(resultado[6])
            edt = self.__editora_dao.buscar_por_id(resultado[7])
            aut = self.__autor_dao.buscar_por_id(resultado[8])

            livro = Livro(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5])
            livro.categoria = cat
            livro.editora = edt
            livro.autor = aut

        cursor.close()
        conexao.close()

        return livro
