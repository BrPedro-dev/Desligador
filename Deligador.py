import os


def menu():
    """Essa função faz o menu"""
    print(linha())
    print("[1] - Para desligar o pc.")
    print("[2] - Para cancelar.")
    print("[3] - Para sair.")
    print(linha())


def linha():
    """Essa Função é para estilo"""
    return "-" * 50


def cacula(horas: int, minutos: int) -> int:
    """
    Essa função transforma horas e minutos para segundos
    :param horas: inteiro
    :param minutos: inteiro
    :return: inteiro
    """
    horas *= (60 ** 2)
    minutos *= (60)
    return horas + minutos


# Programa principal
while True:

    resposta = " "
    menu()
    resposta = int(input("Qual é a opção? "))
    print(linha())

    if resposta == 1:
        horas = int(input("Quantas horas? "))
        print(linha())
        minutos = int(input("Quantos minutos? "))
        os.system(f"shutdown -s -t {cacula(horas, minutos)}")

    elif resposta == 2:
        os.system("shutdown -a")

    elif resposta == 3:
        break

    else:
        print("Resposta invalida, tente novamente")
