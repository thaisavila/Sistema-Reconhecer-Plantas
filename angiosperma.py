from Planta import Planta
# Frutas e 
class Angiosperma(Planta):
  def __init__(self, classificacao, nome_popular, nome_cientifico, altura_minima, altura_maxima, curiosidades,regiao,cor_do_fruto="azul"):
    super().__init__(classificacao,nome_popular, nome_cientifico, altura_minima, altura_maxima, curiosidades,regiao)
    self.cor_do_fruto = cor_do_fruto

  
  def exibir_classificacao():
    print("\nEssa planta é uma angiosperma!\n")
    print("Angiospermas são plantas vasculares com flores e frutos que protegem as sementes. Possuem aproximadamente 250 mil espécies, formando 90% das plantas). Têm vasos condutores bem desenvolvidos e possuem raiz, caule e folhas verdadeiros. Também possuem dupla fecundação, esporófito dominante e polinização por vento/animais. São de tamanho extremamente variados, desde plantas microscópicas até árvores gigantescas (+100m), podendo incluir ervas, arbustos e árvores – praticamente todas as plantas cultivadas (frutas, grãos, flores).")
  
  def _exibir_cor_fruto(self):
    print(f"Cor do fruto: {self.cor_do_fruto}")

  def exibir_infos(self):
    super()._exibir_nome_popular()
    super()._exibir_nome_cientifico()
    super()._exibir_altura()
    self._exibir_cor_fruto()
    super()._exibir_regioes()
    super()._exibir_curiosidades()