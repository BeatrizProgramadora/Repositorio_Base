from flask import Flask

app= Flask(__name__)

@app.route('/')
def home():

    return 'Olá mundo!'

@app.route('/sobre')
def sobre():
    return 'Olá, eu sou a Bia. Estudo programação e amo gatos.'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f'Olá,{nome}!Tudo bem?'

@app.route('/dobro/<int:numero>')
def dobro(numero):
    return f'o dobro de {numero} é {2*numero}'



if __name__=='__main__':
    app.run(debug=True)