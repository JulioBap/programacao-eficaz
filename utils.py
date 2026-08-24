import sqlite3


class Note:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

    @property
    def titulo(self):
        return self.title

    @property
    def detalhes(self):
        return self.content


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

    
def buscar_note(id):
    conexao = abrir_banco()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT
            id,
            title,
            content
        FROM note
        WHERE id = ?
    """, (id,))
    resultado = cursor.fetchone()
    conexao.close()

    if resultado is None:
        return None

    return Note(resultado[0], resultado[1], resultado[2])

def editar(note):
    if isinstance(note, dict):
        note_id = note["id"]
        title = note["titulo"]
        content = note["detalhes"]
    else:
        note_id = note.id
        title = note.title
        content = note.content

    conexao = abrir_banco()
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE note
        SET
            title = ?,
            content = ?
        WHERE id = ?
    """,
    (
        title,
        content,
        note_id
    ))
    conexao.commit()
    conexao.close()
