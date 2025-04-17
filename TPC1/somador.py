import sys

# Inicializar a soma e o estado do somador.
soma = 0
ligado = True

for linha in sys.stdin:
    print(linha, end="")

     # Dividir a linha em palavras.
    palavras = linha.split()
    
    for palavra in palavras:
        if palavra.lower() == "off": # encontra string off desliga o somador
            ligado = False
        elif palavra.lower() == "on": # encontra string on liga o somador
            ligado = True
        elif "=" in palavra:
            print(f">> {int(soma)}") # imprime a soma atual
        else:
            if ligado:
                numero = ''
                for c in palavra:
                    if c.isdigit():
                        numero += c
                    else:
                        if numero != '':
                            soma += int(numero)
                            numero = ''
                if numero != '':
                    soma += int(numero)

# imprime a soma final
print(f">> {int(soma)}")
