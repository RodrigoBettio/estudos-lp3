valorCompra = float(input("Digite o valor da sua compra:"))

if valorCompra < 9.99:
    print(("Você não teve desconto :("),valorCompra)
elif valorCompra <= 99.99:
    print(("O seu desconto foi de 5% :)"),valorCompra*0.95)
elif valorCompra <= 499.99:
    print(("O seu desconto foi de 10% :)"),valorCompra*0.90)
else:
    print(("O seu desconto foi de 15% :)"), valorCompra*0.85)


#Valor entre 0 e 9,99 --> 0%
#Valor entre 10 e 99,99 --> 5%
#Valor entre 100 e 499,99 --> 10%
#Valor acima de 500,00 --> 15%