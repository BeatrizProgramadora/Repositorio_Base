from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('Ex_2-1.html')

@app.route('/sobre')
def sobre():
    return "Olá, sou a Bia,estudo programação e amo gatos!"


if __name__== '__main__':
    app.run(debug=True)
