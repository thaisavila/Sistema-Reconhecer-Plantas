from plantas import *

class Listar:
  def todas(self):
    cont=0
    for planta in lista_plantas:
        cont+=1
        print(cont,".")
        planta.exibir_infos()

  def por_nome(self, nome):
    encontrou = False
    for planta in lista_plantas:
        if nome == planta.nome_popular or nome == planta.nome_cientifico:
            planta.exibir_infos()
            encontrou = True
    if not encontrou:
        print("Nenhuma planta encontrada com esse nome.")

  def por_classificacao(self,classificacao):
   cont=0
   for planta in lista_plantas:
       cont=cont+1
       if planta.classificacao == classificacao:
           print(cont, ".")
           planta.exibir_infos()

  def planta_especifica(self,classificacao, altura,regiao,cor_do_fruto="nenhuma"):
    cont=0
    for planta in lista_plantas:
       if planta.classificacao=="angiosperma" and altura>=planta.altura_minima and altura<=planta.altura_maxima and regiao in planta.regiao and cor_do_fruto==planta.cor_do_fruto:
           cont+=1
           print(cont, ".")
           planta.exibir_infos()
       elif planta.classificacao==classificacao and altura>=planta.altura_minima and altura<=planta.altura_maxima and regiao in planta.regiao:
           cont+=1
           print(cont, ".")
           planta.exibir_infos()
           print()
    if cont ==0:
       print("Nenhuma planta foi encontrada com essas características!")

#listar = Listar()
