# Sistema de Identificação e Classificação de Plantas Representativas do Brasil
Esse sistema visa facilitar a identificação e classificação de plantas representativas do Brasil com bases em 4 categorias: Briófitas, Pteridófitas, Gimnosperma e Angiosperma. O sistema utiliza os conceitos básicos de POO: abstração, encapsulamento, herança e polimorfismo.
Esse Sistema foi criado para o projeto final da disciplina de POO do curso Análise e Desenvolvimento de Sistemas no semestre de 2025.2.

## Diagrama de classes (UML)
<img width="1537" height="971" alt="image" src="https://github.com/user-attachments/assets/e998c7b6-72b2-40c5-ab2d-f82aac2023b4" />



Como é possível perceber no UML, o sistema possui 5 classes:
* **class Planta:** que é classe principal, a classe pai, ela utiliza o conceito de abstração e possui os seguintes **atributos**: classificacao, nome_popular, nome_cientifico, altura_minima, altura_maxima, curiosidades e regiao. Também possui os seguintes métodos: exibir_classificacao, _exibir_nome_popular, _exibir_nome_cientifico, _exibir_altura, _exibir_curiosidades, _exibir_regiao e exibir_infos.
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

* **Encapsulamento:** Estabelecido no método protegido __exibir_classificacao() da classe Planta, nos métodos privados: _exibir_nome_popular, _exibir_nome_cientifico, _exibir_altura, _exibir_curiosidades e _exibir_regiao da classe Planta, no método _exibir_altura da classe Briofita e no método privado _exibir_cor_fruto da classe Angiosperma

* **Polimorfismo:** Estebelecido nos métodos:
- exibir_classificacao: Que está na classe Planta e em todas as suas subclasses 
- exibir_infos, que está na super classe classe Planta e nas subclasses:Briófita e Angiosperma

# Instruções para execução 
1. Clone o repositório na sua máquina
2. Execute o arquivo main.py com o seguinte código ``python main.py``
3. Navegue pelo menu no terminal

## Uso do código
Ao executar o código, você verá o seguinte menu:

<img width="389" height="150" alt="image" src="https://github.com/user-attachments/assets/b52d66c6-03e8-485a-9ee9-62323ce13a95" />


Nesse menu você terá 4 caminhos:

* **1.Identificar planta por característica**
Para selecionar essa opção você deverá enviar o número 1 no menu principal

<img width="533" height="404" alt="image" src="https://github.com/user-attachments/assets/babc7a12-56fd-434e-8291-874cf982a952" />

O sistema vai fazer algumas perguntas, primeiro para identificar o grupo que a planta pertence, depois, se o usuário permitir, para identifiicar as possíveis plantas, com excessão das briófitas

Exemplos com os 4 grupos de plantas:
- **Briófita**
<img width="1776" height="622" alt="image" src="https://github.com/user-attachments/assets/b255c218-998e-4c04-9a9d-0a5378d2847b" />

No caso das briófitas, o sistema só faz perguntas para identificar o grupo, pois as briófitas são plantas difíceis de ser identificadas a olho nu e possuem menos variedades de plantas no catálogo

- **Pteridófita**
<img width="1771" height="842" alt="image" src="https://github.com/user-attachments/assets/178ad66c-47e5-498a-860e-a4605e158b5e" />

- **Gimnosperma**
<img width="1774" height="627" alt="image" src="https://github.com/user-attachments/assets/3ae0729e-342b-4be4-aecc-db87f4ee738c" />

- **Angiosperma**
<img width="1784" height="648" alt="image" src="https://github.com/user-attachments/assets/3cd6ba18-1e34-44d4-84f7-5917af703d09" />

Como é possível perceber, o código não vê diferença entre **letras minúsculas e maiúsculas**, dessa forma, **diminui a possibilidade de erro**

Além disso, existem outros casos, como:
- O usuário tentar identificar uma planta que não existe no catálogo:
<img width="1784" height="513" alt="image" src="https://github.com/user-attachments/assets/9f73c559-1da4-4af7-a484-d283c5173e6a" />

- O usuário digitar algo diferente do esperado:
<img width="1775" height="540" alt="image" src="https://github.com/user-attachments/assets/df06325c-c7d6-4b66-8a02-84a5a0a8e20b" />
Uma mensagem de erro é mostrada e o código só continua quando o usuário digita corretamente

* **2.Identificar planta por nome**
Para acessar essa opção é necessário digitar 2 no menu principal
<img width="534" height="212" alt="image" src="https://github.com/user-attachments/assets/e3adbfd4-82be-41e6-a15b-6629c86b4a7f" />

Aqui será possível digitar o nome de uma planta e o sistema mostrará as informações sobre essa planta, funciona tanto com o nome científico quanto com o nome popular

- **Nome científico**
<img width="1768" height="226" alt="image" src="https://github.com/user-attachments/assets/a313f410-704a-44c8-8f75-ac20db699680" />

- **Nome popular**
<img width="1781" height="236" alt="image" src="https://github.com/user-attachments/assets/f756bbb1-6033-419f-83f1-481a27be2990" />

* **3.Listar plantas disponíveis**
Para acessar essa opção é necessário digitar 3 no menu principal
<img width="1158" height="722" alt="image" src="https://github.com/user-attachments/assets/2ea5a9c0-9440-4699-9c2e-cb0598fae54f" />
O sistema mostrará todas as plantas disponíveis no catálogo, que são 32


* **4.Sair**

Para acessar essa opção é necessário digitar 4 no menu principal

<img width="398" height="216" alt="image" src="https://github.com/user-attachments/assets/4adfd3c5-849a-43a8-811e-a976bb4af3e2" />

## Autor
Criado por Thaís Ávila | thaisaguiar019@gmail.com
