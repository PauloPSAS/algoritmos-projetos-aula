# Função para separar as sílabas de acordo com a língua
def separa_silabas(value):

    # Lib responsável pela separação de sílabas
    import pyphen

    dic = pyphen.Pyphen(lang='pt_BR')
    resultado = dic.inserted(value)
    resultado = resultado.split()

    # Já retorna o texto separando as sílabas por '-'
    return resultado

# Função responsável pela codificação do texto
def codificaP(value):

    # Chama função para separar as sílabas
    result = separa_silabas(value)

    # variável que vai receber as sílabas codificadas
    novoResultado = list()

    # Para cada sílaba na variável 'result'
    for silaba in result:

        # Se tiver '-' executa:
        if '-' in silaba:

            # troca o '-' por um 'pe' + o ultimo caractere da sílaba
            novaSilaba = silaba.replace("-", "pe" + silaba[-1])

            # Adiciona a nova lista
            novoResultado.append(novaSilaba)

        # Se não tiver '-' executa:
        else:

            # Adiciona a sílaba correspondente a nova lista
            novoResultado.append(silaba)

    # Junta todas as novas sílabas por um ' ' (espaço)
    novoResultado = ' '.join(novoResultado)

    return novoResultado

# Função responsável pela decodificação do texto
def decodificaP(value):

    # Separa as frases no ' ' (espaço)
    value = value.split()

    nResult = []

    # Para cada frase no texto splitado
    for frase in value:

        # se têm 'pe' + último caractere da frase executa:
        if 'pe' + frase[-1] in frase:

            # Remove a codificação da frase e adiciona a uma nova lista
            nSilaba = frase.replace("pe" + frase[-1], '')
            nResult.append(nSilaba)

        # Se não têm 'pe' + último caractere da frase executa:
        else:
            nResult.append(frase)

    # Junta tudo em uma única string
    nResult = ' '.join(nResult)
    return nResult

# função principal
def main():

    # Enquanto você não digitar '3' ou escrever 'tre's:
    while True:
        print("\n\n1 (Um) - para codificar\n")
        print("2 - (Dois) para decodificar\n")
        print("3 - (Três) para encerrar\n\n")

        # Escolha uma opção correspondente
        opc = input("Escolha sua opção: ").lower()

        # Se você escolher '1' ou 'um', codifique
        if opc in 'um' or opc == '1':

            frase = input("\nDigite o texto para seu amado(a): ")
            print("\n\nSeu texto codificado é: \n\n")

            # Chama função para codificar o código e retorna ela codificada
            fraseCod = codificaP(frase)

            # Exibe a frase codificada
            print(fraseCod)

        # Se você escolher '2' ou 'dois', decodifique
        elif opc in 'dois' or opc == '2':

            frase = input("\nDigite a frase codificada: ")
            print("\n\nSeu texto decodificado é: \n\n")

            # Chama a função para decodificar o código e retornar ela decodificada
            fraseDecod = decodificaP(frase)
            
            # Exibe a frase decodificada
            print(fraseDecod)

        # Se você escolher '3' ou 'tres', encerra o programa
        elif opc == '3' or opc in 'tres':
            print("\nEncerrando o programa.")
            break
        
        # Se nenhuma opção for correspondente tenta novamente
        else:
            print("\nOpção inválida! Tente novamente.")
            continue

# Executa a função principal
if __name__ == "__main__":
    main()
