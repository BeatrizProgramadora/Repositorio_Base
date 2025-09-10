from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('Ex_2-2.html')

@app.route('/sobre')
def sobre():
    return "Olá, sou a Bia,estudo programação e amo gatos!"

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f'Ola {nome}'

@app.route('/dobro/<int:numero>')
def dobro(numero):
    return f'O dobro de {numero} é {numero*2}'

if __name__== '__main__':
    app.run(debug=True)

