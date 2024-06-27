from flask import Flask, render_template, request
from validate_docbr import CPF, CNPJ


app = Flask(__name__)

# rota + função

# / - home page
@app.route("/")
def home():
    return render_template ("home.html")


# /contato - pagina de contato 
@app.route("/contato")
def contato():
    return render_template ("contato.html")

lista_produtos = [
        {"nome": "Coquinha", "desc": "Suco é melhor"},
        {"nome": "Doritos", "desc": "Suja a mao"},
        {"nome": "Sneakers", "desc": "Eca"}
    ]
# /produtos - pagina produtos 
@app.route("/produtos")
def produtos():
    return render_template ("produtos.html", produtos=lista_produtos)

@app.route("/cadastro")
def cadastro_produtos():
    print(lista_produtos)
    return render_template("cadastro_produto.html")

@app.route("/cnpj")
def cnpj():
    cnpj = CNPJ()
    cnpj_gerado = cnpj.generate(True)  # Gera CNPJ com máscara
    return render_template("cnpj.html", cnpj = cnpj_gerado)

@app.route("/cpf")
def cpf():
    cpf = CPF()
    cpf_gerado = cpf.generate(True)  # Gera CPF com máscara
    return render_template("cpf.html", cpf = cpf_gerado)

#Get para obter o formulário 
@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro_produto.html")

@app.route("/produtos", methods=['POST'])
def salvar_produto():
    nome = request.form['nome'] 
    descricao = request.form['descricao']
    produto = {"nome": nome, "descricao": descricao}
    lista_produtos.append(produto)

    return render_template("produtos.html", produtos = lista_produtos)

@app.route("/termos")
def termos():
    return render_template("termos.html")

@app.route("/politica")
def politica():
    return render_template("politica.html")

@app.route("/comousar")
def como_usar():
    return render_template("como_usar.html")

app.run(debug=True)
