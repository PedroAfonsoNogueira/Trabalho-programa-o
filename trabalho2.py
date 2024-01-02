import re
# pedir texto
def pedir_texto():
    return input("Digite o texto: ")
# calcular quantas letras estão na frase
def calcular_numero_letras(texto):
    return len(re.findall(r'[a-zA-Z]', texto))
# calcular o numero de palavras totais
def calcular_numero_palavras(texto):
    return len(texto.split())
#calcular o numero de frases
def calcular_numero_frases(texto):
    # Determinar a forma como as frases acabam
    frases = [frase for frase in re.split(r'[.!?]', texto) if frase.strip()]
    return len(frases)
#determinar o valor de L
def calcular_L(texto):
    num_letras = calcular_numero_letras(texto)
    num_palavras = calcular_numero_palavras(texto)
    return num_letras / num_palavras
#determinar o valor de S
def calcular_S(texto):
    num_frases = calcular_numero_frases(texto)
    num_palavras = calcular_numero_palavras(texto)
    return num_frases / num_palavras
#determinar o valor de CLI
def calcular_CLI(texto):
    L = calcular_L(texto)
    S = calcular_S(texto)
    return 0.0588 * L - 0.296 * S - 15.8
#indicar o indice
def informar_indice(CLI):
    if CLI < 1:
        return "Inferior ao nível 1"
    elif CLI >= 16:
        return "Superior ao nível 16"
    else:
        return f"{CLI:.2f}"
# pedir o texto ao utilizador
texto = pedir_texto()
# determinar o CLI
CLI = calcular_CLI(texto)
# apresentar o resultado
print(f"O índice Coleman-Liau para o texto fornecido é: {calcular_CLI(texto)}")
