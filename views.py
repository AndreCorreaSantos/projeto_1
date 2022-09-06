from distutils.command.build import build
import urllib
from utils import *
from database import Note
def index(request,db):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    resp = build_response()
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados 
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        lista_split = corpo.split("&")
        for chave_valor in lista_split:
            index = chave_valor.index("=")
            chave = chave_valor[0:index]
            valor = chave_valor[index+1:len(chave_valor)]
            params[chave] = urllib.parse.unquote_plus(valor)
        try:
            if params["option"] == "1":
                newNote = Note(title=params["titulo"],content=params["detalhes"],id=params["id"])
                db.add(newNote)
            if params["option"] == "2":
                newNote = Note(title=params["titulo"],content=params["detalhes"],id=params["id"])
                db.update(newNote)
            if params["option"] == "3":
                db.delete(params["id"])
        except:
                newNote = Note(title=params["titulo"],content=params["detalhes"],id=params["id"])
                db.add(newNote)
        
        # notes = load_data("notes.json")
        # notes.append(params)
        # write_notes(notes)

        resp = build_response(code=303, reason='See Other', headers='Location: /')

    note_template = load_template('components/note.html')
    notes = db.get_all()
    notes_li = [ note_template.format(title=note.title, details=note.content,id = note.id) for note in notes]
    notes = '\n'.join(notes_li)


    return resp+load_template('index.html').format(notes=notes).encode()

    # O RESTO DO CÓDIGO DA FUNÇÃO index CONTINUA DAQUI PARA BAIXO...