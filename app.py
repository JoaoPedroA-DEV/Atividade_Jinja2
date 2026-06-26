from flask import Flask, jsonify, request, render_template, flash, redirect,url_for #type: ignore
import dados

biblioteca = dados.carregar_do_arquivo() 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MinhaChaveSuperSecretaeSegura123'

def encontrar_livro(isbn):
    biblioteca = dados.carregar_do_arquivo()
    for livro in biblioteca:
        if livro['isbn'] == isbn:
            print(livro)
            return livro
    return None

@app.route('/')
def hello ():
    return render_template('hello.html')
    # return "Hello, World!"

@app.route("/<nome>")
def meunome(nome=None):
    return render_template('meunome.html', nome=nome)

@app.route("/name/<nome>", methods=['GET', 'POST'])
def name(nome):
    return f"Olá, eu não sou o {nome}"

@app.route('/api/biblioteca', methods=['GET' , 'POST'])
@app.route('/api/biblioteca/<isbn>', methods=['GET', 'PUT', 'DELETE'])
def manipula_livros(isbn=None):
    if request.method == 'GET':
        if isbn:
            for l in biblioteca:
                if l['isbn'] == isbn:
                    return jsonify(l)
            return jsonify("message: livro não localizado"), 404
        else:
            return render_template('biblioteca.html',biblioteca=biblioteca)
    elif request.method == 'POST':
        novo_livro = request.get_json()
        for l in biblioteca:
            if l['isbn'] == novo_livro['isbn']:
                return jsonify("Livro já está cadastrado"), 200
        biblioteca.append(novo_livro)
        dados.salvar_no_arquivo(biblioteca)
        return jsonify("message: livro cadastrado com sucesso"), 201
    elif request.method == 'DELETE':
        for l in biblioteca:
            if l['isbn'] == isbn:
                biblioteca.remove(l)
                dados.salvar_no_arquivo(biblioteca)
                return jsonify("mensagem: livro deletado com sucesso"), 200
        return jsonify("message: livro não localizado"), 404
    elif request.method == 'PUT':
        alteracoes = request.get_json()
        for livro in biblioteca:
            if livro['isbn'] == isbn:
                for key, value in alteracoes.items():
                    livro[key] = value
                dados.salvar_no_arquivo(biblioteca)
                return jsonify("mensagem: livro alterado com sucesso"), 200
        return jsonify("message: livro não localizado"), 404
    else:
        return 'Solicitação não aceita', 503

# Rotas da Interface Web para a Biblioteca
@app.route('/biblioteca', methods=['GET', 'POST'])
def interface_web():
    """ Função para gerenciamento via interface web
    """
    biblioteca = dados.carregar_do_arquivo()
    return render_template('biblioteca.html', biblioteca=biblioteca)

@app.route('/biblioteca/criar', methods=['GET','POST'])
def cria_livro():
    if request.method == 'POST':
        novo_livro = {
                    'isbn': request.form.get('isbn'),
                    'titulo': request.form.get('titulo'),
                    'autor': request.form.get('autor'),
                    'genero': request.form.get('genero'),
                    'ano_publicacao': request.form.get('ano_publicacao'),
                    'editora': request.form.get('editora'),
                    'paginas': request.form.get('paginas'),
                    'status': request.form.get('status'),
                    'localizacao': request.form.get('localizacao')
                }
        for l in biblioteca:
            if l['isbn'] == novo_livro['isbn']:
                return jsonify("Livro já está cadastrado"), 200
        biblioteca.append(novo_livro)
        dados.salvar_no_arquivo(biblioteca)
        return render_template('biblioteca.html', biblioteca=biblioteca)
    else:
        return render_template('criar_livro.html')

@app.route('/biblioteca/excluir/<isbn>', methods=['POST'])
def excluir_livro(isbn):
    biblioteca = dados.carregar_do_arquivo()
    biblioteca = [livro for livro in biblioteca if livro['isbn'] != isbn]
    flash(f'Livro com ISBN {isbn} foi removido com sucesso!')
    dados.salvar_no_arquivo(biblioteca)
    return redirect(url_for('interface_web'))

@app.route('/biblioteca/atualizar', methods=['GET', 'POST'])
def atualiza_livro():
    biblioteca = dados.carregar_do_arquivo()
    livro = encontrar_livro(request.args.get('isbn'))
    if request.method == 'POST':
        atualizado = {
            'isbn': request.args.get('isbn'),
            'titulo': request.form.get('titulo'),
            'autor': request.form.get('autor'),
            "genero": request.form.get('genero'),
            "ano_publicacao": request.form.get('ano_publicacao'),
            "editora": request.form.get('editora'),
            "paginas": request.form.get('paginas'),
            "status": request.form.get('status'),
            "localizacao": request.form.get('localizacao')
        }
        if livro:
            biblioteca.remove(livro)
            biblioteca.append(atualizado)
            dados.salvar_no_arquivo(biblioteca)
        return redirect(url_for('lista_livros'))
    else:
        if livro:
            return render_template('atualizar_livro.html', livro=livro)
if __name__ == '__main__' :
    app.run(debug=True)