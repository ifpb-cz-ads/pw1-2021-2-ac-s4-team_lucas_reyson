salario = float(input('Infome seu salario atual: '))
porcen_aumen = float(input('Infome a porcentagem do aumento'))
aumento = salario * porcen_aumen / 100
novo_valor = salario + aumento 
print('O novo salario é {}'.format(novo_valor))