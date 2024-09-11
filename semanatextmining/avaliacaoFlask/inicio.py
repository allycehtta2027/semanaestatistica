from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Estilo do Rei Barbearia"

@app.route('/novofuncionario')
def novo_funcionario():
    return "Página para adicionar um novo funcionário"

@app.route('/novocliente')
def novo_cliente():
    return "Página para adicionar um novo cliente"

@app.route('/novoservico')
def novo_servico():
    return "criar novo serviço"

@app.route('/novoagendamento')
def novo_agendamento():
    return "Criar novo usuario"

@app.route('/login')
def login():
    return "Página de login"

@app.route('/logout')
def logout():
    return "Logout efetuado com sucesso"

app.run (debug=True)