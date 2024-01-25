#letra mais frequente
frase = 'O brasil tem muitos rios e mares'
i = 0
letra = []
quantas_vezes = 0
qtd_maisvezes=0
letra_maisvezes=''
while i < len(frase):
    letra = frase[i]
    if letra ==' ':
        i+=1
        continue

    quantas_vezes = frase.count(letra)
    if qtd_maisvezes < quantas_vezes:
        qtd_maisvezes = quantas_vezes
        letra_maisvezes = letra
    i+=1
print(f'A letra que mais apareceu foi  "{letra_maisvezes}" que apareceu {qtd_maisvezes}')
