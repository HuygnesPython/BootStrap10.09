from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/PagInicial')
def PagInicial():
    titulo = 'Página inicial'
    return render_template('index.html', titulo = titulo)

app.run(debug=True)