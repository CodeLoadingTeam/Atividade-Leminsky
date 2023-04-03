cadeiaObjv = "lfa"
scaner = input("Digite a cadeia: ")
posicao = 0
contador = 0

for passos in scaner:
    if passos == 'l':
        posicao = 1
    
    elif posicao == 1 and passos == 'f':
        posicao = 2
    
    elif posicao == 2 and passos == 'a':
        posicao = 3
        contador += 1
    
    else:
        posicao = 0

    print(passos, ' ' , posicao)

    if posicao == 3:
        posicao = 0

if contador>0:
    print(f"Cadeia localizada! ({contador} vezes)")
else:
    print("Não existe!")
