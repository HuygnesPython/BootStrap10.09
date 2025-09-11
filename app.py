from turtle import title
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def PagInicial():
    title = 'Página inicial'
    return render_template('index.html', title=title)
@app.route('/atividade')
def atividade():
    title = 'Atividade'
    return render_template('atividade.html', title=title)
@app.route('/atividade2')
def atividade2():
    title = 'Atividade 2'
    return render_template('atividade2.html', title=title)


app.run(debug=True)