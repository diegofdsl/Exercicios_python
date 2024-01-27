perguntas =[{
    'Pergunta':'Quanto é 2+2:',
    'Opcoes':['1','3','4','5'],
    'Resposta':'4',
},{'Pergunta':'Quanto é 5*5:',
   'Opcoes':['25','55','10','51'],
   'Resposta':'25',},{
    'Pergunta':'Quanto é 10/2:',
    'Opcoes':['4','5','2','1'],
    'Resposta':'5',}]

#Acessando cada item dentro do dicionario
# for chave in perguntas:
#     for a in chave:
#         for b in a:
#             print(b)
acertos =0
for pergunta in perguntas:
    print(pergunta['Pergunta'])
    opcoes = pergunta['Opcoes']
    for i,opcao in enumerate(opcoes):
        print(f'{i})',opcao)
    print()
    escolha =str(input('Escolha uma opcao : '))

    acertou = False
    qtd_opcoes =len(opcoes)


    if escolha == pergunta['Resposta']:
        print('Acertou')
        acertos +=1
    else:
        print('Errou')
print(f'Você acertou {acertos}, Parabéns!!!')
