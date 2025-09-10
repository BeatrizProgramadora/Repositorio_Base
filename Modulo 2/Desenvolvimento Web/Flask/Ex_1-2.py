from flask import Flask

app= Flask(__name__)

@app.route('/')
def home():

    return 'Olá mundo!'

@app.route('/sobre')
def sobre():
    return 'Olá, eu sou a Bia. Estudo programação e amo gatos.'

if __name__=='__main__':
    app.run(debug=True)