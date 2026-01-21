from Planta import Planta

class Briofita(Planta):
  def _exibir_altura(self):
    print("Altura (planta adulta): Entre 5 cm e 20 cm")

  def exibir_infos(self):
    super()._exibir_nome_popular()
    super()._exibir_nome_cientifico()
    self._exibir_altura()
    super()._exibir_regioes()
    super()._exibir_curiosidades()
    print()
    
  def exibir_classificacao():
    print("\nEssa planta é uma briófita!\n")
    print("Briófitas são plantas avasculares de pequeno porte (0,5-20 cm) que formam tapetes verdes em locais úmidos e sombreados, como rochas e troncos de árvores. Não possuem flores, sementes ou frutos e dependem da água para reprodução. ")

#briofita1 = Briofita("briofita","mangueira", "mangueiris", 5,15)
#briofita1.exibir_infos()