class Planta:
  def __init__(self, nome_popular, nome_cientifico, altura_minima, altura_maxima, cor_principal_folhas, outras_cores_folhas=[], curiosidades=""):
    self.nome_popular = nome_popular
    self.nome_cientifico = nome_cientifico
    self.altura_minima = altura_minima
    self.altura_maxima = altura_maxima
    self.cor_principal_folhas = cor_principal_folhas
    self.outras_cores_folhas = outras_cores_folhas
    self.curiosidades = curiosidades

  def exibir_nome_popular(self):
    print(f"Nome popular: {self.nome_popular}")

  def exibir_nome_cientifico(self):
    print(f"Nome científico: {self.nome_cientifico}")

  def exibir_altura(self):
    print(f"Altura (planta adulta): Entre {self.altura_minima} m e {self.altura_maxima} m")

  def exibir_cor_folhas(self):
    print(f"Cor principal das folhas: {self.cor_principal_folhas}")
    if self.outras_cores_folhas == []:
      print(end='')
    else:
      print(f"Outras cores nas folhas: ", end='')
      for i in range(len(self.outras_cores_folhas)):
        if i == len(self.outras_cores_folhas) - 1:
          print(self.outras_cores_folhas[i])  
        else:
          print(self.outras_cores_folhas[i], end=', ') 

  def exibir_curiosidades(self):
    if self.curiosidades == "":
      return
    else:
      print(f"Curiosidades: {self.curiosidades}")    


planta1 = Planta("mangueira", "mangueiris", 5,15,"verde",['laranja','azul'], "é a melhor planta")
planta1.exibir_curiosidades()