#criando um set

s1 = set() #vazio
s2 = {'Luiz',1,2,3}
print(s1,s2)

#Adicionar elementos em set
s1.add('Diego')
s1.update(('Olá mundo'))
print(s1)

#clear limpa o set

#s1.clear()

#discard elimina o item a ser descartado
s1.discard(('Olá mundo'))
print(s1)

#operadores uteis
#uniao (unuion)une
#intersecção (intersection) _Itens presentes em ambos
#diferenca - Itens presentes apenas do set na esquerda
#diferenca simetrica ^ itens que nao estao em ambos
s3 = {1, 2, 3}
s4 = {2, 3, 4}
s5 = s3| s4
print(s5)
s6 = s3 & s4
print(s6)
s7 = s3 - s4
print(s7)
s8 = s3 ^ s4
print(s8)