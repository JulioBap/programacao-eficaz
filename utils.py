import sqlite3
def abrir_banco():
    return sqlite3.connect('banco.db')


def criar_tabela():
    conexao = abrir_banco()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS note (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

criar_tabela()


def load_data():
    conexao = abrir_banco()
    cursor = conexao.cursor()

    cursor.execute("SELECT id, title, content FROM note")
    resultados = cursor.fetchall()

    conexao.close()

    dados = []

    for resultado in resultados:
        dados.append({
            'id': resultado[0],
            "titulo": resultado[1],
            "detalhes": resultado[2]
        })

    return dados


def load_template(arquivo_template):
    caminho = f"static/templates/{arquivo_template}"
    with open(caminho, encoding='utf-8') as arquivo:
        dados = arquivo.read()
        return dados


def recebe_anotacao(anotacao):
    conexao = abrir_banco()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO note (title, content) VALUES (?, ?)",
        (
            anotacao["titulo"],
            anotacao["detalhes"]
        )
    )

    conexao.commit()
    conexao.close()

def apagar_anotacao(anotacao):
    conexao = abrir_banco()
    cursor = conexao.cursor()
    cursor.execute(
        'DELETE FROM note where id = ?',
        (
            anotacao['id'],
        )
    )
    conexao.commit()
    conexao.close()