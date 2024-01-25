#calculadora proposta com while
while True:
  numero1 = input('Digite um número : ')
  numero2 = input('Digite o segundo número : ')
  operador = input('Digite qual operação deseja fazer : + , - , * , / ')
  numeros_validos = None

  try:
    numero1 = float(numero1)
    numero2 = float(numero2)
    numeros_validos= True
  except:
    numeros_validos = None

  if numeros_validos is None:
    print('Um dos números digitados é inválido')
    continue
  if operador == '+':
    print(numero1 + numero2)
  elif operador == '-':
    print(numero1 - numero2)
  elif operador == '*':
    print(numero1 * numero2)
  elif operador == '/' :
    print(numero1 / numero2)
  else:
    print('Operador inválido')

  pergunta = str(input('Você deseja continuar : S/N ')).upper()
  if pergunta =='N':
    break
print('Tenha um bom dia')