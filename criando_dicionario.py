pessoa = {
    'nome':'Luiz Otavio',
    'sobrenome':'Miranda',
    'idade': 18,
    'altura': 1.80,
    'endereço': [{'rua': 'tal tal', 'numero':123},{'rua':'outra rua','numero':321}]

}
# pessoa = dict(nome = 'Luiz Otávio',sobrenome ='Miranda'
print(pessoa['nome'])
print(pessoa['endereço'])
print()

for a in pessoa:
    print(a,pessoa[a])
