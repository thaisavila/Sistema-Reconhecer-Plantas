from Planta import Planta
from briofita import Briofita
from pteridofita import Pteridofita
from gimnosperma import Gimnosperma
from angiosperma import Angiosperma
from listar import Listar
from plantas import *
listar = Listar()

def identificar_planta(classificacao):
    altura = int(input("Digite a altura da sua planta em metros: "))
    print("Digite a região que sua planta pertence")
    regiao = input("Opções disponíveis: Norte, Nordeste, Sul, Suldeste, Centro-Oeste: ").lower()
    if classificacao == "angiosperma":
        cor_do_fruto = input("Digite a cor do fruto (por fora): ").lower()
        listar.planta_especifica("angiosperma",altura,regiao,cor_do_fruto)
    else:
        listar.planta_especifica("angiosperma",altura,regiao)


def identificar_grupo():
    print("\n=== Identificar planta por característica ===")
    # Identificar se é uma briófita    
    print("Sua planta possui vasos condutores?\n")
    print("Observações para identificara olho nu se tem ou não vasos condutores: Se parece um musgo ou um“tapete” muito baixo, formando uma camada fina sobre pedra, tronco ou solo úmido, sem raiz, caule e folhas verdadeiros = sem vasos condutores.\n Se tem caule e folhas bem definidos ou forma uma árvore ou arbusto = tem vasos condutores")
    briofita = input("\nDigite s ou n:").lower()
    while True:
        if briofita == "n":
            classificacao="briofita"
            Briofita.exibir_classificação()
            print()
            print("Possíveis plantas: ")
            listar.listar_plantas_classificacao()
        elif briofita == "s":
            break
        else:
            briofita = input("Sua planta possui vasos condutores? (s/n) ").lower()
    
    # Identificar se é uma angiosperma
    angiosperma = input("Sua planta possui frutos e/ou flores? (s/n) ").lower()    
    while True:
        if angiosperma == "s":
            classificacao="angiosperma"
            Angiosperma.exibir_classificação()
        elif angiosperma == "n":
            break
        else:    
            angiosperma = input("Sua planta possui frutos? (s/n) ").lower()
    
    # Identificar se é uma gimnosperma ou pteridofita
    gimnosperma = input("Sua planta possui semente? (s/n) ").lower()
    while gimnosperma != "s" and "n":
        if gimnosperma == "s":
            classificacao = "gimnosperma"
            Gimnosperma.exibir_classificacao()
        elif gimnosperma == "n":
            classificacao = "pteridofita"
            Pteridofita.exibir_classificacao()
        else:
            gimnosperma = input("Sua planta possui semente? (s/n)").lower()
    
    # Menu para identificar a planta específica
    identificar_planta = input("Você deseja continuar para identificar a planta? (s/n)").lower()
    if identificar_planta == "s":
        identificar_planta(classificacao)
    else:
        return

def identificar_por_nome():
    print("\n=== Identificar planta por nome ===")
    nome = input("Digite o nome da planta (nome popular ou científico): ").capitalize()
    print()
    listar.por_nome(nome)

def menu():
    while True:
        print("\n==== MENU PLANTAS ====")
        print("1. Identificar planta por característica")
        print("2. Identificar planta por nome")
        print("3. Listar plantas disponíveis")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            identificar_grupo()
        elif opcao == "2":
            identificar_por_nome()
        elif opcao == "3":
            listar.todas()
        elif opcao == "4":
            print("Saindo do programa...\nAté a próxima!")
            break
        else:
            print("Opção inválida, tente novamente.")


menu()