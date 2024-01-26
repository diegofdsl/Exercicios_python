lista1 = [1,2,3,4]
lista2 = [10,20,12,25]
lista3 = [5,2,10,20]
acertos = 0
while True:
    resposta_1 =int(input('Quanto é 2+2 ? \n'
                      '1,2,3,4:\n'))
    if resposta_1 in lista1:
        if resposta_1 == 4:
            print('Você acertou\n'
                  'Parabéns!!!')
            acertos+=1
        else:
            print('Resposta errada')
    print()
    resposta_2=int(input('Quanto é 5*5 \n'
                         '10,20,12,25:\n'))
    if resposta_2 in lista2:
        if resposta_2 ==25:
            print('Você acertou\n'
              'Parabéns!!!')
            acertos+=1
        else:
            print('Resposta errada')
    print()

    resposta_3 = int(input('Quanto é 10/2\n'
                           '5,2,10,20\n'))

    if resposta_3 in lista3:
        if resposta_3 == 5:
            print('Você acertou\n''Parabéns!!!')
            acertos+=1
        else:
            print('Resposta errada')

    if resposta_1 not in lista1 or resposta_2 not in lista2 or resposta_3 not in lista3:
        print('Faça somente escolhas válidas')
        break
print(f'Você acertou {acertos} de 3 questões')



