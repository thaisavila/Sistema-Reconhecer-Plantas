class Planta:
  def __init__(self, classificacao, nome_popular, nome_cientifico, altura_minima, altura_maxima, curiosidades="", regiao=[]):
    self.classificacao = classificacao
    self.nome_popular = nome_popular
    self.nome_cientifico = nome_cientifico
    self.altura_minima = altura_minima
    self.altura_maxima = altura_maxima
    self.curiosidades = curiosidades
    self.regiao = regiao

  def _exibir_nome_popular(self):
    print(f"Nome popular: {self.nome_popular}")

  def _exibir_nome_cientifico(self):
    print(f"Nome científico: {self.nome_cientifico}")

  def _exibir_altura(self):
    print(f"Altura (planta adulta): Entre {self.altura_minima} m e {self.altura_maxima} m")

  def _exibir_curiosidades(self):
    if self.curiosidades == "":
      return
    else:
      print(f"Curiosidades: {self.curiosidades}")    

  def _exibir_regioes(self):
    print("Regiões encontrada: ", end='')
    for i in range(len(self.regiao)):
      if i == len(self.regiao) - 1:
        print(self.regiao[i])
      else:
        print(self.regiao[i], end=', ')

  def __exibir_classificacao():
    print("A classificação dessa planta é: {classificacao}")
  
  def exibir_infos(self):
    self._exibir_nome_popular()
    self._exibir_nome_cientifico()
    self._exibir_altura()
    self._exibir_regioes()
    self._exibir_curiosidades()
    print()
  