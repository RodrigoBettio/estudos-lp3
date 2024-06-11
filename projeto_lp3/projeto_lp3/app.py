from flask import Flask

app = Flask("Minha Aplicação")

#Página home - home - /
#@ É o decorator
@app.route("/") #Define a rota / como identificador da def home
def home():
    return "<h1> Home Page </h1>"

#Página contato - /contato (Rotas)
@app.route("/contato")
def contato():
    return "<h1> Contato </h1>"

#Página produtos - /produtos (Rotas)
@app.route("/produtos")
def produtos():
    return "<h1> Produtos </h1>"