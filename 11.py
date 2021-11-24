preco = int(input('Qual o valor do alimento: '))
porcentagem = int(input('Informe a porcentagem do desconto: '))
desconto = preco * porcentagem/100
novo_preco = preco - desconto
print('Preço após o desconto: {}' .format(novo_preco))