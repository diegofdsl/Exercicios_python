#desafio 56
#url=https://www.youtube.com/watch?v=fokDF4th0IY
mediadeidade=0
nomedohomemmaisvelho=''
mulheresmenosde20=0
maioridadehomem=0
mulheresdemaisde20=0
for pessoas in range (1,5):
  nome =input(str('Digite o nome da pessoa : '))
  idade=int(input('Digite a idade da pessoa: '))
  sexo =str(input('Digite o Sexo H / M '))
  sexo=sexo.upper()
  mediadeidade=mediadeidade +idade/4
  if sexo=='H'  and idade>maioridadehomem:
    nomedohomemmaisvelho=nome
    maioridadehomem=idade
  elif sexo=='M'and idade<20:
                 mulheresmenosde20=mulheresmenosde20+1
  elif sexo=='M' and idade>20:
    mulheresdemaisde20=mulheresdemaisde20 +1

print(f'A média de idade é {mediadeidade}')
print(f'O nome do homem mais velho é {nomedohomemmaisvelho}')
print(f'Ha {mulheresmenosde20} mulheres com menos de 20')
