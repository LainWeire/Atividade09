# Um motorista deseja calcular o consumo médio de combustível do seu carro. Crie um programa que receba a quantidade de quilômetros percorridos e a quantidade de litros de combustível consumidos, e calcule o consumo médio (km por litro).
km = float(input("Kms percorridos: "))
c = float(input("Combustível gasto: "))
me = ((km + c) / 2)
print (f"Média de Km por L: {me}")