def validar_opcao(opcoes):
    escolha = input("Opção: ")
    while escolha not in opcoes:
        print("Opção inválida, tente novamente!")
        escolha = input("Opção: ")
    return escolha