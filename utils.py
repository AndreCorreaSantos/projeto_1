from asyncio import ReadTransport
import json

def extract_route(req):
    index1 = req.index("/")
    index2 = req.index("HTTP")
    route = ""
    for i in range(index1+1,index2-1):
        route += req[i]
    return route  

def read_file(path):
    with open(path, mode="rb") as file:
        return file.read()

def load_data(name):
    path = f"data/{name}"
    with open(path) as file:
        return json.load(file)

def load_template(name):
    path = "templates/{}".format(name)
    with open(path) as file:
        return file.read()

def write_notes(notes):
    path = f"data/notes.json"
    with open(path,mode="w") as file:
        string = json.dumps(notes,ensure_ascii=False)
        file.write(string)

def build_response(body = '', code=200,reason='OK',headers=''):
    if headers == '':
        response = f"HTTP.1 {code} {reason}\n\n{body}"
    else:
        response = f"HTTP.1 {code} {reason}\n{headers}\n\n{body}"
    return response.encode()