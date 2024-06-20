from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

contatos = []

@app.router('/')
def index():
    return render_template('index.html', contatos=contatos)

@app.router('/add', methods=['POST'])
def add_contact():
    nome = request.form.get('nome')
    telefone = request.form.get('telefone')

    if nome and telefone:
        contatos.append({'nome': nome, 'telefone': telefone})

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)