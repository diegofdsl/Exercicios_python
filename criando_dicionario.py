pessoa = {
    'nome':'Luiz Otavio',
    'sobrenome':'Miranda',
    'idade': 18,
    'altura': 1.80,
    'endereço': [{'rua': 'tal tal', 'numero':123},{'rua':'outra rua','numero':321}]}

# #Quantas chaves
# print(len(pessoa))
# #Mostrar as chaves
# print(pessoa.keys())
# #mostrar valores
# print(pessoa.values())
# #mostrar chaves e valores correspondentes
# print(pessoa.items())
# # Pra verificar se a chave existe
# print(pessoa.get('sobrenome','Nao existe essa chave'))
# if pessoa.get('sobrenome') is None:
#     print('Não Existe')
# else:
#     print('Existe')

#shallow copy

d1={'c1':1,
    'c2':2
}

print(d1)
d2 = d1
d2['c1']= 1000
print(d1)
print(d2)

#metodo copy
e1 = {'e1':1,
      'e2':2,
      }
e2=e1.copy()
e2['e2']=10
print(e1)
print(e2)


# }
# # pessoa = dict(nome = 'Luiz Otávio',sobrenome ='Miranda'
# print(pessoa['nome'])
# print(pessoa['endereço'])
# print()
#
# for a in pessoa:
#     print(a, pessoa[a])
# pessoa ={}
#
# chave = 'nome_completo'
# pessoa[chave] = ' Diego '
# print(pessoa[chave])
# print(pessoa)




