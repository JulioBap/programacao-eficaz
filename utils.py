import json
def load_data(arquivo_json):
    caminho = f"static/data/{arquivo_json}"
    with open(caminho) as arquivo:
        dados = json.load(arquivo)
        return dados


def load_template(arquivo_template):
    caminho = f"static/templates/{arquivo_template}"
    with open(caminho) as arquivo:
        dados = arquivo.read()
        return dados

def recebe_anotacao(anotacao):
    caminho = 'static/data/notes.json'
    with open(caminho) as arquivo:
        dados = json.load(arquivo)
        dados.append(anotacao)
    with open(caminho, 'w') as arquivo:
        json.dump(dados,arquivo)