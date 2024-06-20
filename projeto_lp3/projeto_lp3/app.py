from flask import Flask, render_template
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


# /produtos - pagina produtos 
@app.route("/produtos")
def produtos():

    lista_produtos = [
        {"nome": "Coquinha", "desc": "Suco é melhor"},
        {"nome": "Doritos", "desc": "Suja a mao"},
        {"nome": "Sneakers", "desc": "Eca"}
    ]

    return render_template ("produtos.html", produtos=lista_produtos)

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

app.run(debug=True)
