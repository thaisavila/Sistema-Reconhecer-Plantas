from Planta import Planta
from briofita import Briofita
from pteridofita import Pteridofita
from gimnosperma import Gimnosperma
from angiosperma import Angiosperma
from plantas import *

def listar_plantas_classificacao(classificacao):
   cont=0
   for planta in lista_plantas:
       cont=cont+1
       if planta.classificacao == classificacao:
           print(cont, ".")
           planta.exibir_infos()
listar_plantas_classificacao("briofita")

def listar_planta_especifica(classificacao):
    pass

def identificar_grupo():
    print("\n=== Identificar planta por característica ===")
    
    briofita = input("Sua planta possui vasos condutores? (s/n) ").lower()
    while True:
        if briofita == "n":
            Briofita.exibir_classificação()
            print()
            print("Possíveis plantas: ")
            listar_plantas_classificacao()
        elif briofita == "s":
            break
        else:
            briofita = input("Sua planta possui vasos condutores? (s/n) ").lower()
    
    angiosperma = input("Sua planta possui frutos? (s/n) ")    
    while True:
        if angiosperma == "s":
            Angiosperma.exibir_classificação()

            # Identificar planta
            identificar_planta = input("Você também deseja identificar a planta? (s/n)")
            if identificar_planta == "s":
                print("Chama a função")
                return
            else:
                return

        elif angiosperma == "n":
            break
        else:    
            angiosperma = input("Sua planta possui frutos? (s/n) ")
    
    gimnosperma = input("Sua planta possui semente? (s/n) ")
    while gimnosperma != "s" and "n":
        if gimnosperma == "s":
            return Gimnosperma.exibir_classificacao()
        elif gimnosperma == "n":
            return Pteridofita.exibir_classificacao()
        else:
            gimnosperma = input("Sua planta possui semente? (s/n)")

def identificar_planta():
    pass



def identificar_por_nome():
    print("\n=== Identificar planta por nome ===")
    nome = input("Digite o nome da planta: ")
    print(f"Buscando planta com o nome: {nome}")
    # exemplo de retorno
    # ...


def listar_plantas():
    print("\n=== Listar plantas disponíveis ===")
    # exemplo de lista fixa (depois você pode trocar por uma lista real)
    plantas = ["Rosa", "Girassol", "Samambaia", "Orquídea"]
    for planta in plantas:
        print(f"- {planta}")
    # ...


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
            listar_plantas()
        elif opcao == "4":
            print("Saindo do programa...\nAté a próxima!")
            break
        else:
            print("Opção inválida, tente novamente.")


#menu()
#identificar_planta()