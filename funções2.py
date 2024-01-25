
HigherOrder
def saudacao (mensagem,nome) :
    return f'{mensagem},{nome}'

def executa (funcao,*args) :
    return funcao(*args)

a = executa(saudacao,'Bom dia','Luiz')
print(a)


Closure

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao},{nome}'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Diego','Sabrina','Nilza']:
    print(falar_bom_dia(nome))


def multiplicar(numero):
    def multiplicador(numero2):
        return numero * numero2
    return multiplicador

a = (multiplicar(2))
print(a(10))