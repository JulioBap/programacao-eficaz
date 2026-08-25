from html import escape

from utils import load_data, load_template, recebe_anotacao, apagar_anotacao, buscar_note, editar as editar_note, alternar_favorito

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id=dados['id'],title=dados['titulo'], details=dados['detalhes'],favorite_icon="★" if dados["favorite"] else "")
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    dicionario = {}
    dicionario['titulo'] = titulo
    dicionario['detalhes'] = detalhes
    recebe_anotacao(dicionario)

def delete(id):
    dicionario = {}
    dicionario['id'] = id
    apagar_anotacao(dicionario)

def editar(id):
    nota = buscar_note(id)

    if nota is None:
        return load_template('components/editar.html').format(id='', title='', details='')

    return load_template('components/editar.html').format(
        id=escape(str(nota.id), quote=True),
        title=escape(nota.title, quote=True),
        details=escape(nota.content)
    )

def update(id, titulo, detalhes):
    dicionario = {}
    dicionario['id'] = id
    dicionario['titulo'] = titulo
    dicionario['detalhes'] = detalhes
    editar_note(dicionario)

def favoritar(id):
    alternar_favorito(id)