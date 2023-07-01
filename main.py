from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'fabricio'
#criação da classe "filme", modo primitivo de armazenar dados da lista
class filme:
    def __init__(self,nome, genero, diretor):
        self.nome = nome
        self.genero = genero
        self.diretor = diretor

#exemplos iniciais pra enriquecer visualmente a experiência de quem entra no site
avatar = filme('avatar 2: caminho do n sei oq', 'aventura/fantasia','james cameron')
joker = filme('joker','drama','todd philips')
jack = filme('o estranho mundo de jack','animação','tim burton')
ldj = filme('liga da justiça','ação','jack snider')
estomago = filme('estomago','drama','marcos jorge')
lista = [avatar,joker,jack,ldj,estomago]

@app.route('/inicio')
def inicio():
    return render_template('index.html',lista=lista)

#só pra página inicial n ficar vazia, poderia ter começado com a lista porém acho feio (não me pergunte pq)
@app.route('/')
def sla():
    return render_template('sla.html')

def vel(session):
    if session == 'verdadeiro':
        return True




#criei pela necessidade e boa prática de encapsular código
#verifica se já tem filme na lista, falso = não tem true = já tem
def verificarro(lista,novo_filme):
    for c in range(len(lista)):
        if lista[c].nome == novo_filme.nome:
            return True
    else:
        return False

@app.route('/catalogar',methods=['POST',])
def catalogar():
    nome = request.form['novo_filme']
    genero = request.form['genero']
    diretor = request.form['diretor']
    var_filme = filme(nome, genero, diretor)
    if verificarro(lista, var_filme) == False:
        lista.append(filme(nome, genero, diretor))
    
    return render_template('index.html',lista=lista)

@app.route('/verificar',methods=['POST',])
def verificar():
    senha = request.form['senha']
    nome = request.form['nome']
    if senha == 'senha' and nome == 'fabricio':
        session['usuario_logado'] = nome
        return redirect('/cadastro')
    else:
        return redirect('/login')

@app.route('/cadastro')
def cadastrar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    else:
        return render_template('cadastro_filme.html')
    
@app.route('/login')
def paglogar():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    return redirect('/inicio')

app.run(debug=True)