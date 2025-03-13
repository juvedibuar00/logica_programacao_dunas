# importanto flask
from flask import Flask, render_template, request, redirect, url_for

# Criação de uma instância do Flask
app = Flask(__name__)

# Definição de uma rota
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html')
# Rodar o servidor
if __name__ == '__main__':
    app.run(debug=True)