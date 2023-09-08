from flask import Flask, render_template, request, session,redirect
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@127.0.0.1/filmesteca'
db = SQLAlchemy(app)

app.secret_key = 'fabricio'



class filmes(db.Model):
    nome = db.Column(db.String(100), primary_key=True, nullable=False)
    gênero = db.Column(db.String(60),nullable=False)
    diretor = db.Column(db.String(60),nullable=False)
    ano = db.Column(db.Integer)

    def __repr__(self):
        return '<Name %r>' % self.name


@app.route('/inicio')
def inicio():
    lista = filmes.query.all()
    return render_template('index.html',lista=lista)

#só pra página inicial n ficar vazia, poderia ter começado com a lista porém acho feio (não me pergunte pq)
@app.route('/')
def sla():
    return render_template('inicio.html')




@app.route('/catalogar',methods=['POST',])
def catalogar():
    nome = request.form.get('nome_cadastro')
    genero = request.form.get('genero_cadastro')
    diretor = request.form.get('diretor_cadastro')
    ano = request.form.get('ano_cadastro')

    #procure no banco de dados o primeiro item com o nome igual ao fornecido no form (nome=nome). Se houver não faça nada, se não houver adicione
    if filmes.query.filter_by(nome=nome).first():
        return redirect('/inicio')
    else:
        var_filme = filmes(nome=nome, gênero=genero, diretor=diretor, ano=ano)
        db.session.add(var_filme)
        db.session.commit()
    
    lista = filmes.query.all()
    return render_template('index.html',lista=lista)


#meramente redireciona para cadastro_filme.html
@app.route('/cadastro')
def cadastrar():
        return render_template('cadastro_filme.html')
    

#garante que o "app.run" só será rodado se aberta neste arquivo
if __name__ == "__main__":
    app.run()


