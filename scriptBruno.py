# identificador da cadeia 'LFA'

ESTADO_INICIAL = 0
CADEIA_ESPERADA = 'LFA'

ESTADOS = {
    'L': 0,
    'F': 1,
    'A': 2
}

estadoAtual=0
contador=0

cadeia = input("Digite a cadeia: ")

for c in cadeia.upper():

    if c in CADEIA_ESPERADA:

        if ESTADOS[c] != estadoAtual:
            estadoAtual = ESTADO_INICIAL

        if estadoAtual == 0 and c == 'L':
            estadoAtual = 1

        elif estadoAtual == 1 and c == 'F':
            estadoAtual = 2

        elif estadoAtual == 2 and c == 'A':
            estadoAtual = 3

    else:
        estadoAtual = ESTADO_INICIAL


    print(c," ",estadoAtual)

    if estadoAtual == 3:
        contador += 1
        estadoAtual = ESTADO_INICIAL

    
print()


if contador > 0:
    print(f"Cadeia localizada! ({contador} vezes)")
else:
    print("Cadeia não encontrada")
