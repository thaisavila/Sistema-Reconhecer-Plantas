-- Ajeitar as plantas angiosperma cor azul azul-----
-- Ajeitar o encapsulamento
# Sistema de Identificação e Classificação de Plantas Representativas do Brasil
Esse sistema visa facilitar a identificação e classificação de plantas representativas do Brasil com bases em 4 categorias: Briófitas, Pteridófitas, Gimnosperma e Angiosperma. O sistema utiliza os conceitos básicos de POO: abstração, encapsulamento, herança e polimorfismo.
Esse Sistema foi criado para o projeto final da disciplina de POO do curso Análise e Desenvolvimento de Sistemas no semestre de 2025.2.

## Diagrama de classes (UML)


Como é possível perceber no UML, o sistema possui 5 classes:
* **class Planta:** que é classe principal, a classe pai, ela utiliza o conceito de abstração e possui os seguintes **atributos**: classificacao, nome_popular, nome_cientifico, altura_minima, altura_maxima, curiosidades e regiao. Também possui os seguintes métodos: exibir_classificacao(encapsulamento), exibir_nome_popular, exibir_nome_cientifico, exibir_altura, exibir_curiosidades, exibir_regiao e exibir_infos.
- A função exibir_infos chama as funções anteriores (menos a encapsulada) e exibe todas as informações da planta
* **class Briofita:** subclasse da classe planta, herda todos os seus atributos e possui 2 métodos com polimorfismo: exibir_altura e exibir_infos, que fazem o mesmo que os respectivos métodos da class Planta, mas com ajustes específicos para a altura da briófita, que é menor do que as outras.
* **class Pteridófita:** subclasse da classe planta, herda todos os seus atributos e métodos, mas possui 1 método adicional: exibir_classificacao, que exibe as informações do grupo pteridófita.
* **class Gimnosperma:** Assim como a class Pteridófita, essa classe é subclasse da classe planta e herda todos os seus atributos e métodos, mas possui 1 método adicional: exibir_classificacao, que exibe as informações do grupo gimnosperma.
* **class Angiosperma:** Como as últimas classes, essa classe também é subclasse da classe planta e herda todos os seus atributos e métodos, mas possui 1 atributo adicional: cor_do_fruto e também possui 3 métodos: exibir_cor do_fruto e exibir_infos e exibir_classificacao, que funcionam como as classes anteriores, mas com as adaptações para as informações da angiosperma.
* **class Listar:** Essa classe tem um funcionamento diferente das outras, pois não utiliza herança de nenhuma forma e não foram declarados atributos, essa classe foi feita para guardar métodos de listar necessários para o arquivo principal main, os métodos são: todas, por_nome, por_classificacao, planta_especifica, todas as funções são para listar as plantas tendo como base o critério declado no nome do método

Cada uma das classes está em um arquivo .py separado. Além dos 5 arquivos das classes, também existem mais os seguintes arquivos:
* **plantas.py:** Possui 32 objetos referentes as 4 subclasses já citadas
* **main.py:** Arquivo principal que importa todos os outros arquivos e possui um menu para o usuário

## Conceitos de POO aplicados
* **Abstração:** Estabelecido na classe Planta e em todas as suas 4 subclasses pois elas abstraem o conceito de plantas do mundo real, com características reais como nome, altura e cor
* **Herança:** Estabelecidade na superclass, ou classe pai, Planta e em suas 4 subclasses, ou classes filhas: Briófita, Pteridófita, Gimnosperma e Angiosperma
* **Encapsulamento:** Estabelecido no método _exibir_classificacao() da classe Planta
* **Polimorfismo:** Estebelecido nos métodos:
- exibir_classificacao: Que está na classe Planta e em todas as suas subclasses 
- exibir_infos, que está na super classe classe Planta e nas subclasses:Briófita e Angiosperma

# Instruções para execução 
1. Clone o repositório na sua máquina
2. Execute o arquivo main.py com o seguinte código ``python main.py``
3. Navegue pelo menu no terminal

# Uso do código
Ao executar o código, você verá o seguinte menu:

Nesse menu você terá 4 caminhos:
* **1.Identificar planta por característica**


* **2.Identificar planta por nome**


* **3.Listar plantas disponíveis**


* **4.Sair**

- uso
- UML