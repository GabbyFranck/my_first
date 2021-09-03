'''
Um programa que simule o fucionamento de um caixa Eletonico
'''
print('=' * 40)
print('{:^30}'.format('BANCO DO BRASIL'))
print('=' * 40)
valor = int(input('Que valor voce quer sacar? R$ '))
total = valor
cedular = 50
totced = 0
while True:
    if total >= cedular:
        total -= cedular
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${cedular}')
        if cedular == 50:
            cedular = 20
        elif cedular == 20:
            cedular = 10
        elif cedular == 10:
            cedular = 1
        elif cedular == 2:
            cedular = 1
        totced = 0
        if total == 0:
            break
print('=' * 40)
print("Volte sempre ao BANCO DO BRASIL ATE MAIS!!!")
print('=' * 40)