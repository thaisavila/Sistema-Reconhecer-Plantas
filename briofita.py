from Planta import Planta

class Briofita(Planta):
  def exibir_altura(self):
    print("Altura (planta adulta): Entre 5 cm e 20 cm")

  def exibir_infos(self):
    super().exibir_nome_popular()
    super().exibir_nome_cientifico()
    self.exibir_altura()
    super().exibir_regioes()
    super().exibir_curiosidades()
    print()
    
  def exibir_classificação():
    print("\nEssa planta é uma briófita!\n")
    print("Briófitas são plantas avasculares de pequeno porte (0,5-20 cm) que formam tapetes verdes em locais úmidos e sombreados, como rochas e troncos de árvores. Não possuem flores, sementes ou frutos e dependem da água para reprodução. ")

#briofita1 = Briofita("briofita","mangueira", "mangueiris", 5,15)
#briofita1.exibir_infos()