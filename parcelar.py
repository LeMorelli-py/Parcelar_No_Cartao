preco = float(input('Informe o valor das compras: R$ '))
print(''' FORMAS DE PAGAMENTO:
[1] a vista dinheiro ou cheque: 
[2] a vista cartao
[3] 2x no cartao
[4] 3x ou mais no cartao''')
opcao = int(input('Qual a opção: '))
parcelas = int(input('Quantas Parcelas: '))

if opcao == 1:
    total = preco - (preco*0.10)
    print(f'O preço R${preco:.2f} ao final com desconto será de R${total:.2f}')
elif opcao == 2:
    total = preco - (preco*0.05)
    print(f'O preço R${preco:.2f} ao final com desconto será de R${total:.2f}')
elif opcao == 3:
    total = preco
    print(f'A compra parcelada em 2x será de R${total:.2f}, sendo 2 parcelas de R${total/2:.2f}')
elif opcao == 4:
    total = preco + (preco * 0.2)
    print(f'A compra de R${preco:.2f}, parcelada em {parcelas} vezes, ficará em R${total:.2f}')