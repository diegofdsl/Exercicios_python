#jogo da palavra secreta


palavra = 'Brasil'
letras_acertadas =''
numero_tentativas = 0
while True:
  letra = str(input('Digite uma letra : '))
  numero_tentativas +=1

  if letra == 'b':
    letra = letra.upper()

  if letra in palavra:
    letras_acertadas +=letra

  palavra_formada = ''

  for a in palavra:
    if a in letras_acertadas:
      palavra_formada += a
    else:
      palavra_formada+='*'
  print(palavra_formada)

  if palavra_formada == palavra:
    print('Parabéns,você acertou')
    print(f'Levou {numero_tentativas} tentativas para conseguir')
    break
