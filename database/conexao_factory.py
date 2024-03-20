import psycopg2

from settings import (
    DB_HOST,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


class ConexaoFactory:
    def get_conexao(self):
        return psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
