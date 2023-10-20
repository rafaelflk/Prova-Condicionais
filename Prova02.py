#Escreva um programa em python que pergunte ao usuário a velocidade de um carro.
#Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
#Nesse caso, exiba o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.


velocidade_carro = int(input('Digite qual a velocidade do carro?: '))
multa_por_km = 20.00
velocidade_permitida = 80
excesso_velocidade = float(velocidade_carro % velocidade_permitida)


if velocidade_carro > velocidade_permitida:
    print('Você foi multado em: ', excesso_velocidade*multa_por_km,'R$')

else:
    print('Velocidade do carro é: ',velocidade_carro,'km/h.')
