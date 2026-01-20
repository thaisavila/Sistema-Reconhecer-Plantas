from Planta import Planta
from briofita import Briofita
from pteridofita import Pteridofita
from gimnosperma import Gimnosperma
from angiosperma import Angiosperma
from listar import Listar
from plantas import *
listar = Listar()

def identificar_planta(classificacao):
    continuar = input("Você deseja continuar para identificar a planta? (s/n) ").lower()
    while continuar != "s" and continuar != "n":
        continuar = input("Você deseja continuar para identificar a planta? (s/n)").lower()
    
    if continuar == "s":
        altura = int(input("Digite a altura da sua planta em metros: "))
        print("Digite a região que sua planta pertence")
        regiao = input("Opções disponíveis: Norte, Nordeste, Sul, Suldeste, Centro-Oeste: ").capitalize()
        if classificacao == "angiosperma":
            cor_do_fruto = input("Digite a cor do fruto (por fora): ").capitalize()
            print("=== Possíveis plantas ===")
            listar.planta_especifica("angiosperma",altura,regiao,cor_do_fruto)
        else:
            print("=== Possíveis plantas ===")
            listar.planta_especifica(classificacao,altura,regiao)
    else: 
        return

def identificar_grupo():
    print("\n=== Identificar planta por característica ===")
    # Identificar se é uma briófita    
    print("Sua planta possui vasos condutores?\n")
    print("Observações para identificar a olho nu se tem ou não vasos condutores: \nSe parece um musgo ou um “tapete” muito baixo, formando uma camada fina sobre pedra, tronco ou solo úmido, sem raiz, caule e folhas verdadeiros = sem vasos condutores. \nSe tem caule e folhas bem definidos ou forma uma árvore ou arbusto = tem vasos condutores")
    briofita = input("\nDigite s ou n: ").lower()
    while True:
        if briofita == "n":
            classificacao="briofita"
            Briofita.exibir_classificação()
            print()
            print("Possíveis plantas: ")
            return listar.por_classificacao("briofita")
            
        elif briofita == "s":
            break
        else:
            briofita = input("Sua planta possui vasos condutores? (s/n) ").lower()
    
    # Identificar se é uma angiosperma
    angiosperma = input("Sua planta possui frutos e/ou flores? (s/n) ").lower()    
    while True:
        if angiosperma == "s":
            Angiosperma.exibir_classificação()
            print()
            return identificar_planta("angiosperma")
        elif angiosperma == "n":
            break
        else:    
            angiosperma = input("Sua planta possui frutos? (s/n) ").lower()
    
    # Identificar se é uma gimnosperma ou pteridofita
    gimnosperma = input("Sua planta possui semente? (s/n) ").lower()
    while gimnosperma != "s" and gimnosperma== "n":
        gimnosperma = input("Sua planta possui semente? (s/n) ").lower()
        
    if gimnosperma == "s":
        Gimnosperma.exibir_classificacao()
        print()
        return identificar_planta("gimnosperma")
        
    elif gimnosperma == "n":
        Pteridofita.exibir_classificacao()
        print()
        return identificar_planta("pteridofita")
    
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