from Planta import Planta
# Frutas e 
class Angiosperma(Planta):
  def __init__(self, classificacao, nome_popular, nome_cientifico, altura_minima, altura_maxima, cor_principal_folhas, outras_cores_folhas, curiosidades,cor_do_fruto):
    super().__init__(classificacao,nome_popular, nome_cientifico, altura_minima, altura_maxima, cor_principal_folhas, outras_cores_folhas, curiosidades)
    self.cor_do_fruto = cor_do_fruto

  
  def exibir_classificação():
    print("\nEssa planta é uma angiosperma!\n")
    print("Angiospermas são plantas vasculares com flores e frutos que protegem as sementes. Possuem aproximadamente 250 mil espécies, formando 90% das plantas). Têm vasos condutores bem desenvolvidos e possuem raiz, caule e folhas verdadeiros. Também possuem dupla fecundação, esporófito dominante e polinização por vento/animais. São de tamanho extremamente variados, desde plantas microscópicas até árvores gigantescas (+100m), podendo incluir ervas, arbustos e árvores – praticamente todas as plantas cultivadas (frutas, grãos, flores).")
  
  def exibir_cor_fruto(self):
    print(f"Cor do fruto: {self.cor_do_fruto}")

  def exibir_infos(self):
    super().exibir_nome_popular()
    super().exibir_nome_cientifico()
    super().exibir_altura()
    self.exibir_cor_fruto()
    super().exibir_regioes()
    super().exibir_curiosidades()