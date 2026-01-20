from briofita import Briofita
from pteridofita import Pteridofita
from gimnosperma import Gimnosperma
from angiosperma import Angiosperma

briofita1 = Briofita(
    classificacao="briofita",
    nome_popular="Musgo de solo",
    nome_cientifico="Bryophyta sp.",
    altura_minima=0.5,
    altura_maxima=5,
    regiao=["Norte", "Nordeste", "Sul", "Sudeste", "Centro-Oeste"]
)

briofita2 = Briofita(
    classificacao="briofita",
    nome_popular="Hepática talosa",
    nome_cientifico="Marchantiophyta sp.",
    altura_minima=0.2,
    altura_maxima=2,
    curiosidades="Hepáticas talosas apresentam gametófitos achatados em forma de fígado e ocorrem em solos muito úmidos no Brasil.",
    regiao=["Norte", "Nordeste", "Sul", "Sudeste", "Centro-Oeste"]
)

briofita3 = Briofita(
    classificacao="briofita",
    nome_popular="Antócero",
    nome_cientifico="Anthocerophyta sp.",
    altura_minima=0.2,
    altura_maxima=2,
    curiosidades="Antóceros são briófitas com esporófitos alongados em forma de 'chifre' e ocorrem em solos úmidos brasileiros.", 
    regiao=["Norte", "Nordeste", "Sul", "Sudeste", "Centro-Oeste"]
)

# Pteridófitas
pteridofita1 = Pteridofita(
classificacao="pteridofita",
nome_popular="Samambaia",
nome_cientifico="Pteridium aquilinum",
altura_minima=0.5,
altura_maxima=2.0,
curiosidades="Comum em áreas abertas, considerada invasora em pastagens e tóxica para o gado.",
regiao=["Sul", "Sudeste", "Centro-Oeste"]
)

pteridofita2 = Pteridofita(
classificacao="pteridofita",
nome_popular="Avenca",
nome_cientifico="Adiantum raddianum",
altura_minima=0.3,
altura_maxima=1.0,
curiosidades="Samambaia delicada usada como ornamental, cresce em solos úmidos e sombreados.",
regiao=["Sul", "Sudeste"]
)

pteridofita3 = Pteridofita(
classificacao="pteridofita",
nome_popular="Xaxim",
nome_cientifico="Dicksonia sellowiana",
altura_minima=1.0,
altura_maxima=5.0,
curiosidades="Samambaia arborescente da Mata Atlântica, ameaçada pela extração de caules para substrato.",
regiao=["Sul", "Sudeste"]
)

pteridofita4 = Pteridofita(
classificacao="pteridofita",
nome_popular="Cavalinha gigante",
nome_cientifico="Equisetum giganteum",
altura_minima=1.0,
altura_maxima=4.0,
curiosidades="Planta medicinal usada tradicionalmente, comum em solos úmidos e alagados.",
regiao=["Sul", "Sudeste", "Centro-Oeste"]
)

pteridofita5 = Pteridofita(
classificacao="pteridofita",
nome_popular="Samambaia do brejo",
nome_cientifico="Blechnum brasiliense",
altura_minima=0.5,
altura_maxima=2.0,
curiosidades="Samambaia terrestre em florestas serranas, com frondes dimórficas.",
regiao=["Sul", "Sudeste"]
)

pteridofita6 = Pteridofita(
classificacao="pteridofita",
nome_popular="Samambaia",
nome_cientifico="Alsophila setosa",
altura_minima=2.0,
altura_maxima=6.0,
curiosidades="Samambaia-árvore comum no Rio Grande do Sul, em solos férteis.",
regiao=["Sul"]
)

pteridofita7 = Pteridofita(
classificacao="pteridofita",
nome_popular="Samambaia",
nome_cientifico="Cyathea publicoarvorea",
altura_minima=3.0,
altura_maxima=10.0,
curiosidades="Espécie arbórea da família Cyatheaceae, encontrada em florestas montanhosas.",
regiao=["Sudeste"]
)

pteridofita8 = Pteridofita(
classificacao="pteridofita",
nome_popular="Rabo de peixe",
nome_cientifico="Nephrolepis biserrata",
altura_minima=0.5,
altura_maxima=1.5,
curiosidades="Epífita ou terrestre na Amazônia, forma grandes populações em clareiras.",
regiao=["Norte", "Centro-Oeste"]
)

pteridofita9 = Pteridofita(
classificacao="pteridofita",
nome_popular="Samambaia macho",
nome_cientifico="Dryopteris filix-mas",
altura_minima=0.5,
altura_maxima=1.5,
curiosidades="Comum em matas naturais elevadas, de Bahia ao Rio Grande do Sul.",
regiao=["Nordeste", "Sudeste", "Sul"]
)

pteridofita10 = Pteridofita(
classificacao="pteridofita",
nome_popular="Filme",
nome_cientifico="Hymenophyllum spp.",
altura_minima=0.1,
altura_maxima=0.5,
curiosidades="Epífitas delicadas em florestas úmidas e nebulares, com frondes transparentes.",
regiao=["Sul", "Sudeste"]
)

# Gimnospermas
gimnosperma1 = Gimnosperma(
classificacao="gimnosperma",
nome_popular="Araucária",
nome_cientifico="Araucaria angustifolia",
altura_minima=10.0,
altura_maxima=50.0,
curiosidades="Produz o pinhão comestível e forma florestas exclusivas em altitudes acima de 800m.",
regiao=["Sul", "Sudeste"]
)

gimnosperma2 = Gimnosperma(
classificacao="gimnosperma",
nome_popular="Pinheiro do mato",
nome_cientifico="Podocarpus sellowii",
altura_minima=5.0,
altura_maxima=25.0,
curiosidades="Árvore perenifólia comum em brejos de altitude e chapadas, com sementes com arilo atrativo para aves.",
regiao=["Nordeste", "Sudeste"]
)

gimnosperma3 = Gimnosperma(
classificacao="gimnosperma",
nome_popular="Ituá",
nome_cientifico="Gnetum amazonicum",
altura_minima=5.0,
altura_maxima=20.0,
curiosidades="Liana lenhosa da Amazônia usada em estudos fitogeográficos, com sementes comestíveis.",
regiao=["Norte"]
)

gimnosperma4 = Gimnosperma(
classificacao="gimnosperma",
nome_popular="Batata de paca",
nome_cientifico="Zamia amazonum",
altura_minima=0.5,
altura_maxima=2.0,
curiosidades="Cica terrestre com folhas pinadas, nativa da região amazônica.",
regiao=["Norte"]
)

gimnosperma5 = Gimnosperma(
classificacao="gimnosperma",
nome_popular="Ituá",
nome_cientifico="Gnetum leyboldii",
altura_minima=3.0,
altura_maxima=15.0,
curiosidades="Cipó comum às margens de rios na Amazônia, representado em herbários brasileiros.",
regiao=["Norte", "Centro-Oeste"]
)

gimnosperma6 = Gimnosperma(
classificacao="gimnosperma",
nome_popular="Cipó macarrão",
nome_cientifico="Ephedra triandra",
altura_minima=1.0,
altura_maxima=6.0,
curiosidades="Arbusto escandente no Sul do Brasil, com folhas caducas e estróbilos globosos.",
regiao=["Sul"]
)

gimnosperma7 = Gimnosperma(
classificacao="gimnosperma",
nome_popular="Pinheiro bravo",
nome_cientifico="Podocarpus lambertii",
altura_minima=5.0,
altura_maxima=27.0,
curiosidades="Árvore de florestas com araucária, com DAP até 120cm e folhas lanceoladas.",
regiao=["Sul", "Sudeste"]
)

gimnosperma8 = Gimnosperma(
classificacao="gimnosperma",
nome_popular="Batata de catuaba",
nome_cientifico="Zamia ulei",
altura_minima=0.5,
altura_maxima=3.0,
curiosidades="Cica com tronco curto, encontrada em solos amazônicos.",
regiao=["Norte"]
)

gimnosperma9 = Gimnosperma(
classificacao="gimnosperma",
nome_popular="Coração de pássaro",
nome_cientifico="Gnetum urens",
altura_minima=5.0,
altura_maxima=20.0,
curiosidades="Liana da Amazônia com ocorrência em herbários como o IAN.",
regiao=["Norte"]
)

# Angiospermas
angiosperma1 = Angiosperma(
classificacao="angiosperma",
nome_popular="Cupuaçu",
nome_cientifico="Theobroma grandiflorum",
altura_minima=6.0,
altura_maxima=20.0,
curiosidades="Árvore da família do cacau com frutos grandes ricos em polpa aromática, usada em sucos e doces.",
regiao=["Norte"]
)

angiosperma2 = Angiosperma(
classificacao="Angiosperma",
nome_popular="Açaí",
nome_cientifico="Euterpe oleracea",
altura_minima=10.0,
altura_maxima=25.0,
curiosidades="Palmeira esguia de várzeas amazônicas, com cachos de frutos roxos nutritivos.",
regiao=["Norte"]
)

angiosperma3 = Angiosperma(
classificacao="angiosperma",
nome_popular="Juazeiro",
nome_cientifico="Ziziphus joazeiro",
altura_minima=5.0,
altura_maxima=16.0,
curiosidades="Árvore pioneira da Caatinga com frutos comestíveis e copa larga espinhosa.",
regiao=["Nordeste"]
)

angiosperma4 = Angiosperma(
classificacao="angiosperma",
nome_popular="Mandacaru",
nome_cientifico="Cereus jamacaru",
altura_minima=3.0,
altura_maxima=16.0,
curiosidades="Cacto columnar icônico da Caatinga com flores noturnas e frutos vermelhos.",
regiao=["Nordeste"]
)

angiosperma5 = Angiosperma(
classificacao="angiosperma",
nome_popular="Cajueiro",
nome_cientifico="Anacardium occidentale",
altura_minima=6.0,
altura_maxima=14.0,
curiosidades="O que conhecemos como frut do caju na verdade é um pseudofruto e o fruto verdadeiro do cajueiro é a castanha, que é formada por três partes: casca, película e amêndoa(que é a semente)",
regiao=["Nordeste", "Centro-Oeste"]
)

angiosperma6 = Angiosperma(
classificacao="angiosperma",
nome_popular="Jatobá",
nome_cientifico="Hymenaea courbaril",
altura_minima=15.0,
altura_maxima=40.0,
curiosidades="Árvore majestosa com resina medicinal e madeira resistente usada em construção.",
regiao=["Centro-Oeste", "Nordeste"]
)

angiosperma7 = Angiosperma(
classificacao="angiosperma",
nome_popular="Ipê roxo",
nome_cientifico="Handroanthus impetiginosus",
altura_minima=8.0,
altura_maxima=12.0,
curiosidades="Árvore ornamental com flores roxas vibrantes no inverno, copa larga.",
regiao=["Sudeste", "Centro-Oeste", "Nordeste", "Norte"]
)

angiosperma8 = Angiosperma(
classificacao="angiosperma",
nome_popular="Jabuticaba",
nome_cientifico="Plinia cauliflora",
altura_minima=3.0,
altura_maxima=15.0,
curiosidades="Árvore semidecídua com frutos doces nascendo no tronco e galhos.",
regiao=["Sudeste", "Sul", "Nordeste"]
)

angiosperma9 = Angiosperma(
classificacao="angiosperma",
nome_popular="Pitanga",
nome_cientifico="Eugenia uniflora",
altura_minima=2.0,
altura_maxima=7.0,
curiosidades="Arbusto com frutos vermelhos aromáticos, usado em cercas vivas.",
regiao=["Sul", "Sudeste"]
)

angiosperma10 = Angiosperma(
classificacao="angiosperma",
nome_popular="Guaraná",
nome_cientifico="Paullinia cupana",
altura_minima=3.0,
altura_maxima=10.0,
curiosidades="Trepadeira liana com sementes ricas em cafeína, base de bebidas energéticas.",
regiao=["Norte"]
)

lista_plantas = [
    # Briofitas
    briofita1,
    briofita2,
    briofita3,

    # Pteridófitas
    pteridofita1,
    pteridofita2,
    pteridofita3,
    pteridofita4,
    pteridofita5,
    pteridofita6,
    pteridofita7,
    pteridofita8,
    pteridofita9,
    pteridofita10,

    # Gimnospermas
    gimnosperma1,
    gimnosperma2,
    gimnosperma3,
    gimnosperma4,
    gimnosperma5,
    gimnosperma6,
    gimnosperma7,
    gimnosperma8,
    gimnosperma9,

    # Angiospermas
    angiosperma1,
    angiosperma2,
    angiosperma3,
    angiosperma4,
    angiosperma5,
    angiosperma6,
    angiosperma7,
    angiosperma8,
    angiosperma9,
    angiosperma10,
]

#briofita3.exibir_infos()