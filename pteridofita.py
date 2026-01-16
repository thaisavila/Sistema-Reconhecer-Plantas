from Planta import Planta

class Pteridofita(Planta):
  def exibir_classificacao():
    print("\nEssa planta é uma pteridófita!\n")
    print("Pteridófitas são plantas vasculares sem sementes. Possuem vasos condutores(xilema e floema), raiz, caule e folhas verdadeiras, sendo maiores que briófitas. Não possuem flores ou frutos. Reproduzem-se por esporos em soros (manchas marrons nas folhas) e dependem de água para fecundação.")

  def exibir_infos(self):
    super().exibir_nome_popular()
    super().exibir_nome_cientifico()
    super().exibir_altura()
    super().exibir_cor_folhas()
    super().exibir_curiosidades()

