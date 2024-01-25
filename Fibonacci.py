# Fibonaccci definitivo


print('Sequência de Fibonacci')

termo = int(input(' Digite o termo que você gostaria de encontrar :'))
ultimo = 1
penultimo = 0
acumulador = 0
if termo == 1:
    print(f'O {termo} termo  é igual a 1 na sequência de Fibonacci')
else:
    for a in range(1, termo):
        acumulador = penultimo +ultimo
        penultimo = ultimo
        ultimo = acumulador
    print(f'O {termo}  termo é igual a {acumulador} na sequência de Fibonacci')