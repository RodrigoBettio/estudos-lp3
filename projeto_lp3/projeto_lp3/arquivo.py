arquivo = open("dados.txt")
#print(arquivo) Imprime as informações do arquivo, não o conteúdo

conteudo = arquivo.read()

print(conteudo)
arquivo.close()

#bloco with--> Fecha o arquivo quando sai do bloco

with open("dados.txt", "r") as arquivo2: #passa read como argumento, é importante deixar explicito que o arquivo está em read
    print(arquivo2.read())

#readlines retornam uma lista com as linhas    
with open("dados.txt") as arquivo3: #Imprime o \n junto
    linhas =arquivo3.readlines()
    print(linhas)
     
with open("dados.txt", "r") as arquivo4: #Tira o \n
    linhas = []
    for linha in arquivo4 :
        linhas.append(linha.strip())
    print(linhas)

#abrir no modo escrita
# w --> Escreve no arquivo

#with open("dados.txt", "w") as arquivo5: #Apaga todo o arquivo e escreve Jaca
    #arquivo5.write("JACA")

#a- append - escreve no final do arquivo
with open("dados.txt", "a") as arquivo6:
    arquivo6.write("\nJACA")

#csv--> valores separados por virgula
def obter_produtos():
    with open("produtos.csv", "r") as arquivo_produtos:
        produtos = []
        for linha in arquivo_produtos:
            dados_produto = linha.strip().split(",")
            produto = {
                "nome": dados_produto[0],
                "descricao": dados_produto[1],
                "preco": float(dados_produto[2]),
                "imagem": dados_produto[3]
            }        
            produtos.append(produto)

        return(produtos)
    
print(obter_produtos())


def salvar_produto(nome, descricao, preco, imagem):
    #1. abrir o arquivo em modo append "a"
    with open("produtos.csv", "a") as arquivo_produtos:
        #2. montar a string com os dados separados por vírgula
        texto_produto = f"\n{nome},{descricao},{preco},{imagem}"
        #3. escrever a string no arquivo
        arquivo_produtos.write(texto_produto)
        
salvar_produto("Celular", "Tira foto", 5000.0, "celular.jpg")
salvar_produto("Tablet","Joga jogo",1250.0,"tablet.jpg")

    
    