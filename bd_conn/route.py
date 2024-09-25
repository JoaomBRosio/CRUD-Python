# ESTE ARQUIVO É COMO SE FOSSE UM CONTROLLER

from flask import Flask, render_template, request, redirect, url_for, session
# aqui eu digo quais funções eu usarei do meu mmodel
from models import buscar_usuario, criar_banco, cadastrar_usuario, editar_usuario, verificar_login

app = Flask(__name__)
app.secret_key = 'chave_secreta'

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        # pega os dados do formulário
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
         # chama a função para editar o usuário no banco
        editar_usuario(id, nome, email, senha)
        
        # atualizando o nome do usuário na sessão
        if 'usuario_id' in session and session['usuario_id'] == id:
            session['usuario'] = nome  # pega o novo nome na sessão

        return redirect(url_for('dashboard'))

    # se for GET, tenta buscar para automaticamente preencher o formulário
    usuario = buscar_usuario(id)
    return render_template('editar.html', usuario=usuario)


# caminho do login
@app.route('/')
def login():
    return render_template('login.html')

# isso é rota para autenticação de login
@app.route('/autenticar', methods=['POST'])
def autenticar():
    email = request.form['email']
    senha = request.form['senha']
    usuario = verificar_login(email, senha)
    if usuario:
        session['usuario'] = usuario[1]
        session['usuario_id'] = usuario[0]
        return redirect(url_for('dashboard'))
    else:
        return 'Login falhou!'

# isso é rota para quando o usuario quiser se cadastrar
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        cadastrar_usuario(nome, email, senha)
        return redirect(url_for('login'))
    return render_template('cadastro.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    session.pop('usuario_id', None)
    return redirect(url_for('login'))

# isso é rota que leva para o que vem depois do login
@app.route('/dashboard')
def dashboard():
    if 'usuario' in session:
        return render_template('dashboard.html', usuario=session['usuario'], usuario_id=session['usuario_id'])
    return redirect(url_for('login'))

if __name__ == '__main__':
    criar_banco()
    app.run(debug=True)
