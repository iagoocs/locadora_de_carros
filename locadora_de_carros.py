import os

carros = [
    ('chevrolet Onix', 90),
    ('chevrolet Spin', 150),
    ('Hyundai HB20', 85),
    ('Hyundai Tucson', 120),
    ('Fiat Uno', 60),
    ('Fiat Mobi', 70),
    ('Fiat Pulse', 130)
    ]

alugados = []

def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print('[{}] {} - R$ {} /dia.'.format(i, car[0], car[1]))

mostrar_lista_de_carros(carros)

while True:
    
    os.system("cls")
    print('=======')
    print('Bem-vindo a locadora de carros.')
    print('=======')
    print('O que deseja fazer?')
    print('0 - Mostrar portfolio | 1 - Alugar veiculos | 2 - Devolver veiculo')
    
    ds = int(input())

    os.system('cls')
    if ds == 0:
        print(mostrar_lista_de_carros(carros))
    elif ds == 1:
        print(mostrar_lista_de_carros(carros))
        print('=========')
        print('Qual carro deseja alugar?')
        buy_car = int(input())
        print('Quantos dias deseja alugar?')
        dias = int(input())
        os.system('cls')
        print('Voce esta alugando o {} por {} dias.'.format(carros[buy_car][0], dias))
        print('O aluguel totalizaria R$ {}. Deseja alugar?'.format(dias * carros[buy_car][1]))
        print('')
        print('0 - SIM | 1 - NAO')
        confirm = int(input())

        if confirm == 0:
            print('')
            print('PARABENS! Voce alugou o {} por {} dias.'.format(carros[buy_car][0], dias))
            alugados.append(carros.pop(buy_car))

    elif ds == 2:
        print(mostrar_lista_de_carros(alugados))
        print('')
        print('Qual carro deseja devolver?')
        devolver = int(input())
        os.system('cls')
        print('Voce quer devolver o {} ?'.format(alugados[devolver][0]))
        print('0 - SIM | 1 - NAO')
        confirm_devolver = int(input())

        if confirm_devolver == 0:
            print('PARABENS! Voce devolveu o {}'.format(alugados[devolver][0]))
            carros.append(alugados.pop(devolver))


    print('')
    print('==========')
    print('0 Para continuar | 1 Para sair')
    if float(input()) == 1:
        break
