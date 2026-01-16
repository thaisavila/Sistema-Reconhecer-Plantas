from Planta import Planta
# Frutas e 
class Angiosperma(Planta):
  def exibir_classificação():
    print("\nEssa planta é uma angiosperma!\n")
    print("Angiospermas são plantas vasculares com flores e frutos que protegem as sementes. Possuem aproximadamente 250 mil espécies, formando 90% das plantas). Têm vasos condutores bem desenvolvidos e possuem raiz, caule e folhas verdadeiros. Também possuem dupla fecundação, esporófito dominante e polinização por vento/animais. São de tamanho extremamente variados, desde plantas microscópicas até árvores gigantescas (+100m), podendo incluir ervas, arbustos e árvores – praticamente todas as plantas cultivadas (frutas, grãos, flores).")

angiosperma1 = Angiosperma("mangueira", "mangueiris", 5,15,"verde",['laranja','azul'], "é a melhor planta")
# planta1.exibir_infos()
angiosperma1 = Angiosperma.exibir_classificação()