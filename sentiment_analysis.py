def analisar_sentimento(comentario):
    palavras_positivas = ["bom", "ótimo", "excelente", "maravilhoso", "gostei", "incrível"]
    palavras_negativas = ["ruim", "péssimo", "horrível", "terrível", "odeio"]
    palavras_neutras = ["mas", "deixou", "apesar", "embora"]

    cont_positivas = 0
    cont_negativas = 0
    cont_neutras = 0

    palavras = comentario.lower().split()

    for palavra in palavras:
        if palavra in palavras_positivas:
            cont_positivas += 1
        elif palavra in palavras_negativas:
            cont_negativas += 1
        elif palavra in palavras_neutras:
            cont_neutras += 1

    if cont_positivas > cont_negativas:
        sentimento = "Positivo"
    elif cont_negativas > cont_positivas:
        sentimento = "Negativo"
    else:
        sentimento = "Neutro"

    return sentimento

# Exemplo 
if __name__ == "__main__":
    comentario = input("Digite seu comentário: ")
    sentimento = analisar_sentimento(comentario)
    print(f"Sentimento: {sentimento}")
