# -*- coding: utf-8 -*-
db_name = 'militantes'

icon = '../src_files/logos/logo.ico'
pdf_image = '../src_files/logos/nova_direita.png'

select_options = {
    "Distrito de Aveiro": {
        "Águeda": ["Agadão", "Aguada de Baixo", "Aguada de Cima", "Águeda e Borralha", "Barrô e Aguada de Baixo", "Belazaima do Chão, Castanheira do Vouga e Agadão", "Fermentelos", "Macinhata do Vouga", "Préstimo e Macieira de Alcôba", "Recardães e Espinhel", "Trofa, Segadães e Lamas do Vouga", "Valongo do Vouga"],
        "Albergaria-a-Velha": ["Albergaria-a-Velha e Valmaior", "Alquerubim", "Angeja", "Branca", "Ribeira de Fráguas", "São João de Loure e Frossos"],
        "Anadia": ["Amoreira da Gândara, Paredes do Bairro e Ancas", "Arcos e Mogofores", "Avelãs de Caminho", "Avelãs de Cima", "Moita", "Sangalhos", "São Lourenço do Bairro", "Tamengos, Aguim e Óis do Bairro", "Vilarinho do Bairro"],
        "Arouca": ["Albergaria da Serra e Cabreiros", "Arouca e Burgo", "Chave", "Covelo de Paivó e Janarde", "Canelas e Espiunca", "Escariz", "Fermedo", "Mansores", "Moldes", "Rossas", "Santa Eulália", "São Miguel do Mato", "Tropeço", "Urrô", "Várzea"],
        "Aveiro": ["Aradas", "Cacia", "Eixo e Eirol", "Esgueira", "Glória e Vera Cruz", "Oliveirinha", "Requeixo, Nossa Senhora de Fátima e Nariz", "Santa Joana", "São Bernardo", "São Jacinto"],
        "Castelo de Paiva": ["Fornos", "Raiva, Pedorido e Paraíso", "Real", "Santa Maria de Sardoura", "São Martinho de Sardoura", "Sobrado e Bairros"],
        "Espinho": ["Anta e Guetim", "Espinho", "Paramos", "Silvalde"],
        "Estarreja": ["Avanca", "Beduído e Veiros", "Canelas e Fermelã", "Pardilhó", "Salreu"],
        "Ílhavo": ["Gafanha da Encarnação", "Gafanha da Nazaré", "Gafanha do Carmo", "Ílhavo (São Salvador)"],
        "Mealhada": ["Barcouço", "Casal Comba", "Luso", "Mealhada, Ventosa do Bairro e Antes", "Pampilhosa", "Vacariça"],
        "Murtosa": ["Bunheiro", "Monte", "Murtosa", "Torreira"],
        "Oliveira de Azeméis": ["Carregosa", "Cesar", "Fajões", "Loureiro", "Macieira de Sarnes", "Madalena e Senhora do Salto", "Nogueira do Cravo e Pindelo", "Oliveira de Azeméis, Santiago de Riba-Ul, Ul, Macinhata da Seixa e Madail", "Ossela", "Pinheiro da Bemposta, Travanca e Palmaz", "São Martinho da Gândara", "São Roque", "Vila de Cucujães"],
        "Oliveira do Bairro": ["Bustelos, Troviscal e Mamarrosa", "Oiã", "Oliveira do Bairro", "Palhaça"],
        "Ovar": ["Arada", "Cortegaça", "Espargo", "Maceda", "Ovar, São João, Arada e São Vicente de Pereira Jusã", "São João de Ovar", "São Vicente de Pereira Jusã", "Válega"],
        "Santa Maria da Feira": ["Argoncilhe", "Arrifana", "Caldas de São Jorge e Pigeiros", "Canedo, Vale e Vila Maior", "Escapães", "Espargo", "Fiães", "Fornos", "Lourosa", "Milheirós de Poiares", "Mozelos", "Nogueira da Regedoura", "Paços de Brandão", "Rio Meão", "Romariz", "Sanguedo", "Santa Maria de Lamas", "São João de Ver", "São Paio de Oleiros", "Souto", "Travanca", "Vale", "Vila Maior"],
        "São João da Madeira": ["São João da Madeira"],
        "Sever do Vouga": ["Cedrim e Paradela", "Couto de Esteves", "Pessegueiro do Vouga", "Rocas do Vouga", "Sever do Vouga", "Silva Escura e Dornelas", "Talhadas"],
        "Vagos": ["Calvão", "Fonte de Angeão e Covão do Lobo", "Gafanha da Boa Hora", "Ouca", "Ponte de Vagos e Santa Catarina", "Santo André de Vagos", "Sosa", "Vagos e Santo António"],
        "Vale de Cambra": ["Arões", "Cepelos", "Junqueira", "Macieira de Cambra", "Roge", "São Pedro de Castelões", "Vila Chã", "Codal e Vila Cova de Perrinho"]
    },
    "Distrito de Beja": {
        "Aljustrel": ["Aljustrel e Rio de Moinhos", "Ervidel", "Messejana", "São João de Negrilhos"],
        "Almodôvar": ["Aldeia dos Fernandes", "Almodôvar e Graça dos Padrões", "Rosário", "Santa Clara-a-Nova e Gomes Aires", "São Barnabé", "Santa Cruz", "São Marcos da Serra"],
        "Alvito": ["Alvito", "Vila Nova da Baronia"],
        "Barrancos": ["Barrancos"],
        "Beja": ["Albernoa e Trindade", "Baleizão", "Beringel", "Cabeça Gorda", "Nossa Senhora das Neves", "Salvada e Quintos", "Santa Clara de Louredo", "Santa Maria da Feira", "São João Baptista", "São Matias", "São Brissos", "Trigaches e São Brissos"],
        "Castro Verde": ["Castro Verde e Casével", "Entradas", "Santa Bárbara de Padrões", "São Marcos da Ataboeira"],
        "Cuba": ["Cuba", "Faro do Alentejo", "Vila Alva", "Vila Ruiva"],
        "Ferreira do Alentejo": ["Alfundão e Peroguarda", "Canhestros", "Ferreira do Alentejo e Canhestros", "Figueira dos Cavaleiros", "Odivelas"],
        "Mértola": ["Alcaria Ruiva", "Corte do Pinto", "Espírito Santo", "Mértola", "Santana de Cambas", "São João dos Caldeireiros", "São Miguel do Pinheiro", "São Pedro de Sólis", "São Sebastião dos Carros"],
        "Moura": ["Amareleja", "Moura (Santo Agostinho e São João Baptista) e Santo Amador", "Póvoa de São Miguel", "Safara e Santo Aleixo da Restauração", "Sobral da Adiça"],
        "Odemira": ["Boavista dos Pinheiros", "Colos", "Longueira/Almograve", "Luzianes-Gare", "Relíquias", "Sabóia", "Santa Clara-a-Velha", "São Luís", "São Martinho das Amoreiras", "São Salvador e Santa Maria", "São Teotónio", "Vale de Santiago", "Vila Nova de Milfontes"],
        "Ourique": ["Garvão e Santa Luzia", "Ourique", "Panoias e Conceição", "Santana da Serra"],
        "Serpa": ["Brinches", "Pias", "Vila Nova de São Bento e Vale de Vargo", "Serpa (Salvador e Santa Maria)", "Vila Verde de Ficalho"],
        "Vidigueira": ["Pedrógão", "Selmes", "Vidigueira", "Vila de Frades"]
    },
    "Distrito de Braga": {
        "Amares": ["Amares e Figueiredo", "Barreiros", "Besteiros", "Bico", "Caires", "Caldelas, Sequeiros e Paranhos", "Carrazedo", "Dornelas", "Ferreiros, Prozelo e Besteiros", "Fiscal", "Goães", "Lago", "Rendufe", "Santa Maria do Bouro", "Santa Marta do Bouro", "Torre e Portela", "Vilela, Seramil e Paredes Secas"],
        "Barcelos": ["Abade de Neiva", "Aborim", "Adães", "Aguiar", "Airó", "Aldreu", "Alheira e Igreja Nova", "Alvelos", "Arcozelo", "Areias", "Areias de Vilar e Encourados", "Balugães", "Barcelinhos", "Barcelos, Vila Boa e Vila Frescainha (São Martinho e São Pedro)", "Barqueiros", "Cambeses", "Campo e Tamel (São Pedro Fins)", "Carapeços", "Carreira", "Carvalhal", "Carvalhas", "Chavão", "Chorente, Góios, Courel, Pedra Furada e Gueral", "Cossourado", "Couto", "Creixomil e Mariz", "Cristelo", "Durrães e Tregosa", "Faria", "Feitos", "Fonte Coberta", "Fornelos", "Fragoso", "Gamil e Midões", "Gilmonde", "Grimancelos", "Lama", "Lijó", "Macieira de Rates", "Manhente", "Martim", "Milhazes, Vilar de Figos e Faria", "Moure", "Negreiros e Chavão", "Oliveira", "Palme", "Panque", "Paradela", "Pereira", "Perelhal", "Pousa", "Quintiães e Aguiar", "Remelhe", "Roriz", "Sequeade e Bastuço (São João e Santo Estêvão)", "Silva", "Silveiros e Rio Covo (Santa Eulália)", "Tamel (Santa Leocádia) e Vilar do Monte", "Ucha", "Várzea", "Viatodos, Grimancelos, Minhotães e Monte de Fralães", "Vila Cova e Feitos", "Vilar de Figos e Faria"],
        "Braga": ["Adaúfe", "Arentim e Cunha", "Braga (Maximinos, Sé e Cividade)", "Braga (São José de São Lázaro e São João do Souto)", "Cabreiros e Passos (São Julião)", "Celeirós, Aveleda e Vimieiro", "Crespos e Pousada", "Escudeiros e Penso (Santo Estêvão e São Vicente)", "Espinho", "Esporões", "Este (São Pedro e São Mamede)", "Ferreiros e Gondizalves", "Figueiredo", "Gualtar", "Guisande e Oliveira (São Pedro)", "Lamas", "Lamaçães", "Lomar e Arcos", "Merelim (São Paio), Panoias e Parada de Tibães", "Merelim (São Pedro) e Frossos", "Mire de Tibães", "Nogueira, Fraião e Lamaçães", "Nogueiró e Tenões", "Padim da Graça", "Palmeira", "Pedralva", "Priscos", "Real, Dume e Semelhe", "Ruilhe", "Santa Lucrécia de Algeriz e Navarra", "São Vicente", "Sequeira", "Sobreposta", "Tadim", "Trandeiras", "Vilaça e Fradelos"],
        "Cabeceiras de Basto": ["Abadim", "Alvite e Passos", "Arco de Baúlhe e Vila Nune", "Basto", "Bucos", "Cabeceiras de Basto", "Cavez", "Faia", "Gondiães e Vilar de Cunhas", "Painzela", "Pedraça", "Refojos de Basto, Outeiro e Painzela", "Rio Douro"],
        "Celorico de Basto": ["Agilde", "Arnóia", "Borba de Montanha", "Britelo, Gémeos e Ourilhe", "Caçarilhe e Infesta", "Canedo de Basto e Corgo", "Carvalho e Basto (Santa Tecla)", "Codeçoso", "Fervença", "Moreira do Castelo", "Rego", "Ribas", "Vale de Bouro", "Veade, Gagos e Molares"],
        "Esposende": ["Antas", "Apúlia e Fão", "Belinho e Mar", "Esposende, Marinhas e Gandra", "Fonte Boa e Rio Tinto", "Forjães", "Gemeses", "Palmeira de Faro e Curvos", "Vila Chã"],
        "Fafe": ["Aboim, Felgueiras, Gontim e Pedraído", "Agrela e Serafão", "Antime e Silvares (São Clemente)", "Ardegão, Arnozela e Seidões", "Armil", "Cepães e Fareja", "Estorãos", "Fafe", "Fornelos", "Freitas e Vila Cova", "Golães", "Medelo", "Monte e Queimadela", "Moreira do Rei", "Passos", "Quinchães", "Regadas", "Revelhe", "Ribeiros", "Santa Cristina de Arões", "São Gens", "São Martinho de Silvares", "São Romão de Arões", "Travassós", "Várzea Cova", "Vinhós"],
        "Guimarães": ["Aldão", "Azurém", "Barco", "Brito", "Caldelas", "Candoso (São Martinho)", "Candoso (Santiago)", "Conde e Gandarela", "Costa", "Creixomil", "Fermentões", "Gonça", "Gondar", "Guardizela", "Infantas", "Leitões, Oleiros e Figueiredo", "Longos", "Lordelo", "Mesão Frio", "Moreira de Cónegos", "Nespereira", "Oliveira, São Paio e São Sebastião", "Pencelo", "Pinheiro", "Polvoreira", "Ponte", "Prazins (Santa Eufémia)", "Prazins (Santo Tirso)", "Ronfe", "Sande (São Lourenço e Balazar)", "Sande (São Martinho)", "Sande (Vila Nova e São Clemente)", "São Torcato", "Selho (São Cristóvão)", "Selho (São Jorge)", "Selho (São Lourenço)", "Serzedelo", "Serzedo e Calvos", "Silvares", "Tabuadelo e São Faustino", "Urgezes", "Briteiros Santo Estêvão e Donim", "Briteiros São Salvador e Briteiros Santa Leocádia", "Atães e Rendufe", "Souto Santa Maria, Souto São Salvador e Gondomar"],
        "Póvoa de Lanhoso": ["Águas Santas e Moure", "Ajude", "Brunhais", "Calvos e Frades", "Campos e Louredo", "Covelas", "Esperança e Brunhais", "Ferreiros", "Fonte Arcada e Oliveira", "Galegos", "Garfe", "Geraz do Minho", "Lanhoso", "Monsul", "Póvoa de Lanhoso (Nossa Senhora do Amparo)", "Rendufinho", "Santo Emilião", "São João de Rei", "Serzedelo", "Sobradelo da Goma", "Taíde", "Travassos", "Verim, Friande e Ajude", "Vilela"],
        "Terras do Bouro": ["Balança", "Campo do Gerês", "Carvalheira", "Chamoim e Vilar", "Chorense e Monte", "Cibões e Brufe", "Covide", "Gondoriz", "Moimenta", "Ribeira", "Rio Caldo", "Souto", "Valdosende", "Vilar da Veiga"],
        "Vieira do Minho": ["Anissó e Soutelo", "Anjos", "Caniçada e Soengas", "Cantelães", "Cova", "Eira Vedra", "Guilhofrei", "Louredo", "Mosteiro", "Parada de Bouro", "Pinheiro", "Rossas", "Ruivães e Campos", "Salamonde", "Tabuaças", "Ventosa e Cova", "Vieira do Minho", "Vilar Chão"],
        "Vila Nova de Famalicão": ["Abade de Vermoim", "Antas e Abade de Vermoim", "Arnoso (Santa Maria e Santa Eulália) e Sezures", "Bairro", "Bente", "Brufe", "Cabeçudos", "Calendário", "Carreira e Bente", "Castelões", "Cavalões", "Cruz", "Delães", "Esmeriz e Cabeçudos", "Fradelos", "Gavião", "Gondifelos, Cavalões e Outiz", "Joane", "Landim", "Lemenhe, Mouquim e Jesufrei", "Louro", "Lousado", "Mogege", "Nine", "Novais e Ruivães", "Oliveira (Santa Maria)", "Oliveira (São Mateus)", "Pedome", "Pousada de Saramagos", "Requião", "Riba de Ave", "Ribeirão", "Seide", "Vermoim", "Vila Nova de Famalicão e Calendário", "Vilarinho das Cambas"],
        "Vila Verde": ["Aboim da Nóbrega e Gondomar", "Atiães", "Barbudo", "Cabanelas", "Carreiras (Santiago e São Miguel)", "Cervães", "Coucieiro", "Dossãos", "Duas Igrejas", "Esqueiros, Nevogilde e Travassós", "Freiriz", "Geme", "Goães", "Godinhaços", "Lage", "Lanhas", "Marrancos e Arcozelo", "Moure", "Oleiros", "Parada de Gatim", "Pico", "Pico de Regalados, Gondiães e Mós", "Ponte", "Portela das Cabras", "Ribeira do Neiva (Duque, Duas Igrejas, Godinhaços, Pedregais e Rio Mau)", "Sabariz", "Sande, Vilarinho, Barros e Gomide", "São Vicente do Bico", "Turiz", "Valdreu", "Valões", "Vila de Prado", "Vila Verde e Barbudo"],
        "Vizela": ["Caldas de Vizela (São Miguel e São João)", "Infias", "Santa Eulália", "Santo Adrião de Vizela", "Tagilde e Vizela (São Paio)"]
    },
    'Distrito de Bragança': {
        'Concelho de Alfândega da Fé': ['Agrobom', 'Alfândega da Fé', 'Cerejais', 'Eucísia', 'Ferradosa', 'Gebelim', 'Gouveia', 'Parada', 'Pombal', 'Saldonha', 'Sambade', 'Sendim da Ribeira', 'Sendim da Serra', 'Soeima', 'Vale Pereiro', 'Vales', 'Valverde', 'Vilar Chão', 'Vilarelhos', 'Vilares de Vilariça'],
        'Concelho Bragança': ['Alfaião', 'Aveleda', 'Babe', 'Baçal', 'Calvelhe', 'Carragosa', 'Carrazedo', 'Castrelos', 'Castro de Avelãs', 'Coelhoso', 'Deilão', 'Donai', 'Espinhosela', 'Faílde', 'França', 'Gimonde', 'Gondesende', 'Gostei', 'Grijó de Parada', 'Izeda', 'Macedo do Mato', 'Meixedo', 'Milhão', 'Mós', 'Nogueira', 'Outeiro', 'Parada', 'Paradinha Nova', 'Parâmio', 'Pinela', 'Pombares', 'Quintanilha', 'Quintela de Lampaças', 'Rabal', 'Rebordainhos', 'Rebordãos', 'Rio de Onor', 'Rio Frio', 'Salsas', 'Samil', 'Santa Comba de Rossas', 'Santa Maria (Bragança)', 'São Julião de Palácios', 'São Pedro de Sarracenos', 'Sé (Bragança)', 'Sendas', 'Serapicos', 'Sortes', 'Zoio'],
        'Concelho de Freixo de Espada à Cinta': ['Fornos', 'Freixo de Espada à Cinta', 'Lagoaça', 'Ligares', 'Mazouco', 'Poiares'],
        'Concelho de Macedo de Cavaleiros': ['Ala', 'Amendoeira', 'Arcas', 'Bagueixe', 'Bornes', 'Burga', 'Carrapatas', 'Castelãos', 'Chacim', 'Cortiços', 'Corujas', 'Edroso', 'Espadanedo', 'Ferreira', 'Grijó', 'Lagoa', 'Lamalonga', 'Lamas', 'Lombo', 'Macedo de Cavaleiros', 'Morais', 'Murçós', 'Olmos', 'Peredo', 'Podence', 'Salselas', 'Santa Combinha', 'Sezulfe', 'Soutelo Mourisco', 'Talhas', 'Talhinhas', 'Vale Benfeito', 'Vale da Porca', 'Vale de Prados', 'Vilar do Monte', 'Vilarinho de Agrochão', 'Vilarinho do Monte', 'Vinhas'],
        'Concelho de Miranda do Douro': ['Águas Vivas', 'Atenor', 'Cicouro', 'Constantim', 'Duas Igrejas', 'Genísio', 'Ifanes', 'Malhadas', 'Miranda do Douro', 'Palaçoulo', 'Paradela', 'Picote', 'Póvoa', 'São Martinho de Angueira', 'Sendim', 'Silva', 'Vila Chã de Braciosa'],
        'Concelho de Mirandela': ['Abambres', 'Abreiro', 'Aguieiras', 'Alvites', 'Avantos', 'Avidagos', 'Barcel', 'Bouça', 'Cabanelas', 'Caravelas', 'Carvalhais', 'Cedães', 'Cobro', 'Fradizela', 'Franco', 'Frechas', 'Freixeda', 'Lamas de Orelhão', 'Marmelos', 'Mascarenhas', 'Mirandela', 'Múrias', 'Navalho', 'Passos', 'Pereira', 'Romeu', 'São Pedro Velho', 'São Salvador', 'Suçães', 'Torre de Dona Chama', 'Vale de Asnes', 'Vale de Gouvinhas', 'Vale de Salgueiro', 'Vale de Telhas', 'Valverde', 'Vila Boa', 'Vila Verde'],
        'Concelho de Mogadouro': ['Azinhoso', 'Bemposta', 'Bruçó', 'Brunhoso', 'Brunhozinho', 'Castanheira', 'Castelo Branco', 'Castro Vicente', 'Meirinhos', 'Mogadouro', 'Paradela', 'Penas Róias', 'Peredo da Bemposta', 'Remondes', 'Saldanha', 'Sanhoane', 'São Martinho do Peso', 'Soutelo', 'Tó', 'Travanca', 'Urrós', 'Vale da Madre', 'Vale de Porco', 'Valverde', 'Ventozelo', 'Vila de Ala', 'Vilar de Rei', 'Vilarinho dos Galegos'],
        'Concelho de Torre de Moncorvo': ['Açoreira', 'Adeganha', 'Cabeça Boa', 'Cardanha', 'Carviçais', 'Castedo', 'Felgar', 'Felgueiras', 'Horta da Vilariça', 'Larinho', 'Lousa', 'Maçores', 'Mós', 'Peredo dos Castelhanos', 'Souto da Velha', 'Torre de Moncorvo', 'Urrós'],
        'Concelho de Vila Flor': ['Assares', 'Benlhevai', 'Candoso', 'Carvalho de Egas', 'Freixiel', 'Lodões', 'Mourão', 'Nabo', 'Róios', 'Samões', 'Sampaio', 'Santa Comba de Vilariça', 'Seixo de Manhoses', 'Trindade', 'Vale de Torno', 'Vale Frechoso', 'Vila Flor', 'Vilarinho das Azenhas', 'Vilas Boas'],
        'Concelho do Vimioso': ['Algoso', 'Angueira', 'Argozelo', 'Avelanoso', 'Caçarelhos', 'Campo de Víboras', 'Carção', 'Matela', 'Pinelo', 'Santulhão', 'Uva', 'Vale de Frades', 'Vilar Seco', 'Vimioso'],
        'Concelho de Vinhais': ['Agrochão', 'Alvaredos', 'Candedo', 'Celas', 'Curopos', 'Edral', 'Edrosa', 'Ervedosa', 'Fresulfe', 'Mofreita', 'Montouto', 'Moimenta', 'Nunes', 'Ousilhão', 'Paçó', 'Penhas Juntas', 'Pinheiro Novo', 'Quirás', 'Rebordelo', 'Santa Cruz', 'Santalha', 'São Jomil', 'Sobreiró de Baixo', 'Soeira', 'Travanca', 'Tuizelo', 'Vale das Fontes', 'Vale de Janeiro', 'Vila Boa de Ousilhão', 'Vila Verde', 'Vilar de Lomba', 'Vilar de Ossos', 'Vilar de Peregrinos', 'Vilar Seco de Lomba', 'Vinhais']
    },
    'Distrito de Castelo Branco': {
        'Concelho de Belmonte': ['Belmonte', 'Caria', 'Colmeal da Torre', 'Inguias', 'Maçainhas'],
        'Concelho de Castelo Branco': ['Alcains', 'Almaceda', 'Benquerenças', 'Cafede', 'Castelo Branco', 'Cebolais de Cima', 'Escalos de Baixo', 'Escalos de Cima', 'Freixial do Campo', 'Juncal do Campo', 'Lardosa', 'Louriçal do Campo', 'Lousa', 'Malpica do Tejo', 'Mata', 'Monforte da Beira', 'Ninho do Açor', 'Póvoa de Rio de Moinhos'],
        'Concelho da Covilhã': ['Aldeia de São Francisco de Assis', 'Aldeia do Souto', 'Barco', 'Boidobra (Covilhã)', 'Canhoso', 'Cantar-Galo (Covilhã)', 'Casegas', 'Conceição (Covilhã)', 'Cortes do Meio', 'Coutada', 'Dominguizo', 'Erada', 'Ferro', 'Orjais', 'Ourondo', 'Paul', 'Peraboa', 'Peso', 'Santa Maria (Covilhã)', 'São Jorge da Beira', 'São Martinho (Covilhã)', 'São Pedro (Covilhã)', 'Sarzedo', 'Sobral de São Miguel', 'Teixoso', 'Tortosendo', 'Unhais da Serra', 'Vale Formoso', 'Vales do Rio', 'Verdelhos', 'Vila do Carvalho (Covilhã)'],
        'Concelho do Fundão': ['Alcaide', 'Alcaria', 'Alcongosta', 'Aldeia de Joanes', 'Aldeia Nova do Cabo', 'Alpedrinha', 'Atalaia do Campo', 'Barroca', 'Bogas de Baixo', 'Bogas de Cima', 'Capinha', 'Castelejo', 'Castelo Novo', 'Donas', 'Enxames', 'Escarigo', 'Fatela', 'Fundão', 'Janeiro de Cima', 'Lavacolhos', 'Mata da Rainha', 'Orca', 'Pêro Viseu', 'Póvoa de Atalaia', 'Salgueiro', 'Silvares', 'Soalheira', 'Souto da Casa', 'Telhado', 'Vale de Prazeres', 'Valverde'],
        'Concelho de Idanha-a-Nova': ['Alcafozes', 'Aldeia de Santa Margarida', 'Idanha-a-Nova', 'Idanha-a-Velha', 'Ladoeiro', 'Medelim', 'Monfortinho', 'Monsanto', 'Oledo', 'Penha Garcia', 'Proença-a-Velha', 'Rosmaninhal', 'Salvaterra do Extremo', 'São Miguel de Acha', 'Segura', 'Toulões', 'Zebreira'],
        'Concelho de Oleiros': ['Álvaro', 'Amieira', 'Cambas', 'Estreito', 'Isna', 'Madeirã', 'Mosteiro', 'Oleiros', 'Orvalho', 'Sarnadas de São Simão', 'Sobral', 'Vilar Barroco'],
        'Concelho de Penamacor': ['Águas', 'Aldeia de João Pires', 'Aldeia do Bispo', 'Aranhas', 'Bemposta', 'Benquerença', 'Meimão', 'Meimoa', 'Pedrógão de São Pedro', 'Penamacor', 'Salvador', 'Vale da Senhora da Póvoa'],
        'Concelho de Proença-a-Nova': ['Alvito da Beira', 'Montes da Senhora', 'Peral', 'Proença-a-Nova', 'São Pedro do Esteval', 'Sobreira Formosa'],
        'Concelho da Sertã': ['Sertã'],
        'Concelho de Vila de Rei': ['Fundada', 'São João do Peso', 'Vila de Rei'],
        'Concelho de Vila Velha de Ródão': ['Fratel', 'Perais', 'Sarnadas de Ródão', 'Vila Velha de Ródão', 'Retaxo', 'Salgueiro do Campo', 'Santo André das Tojeiras', 'São Vicente da Beira', 'Sarzedas', 'Sobral do Campo', 'Tinalhas'],
    },
    'Distrito de Coimbra': {
        'Concelhos': ['Arganil', 'Cantanhede', 'Coimbra', 'Condeixa-a-Nova', 'Figueira da Foz', 'Góis', 'Lousã', 'Mira', 'Miranda do Corvo', 'Montemor-o-Velho', 'Oliveira do Hospital', 'Pampilhosa da Serra', 'Penacova', 'Penela', 'Soure', 'Tábua', 'Vila Nova de Poiares'],
        'Concelho de Arganil': ['Anceriz', 'Arganil', 'Barril de Alva', 'Benfeita', 'Celavisa', 'Cepos', 'Cerdeira', 'Coja', 'Folques', 'Moura da Serra', 'Piódão', 'Pomares', 'Pombeiro da Beira', 'São Martinho da Cortiça', 'Sarzedo', 'Secarias', 'Teixeira', 'Vila Cova de Alva'],
        'Concelho de Cantanhede': ['Ançã', 'Bolho', 'Cadima', 'Camarneira', 'Cantanhede', 'Cordinhã', 'Corticeiro de Cima', 'Covões', 'Febres', 'Murtede', 'Ourentã', 'Outil', 'Pocariça', 'Portunhos', 'Sanguinheira', 'São Caetano', 'Sepins', 'Tocha', 'Vilamar'],
        'Concelho de Coimbra': ['Almalaguês', 'Almedina (Coimbra)', 'Ameal', 'Antanhol', 'Antuzede (Coimbra)', 'Arzila', 'Assafarge', 'Botão', 'Brasfemes', 'Castelo Viegas', 'Ceira', 'Cernache', 'Eiras (Coimbra)', 'Lamarosa', 'Ribeira de Frades (Coimbra)', 'Santa Clara (Coimbra)', 'Santa Cruz (Coimbra)', 'Santo António dos Olivais (Coimbra)', 'São Bartolomeu (Coimbra)', 'São João do Campo', 'São Martinho de Árvore', 'São Martinho do Bispo (Coimbra)', 'São Paulo de Frades (Coimbra)', 'São Silvestre', 'Sé Nova (Coimbra)', 'Souselas', 'Taveiro', 'Torre de Vilela', 'Torres do Mondego', 'Trouxemil', 'Vil de Matos'],
        'Concelho de Condeixa-a-Nova': ['Anobra', 'Belide', 'Bem da Fé', 'Condeixa-a-Nova', 'Condeixa-a-Velha', 'Ega', 'Furadouro', 'Sebal', 'Vila Seca', 'Zambujal'],
        'Concelho da Figueira da Foz': ['Alhadas', 'Alqueidão', 'Bom Sucesso', 'Borda do Campo', 'Brenha', 'Buarcos (Figueira da Foz)', 'Ferreira-a-Nova', 'Lavos', 'Maiorca (Figueira da Foz)', 'Marinha das Ondas', 'Moinhos da Gândara', 'Paião', 'Quiaios', 'Santana (Figueira da Foz)', 'São Julião da Figueira da Foz (Figueira da Foz)', 'São Pedro (Figueira da Foz)', 'Tavarede (Figueira da Foz)', 'Vila Verde (Figueira da Foz)'],
        'Concelho de Góis': ['Alvares', 'Cadafaz', 'Colmeal', 'Góis', 'Vila Nova do Ceira'],
        'Concelho da Lousã': ['Casal de Ermio', 'Foz de Arouce', 'Gândaras', 'Lousã', 'Serpins', 'Vilarinho (Lousã)'],
        'Concelho de Mira': ['Carapelhos', 'Mira', 'Praia de Mira', 'Seixo'],
        'Concelho de Miranda do Corvo': ['Lamas', 'Miranda do Corvo', 'Rio Vide', 'Semide (da qual faz parte a aldeia do Senhor da Serra)', 'Vila Nova'],
        'Concelho de Montemor-o-Velho': ['Abrunheira', 'Arazede', 'Carapinheira', 'Ereira', 'Gatões', 'Liceia', 'Meãs do Campo', 'Montemor-o-Velho', 'Pereira', 'Santo Varão', 'Seixo de Gatões', 'Tentúgal', 'Verride', 'Vila Nova da Barca'],
        'Concelho de Oliveira do Hospital': ['Aldeia das Dez', 'Alvoco das Várzeas', 'Avô', 'Bobadela', 'Ervedal', 'Lagares da Beira', 'Lagos da Beira', 'Lajeosa', 'Lourosa', 'Meruge', 'Nogueira do Cravo', 'Oliveira do Hospital', 'Penalva de Alva', 'Santa Ovaia', 'São Gião', 'São Paio de Gramaços', 'São Sebastião da Feira', 'Seixo da Beira', 'Travanca de Lagos', 'Vila Franca da Beira', 'Vila Pouca da Beira'],
        'Concelho de Pampilhosa da Serra': ['Cabril', 'Dornelas do Zêzere', 'Fajão', 'Janeiro de Baixo', 'Machio', 'Pampilhosa da Serra', 'Pessegueiro', 'Portela do Fojo', 'Unhais-o-Velho', 'Vidual'],
        'Concelho de Penacova': ['Carvalho', 'Figueira de Lorvão', 'Friúmes', 'Lorvão', 'Oliveira do Mondego', 'Paradela', 'Penacova', 'São Paio do Mondego', 'São Pedro de Alva', 'Sazes do Lorvão', 'Travanca do Mondego'],
        'Concelho de Penela': ['Cumeeira', 'Espinhal', 'Podentes', 'Rabaçal', 'Santa Eufémia (Penela)', 'São Miguel (Penela)'],
        'Concelho de Soure': ['Alfarelos', 'Brunhós', 'Degracias', 'Figueiró do Campo', 'Gesteira', 'Granja do Ulmeiro', 'Pombalinho', 'Samuel', 'Soure', 'Tapéus', 'Vila Nova de Anços', 'Vinha da Rainha'],
        'Concelho de Tábua': ['Ázere', 'Candosa', 'Carapinha', 'Covas', 'Covelo', 'Espariz', 'Meda de Mouros', 'Midões', 'Mouronho', 'Pinheiro de Coja', 'Póvoa de Midões', 'São João da Boa Vista', 'Sinde', 'Tábua', 'Vila Nova de Oliveirinha'],
        'Concelho da Vila Nova de Poiares': ['Arrifana', 'Lavegadas', 'Poiares (Vila Nova de Poiares)', 'São Miguel de Poiares'],
    },
    'Distrito de Évora': {
        'Concelho do Alandroal': ['Nossa Senhora da Conceição', 'Capelins (Santo António)', 'Juromenha (Nossa Senhora do Loreto)', 'São Brás dos Matos (Mina do Bugalho)', 'Santiago Maior (Alandroal)', 'Terena (São Pedro)'],
        'Concelho de Arraiolos': ['Arraiolos', 'Igrejinha', 'Sabugueiro', 'Santa Justa', 'São Gregório', 'São Pedro de Gafanhoeira', 'Vimieiro'],
        'Concelho de Borba': ['Matriz (Borba)', 'Orada', 'Rio de Moinhos', 'São Bartolomeu (Borba)'],
        'Concelho de Estremoz': ['Arcos', 'Évora Monte', 'Glória', 'Santa Maria (Estremoz)', 'Santa Vitória do Ameixial', 'Santo André (Estremoz)', 'Santo Estêvão', 'São Bento de Ana Loura', 'São Bento do Ameixial', 'São Bento do Cortiço', 'São Domingos de Ana Loura', 'São Lourenço de Mamporcão', 'Veiros'],
        'Concelho de Évora': ['Bacelo', 'Canaviais (Évora)', 'Horta das Figueiras (Évora)', 'Malagueira (Évora)', 'Nossa Senhora da Boa Fé', 'Nossa Senhora da Graça do Divor', 'Nossa Senhora da Tourega', 'Nossa Senhora de Guadalupe', 'Nossa Senhora de Machede', 'Santo Antão (Évora)', 'São Bento do Mato', 'São Mamede (Évora)', 'São Manços', 'São Miguel de Machede', 'São Sebastião da Giesteira', 'São Vicente do Pigeiro', 'Sé e São Pedro (Évora)', 'Senhora da Saúde (Évora)', 'Torre de Coelheiros'],
        'Concelho de Montemor-o-Novo': ['Cabrela', 'Ciborro', 'Cortiçadas', 'Foros de Vale de Figueira', 'Lavre', 'Nossa Senhora da Vila (Montemor-o-Novo)', 'Nossa Senhora do Bispo (Montemor-o-Novo)', 'Santiago do Escoural', 'São Cristóvão', 'Silveiras'],
        'Concelho de Mora': ['Brotas', 'Cabeção', 'Mora', 'Pavia'],
        'Concelho de Mourão': ['Granja', 'Luz', 'Mourão'],
        'Concelho de Portel': ['Alqueva', 'Amieira', 'Monte do Trigo', 'Oriola', 'Portel', 'Santana', 'São Bartolomeu do Outeiro', 'Vera Cruz'],
        'Concelho do Redondo': ['Montoito', 'Redondo'],
        'Concelho de Reguengos de Monsaraz': ['Campinho', 'Campo', 'Corval', 'Monsaraz', 'Reguengos de Monsaraz'],
        'Concelho de Vendas Novas': ['Landeira', 'Vendas Novas'],
        'Concelho de Viana do Alentejo': ['Aguiar', 'Alcáçovas', 'Viana do Alentejo'],
        'Concelho de Vila Viçosa': ['Bencatel', 'Ciladas', 'Conceição (Vila Viçosa)', 'Pardais', 'São Bartolomeu (Vila Viçosa)'],
    },
    'Distrito de Faro': {
        'Concelho de Albufeira': ['Albufeira', 'Ferreiras', 'Guia', 'Olhos de Água', 'Paderne'],
        'Concelho de Alcoutim': ['Alcoutim', 'Giões', 'Martim Longo', 'Pereiro', 'Vaqueiros'],
        'Concelho de Aljezur': ['Aljezur', 'Bordeira', 'Odeceixe', 'Rogil'],
        'Concelho de Castro Marim': ['Altura', 'Azinhal', 'Castro Marim', 'Odeleite'],
        'Concelho de Faro': ['Conceição', 'Estoi', 'Montenegro', 'Santa Bárbara de Nexe', 'São Pedro (Faro)', 'Sé (Faro)'],
        'Concelho de Lagoa': ['Carvoeiro', 'Estômbar', 'Ferragudo', 'Lagoa', 'Parchal', 'Porches'],
        'Concelho de Lagos': ['Barão de São João', 'Bensafrim', 'Luz', 'Odiáxere', 'Santa Maria (Lagos)', 'São Sebastião (Lagos)'],
        'Concelho de Loulé': ['Almancil', 'Alte', 'Ameixial', 'Benafim', 'Boliqueime', 'Quarteira', 'Querença', 'Salir', 'São Clemente (Loulé)', 'São Sebastião (Loulé)', 'Tôr'],
        'Concelho de Monchique': ['Alferce', 'Marmelete', 'Monchique'],
        'Concelho de Olhão': ['Fuseta', 'Moncarapacho', 'Olhão', 'Pechão (Olhão)', 'Quelfes (Olhão)'],
        'Concelho de Portimão': ['Alvor', 'Mexilhoeira Grande', 'Portimão'],
        'Concelho de São Brás de Alportel': ['São Brás de Alportel'],
        'Concelho de Silves': ['Alcantarilha', 'Algoz', 'Armação de Pêra', 'Pêra', 'São Bartolomeu de Messines', 'São Marcos da Serra', 'Silves', 'Tunes'],
        'Concelho de Tavira': ['Cabanas de Tavira', 'Cachopo', 'Conceição', 'Luz de Tavira', 'Santa Catarina da Fonte do Bispo', 'Santa Luzia', 'Santa Maria (Tavira)', 'Santiago (Tavira)', 'Santo Estêvão'],
        'Concelho de Vila do Bispo': ['Barão de São Miguel', 'Budens', 'Raposeira', 'Sagres', 'Vila do Bispo'],
        'Concelho de Vila Real de Santo António': ['Monte Gordo', 'Vila Nova de Cacela', 'Vila Real de Santo António'],
    },
    'Distrito da Guarda': {
        'Concelho de Aguiar da Beira': ['Aguiar da Beira', 'Carapito', 'Cortiçada', 'Coruche', 'Dornelas', 'Eirado', 'Forninhos', 'Gradiz', 'Pena Verde', 'Pinheiro', 'Sequeiros', 'Souto de Aguiar da Beira', 'Valverde', 'Cavaca (Aguiar da Beira)'],
        'Concelho de Almeida': ['Ade', 'Aldeia Nova', 'Almeida', 'Amoreira', 'Azinhal', 'Cabreira', 'Castelo Bom', 'Castelo Mendo', 'Freineda', 'Freixo', 'Junça', 'Leomil', 'Malhada Sorda', 'Malpartida', 'Mesquitela', 'Mido', 'Miuzela', 'Monte Perobolço', 'Nave de Haver', 'Naves', 'Parada', 'Peva', 'Porto de Ovelha', 'São Pedro de Rio Seco', 'Senouras', 'Vale da Mula', 'Vale de Coelha', 'Vale Verde', 'Vilar Formoso'],
        'Concelho de Celorico da Beira': ['Açores', 'Baraçal', 'Cadafaz', 'Carrapichana', 'Casas do Soeiro', 'Cortiçô da Serra', 'Forno Telheiro', 'Lajeosa do Mondego', 'Linhares', 'Maçal do Chão', 'Mesquitela', 'Minhocal', 'Prados', 'Rapa', 'Ratoeira', 'Salgueirais', 'Santa Maria', 'São Pedro', 'Vale de Azares', 'Velosa', 'Vide Entre Vinhas', 'Vila Boa do Mondego'],
        'Concelho de Figueira de Castelo Rodrigo': ['Algodres', 'Almofala', 'Castelo Rodrigo', 'Cinco Vilas', 'Colmeal', 'Escalhão', 'Escarigo', 'Figueira de Castelo Rodrigo', 'Freixeda de Torrão', 'Mata de Lobos', 'Penha da Águia', 'Quintã de Pêro Martins', 'Reigada', 'Vale de Alfonsinho', 'Vermiosa', 'Vilar de Amargo', 'Vilar Torpim'],
        'Concelho de Fornos de Algodres': ['Algodres', 'Casal Vasco', 'Cortiçô', 'Figueiró da Granja', 'Fornos de Algodres', 'Fuinhas', 'Infias', 'Juncais', 'Maceira', 'Matança', 'Muxagata', 'Queiriz', 'Sobral Pichorro', 'Vila Chã', 'Vila Ruiva', 'Vila Soeiro do Chão'],
        'Concelho de Gouveia': ['Aldeias', 'Arcozelo', 'Cativelos', 'Figueiró da Serra', 'Folgosinho', 'Freixo da Serra', 'Lagarinhos', 'Mangualde da Serra', 'Melo', 'Moimenta da Serra', 'Nabais', 'Nespereira', 'Paços da Serra', 'Ribamondego', 'Rio Torto', 'São Julião (Gouveia)', 'São Paio', 'São Pedro (Gouveia)', 'Vila Cortês da Serra', 'Vila Franca da Serra', 'Vila Nova de Tazem', 'Vinhó'],
        'Concelho da Guarda': ['Adão', 'Albardo', 'Aldeia do Bispo', 'Aldeia Viçosa', 'Alvendre', 'Arrifana', 'Avelãs da Ribeira', 'Avelãs de Ambom', 'Benespera', 'Carvalhal Meão', 'Casal de Cinza', 'Castanheira', 'Cavadoude', 'Codesseiro', 'Corujeira', 'Faia', 'Famalicão', 'Fernão Joanes', 'Gagos', 'Gonçalo', 'Gonçalo Bocas', 'João Antão', 'Maçainhas', 'Marmeleiro', 'Meios', 'Mizarela', 'Monte Margarida', 'Panóias de Cima', 'Pega', 'Pêra do Moço', 'Pêro Soares', 'Porto da Carne', 'Pousada', 'Ramela', 'Ribeira dos Carinhos', 'Rocamondo', 'Rochoso', 'Santana da Azinha', 'São Miguel da Guarda (Guarda)', 'São Miguel de Jarmelo', 'São Pedro de Jarmelo', 'São Vicente', 'Sé', 'Seixo Amarelo', 'Sobral da Serra', 'Trinta', 'Vale de Estrela', 'Valhelhas', 'Vela', 'Videmonte', 'Vila Cortês do Mondego', 'Vila Fernando', 'Vila Franca do Deão', 'Vila Garcia', 'Vila Soeiro'],
        'Concelho de Manteigas': ['Sameiro', 'Santa Maria (Manteigas)', 'São Pedro (Manteigas)', 'Vale de Amoreira'],
        'Concelho de Meda': ['Aveloso', 'Barreira', 'Carvalhal', 'Casteição', 'Coriscada', 'Fonte Longa', 'Longroiva', 'Marialva', 'Meda', 'Outeiro de Gatos', 'Pai Penela', 'Poço do Canto', 'Prova', 'Rabaçal', 'Ranhados', 'Vale Flor'],
        'Concelho de Pinhel': ['Alverca da Beira', 'Atalaia', 'Azevo', 'Bogalhal', 'Bouça Cova', 'Cerejo', 'Cidadelhe', 'Ervas Tenras', 'Ervedosa', 'Freixedas', 'Gouveia', 'Lamegal', 'Lameiras', 'Manigoto', 'Pala', 'Pereiro', 'Pinhel', 'Pínzio', 'Pomares', 'Póvoa de El-Rei', 'Safurdão', 'Santa Eufémia', 'Sorval', 'Souro Pires', 'Valbom', 'Vale de Madeira', 'Vascoveiro'],
        'Concelho do Sabugal': ['Águas Belas', 'Aldeia da Ponte', 'Aldeia da Ribeira', 'Aldeia de Santo António', 'Aldeia do Bispo', 'Aldeia Velha', 'Alfaiates', 'Badamalos', 'Baraçal', 'Bendada', 'Bismula', 'Casteleiro', 'Cerdeira', 'Fóios', 'Forcalhos', 'Lajeosa', 'Lomba', 'Malcata', 'Moita', 'Nave', 'Pena Lobo', 'Pousafoles do Bispo', 'Quadrazais', 'Quinta de São Bartolomeu', 'Rapoula do Côa', 'Rebolosa', 'Rendo', 'Ruivós', 'Ruvina', 'Sabugal', 'Santo Estêvão', 'Seixo do Côa', 'Sortelha', 'Souto', 'Vale das Éguas', 'Vale de Espinho', 'Vale Longo', 'Vila Boa', 'Vila do Touro', 'Vilar Maior'],
        'Concelho de Seia': ['Alvoco da Serra', 'Cabeça', 'Carragozela', 'Folhadosa', 'Girabolhos', 'Lajes', 'Lapa dos Dinheiros', 'Loriga', 'Paranhos da Beira', 'Pinhanços', 'Sabugueiro', 'Sameice', 'Sandomil', 'Santa Comba', 'Santa Eulália', 'Santa Marinha', 'Santiago', 'São Martinho', 'São Romão', 'Sazes da Beira', 'Seia', 'Teixeira', 'Torrozelo', 'Tourais', 'Travancinha', 'Valezim', 'Várzea de Meruge', 'Vide', 'Vila Cova à Coelheira'],
        'Concelho de Trancoso': ['Aldeia Nova', 'Carnicães', 'Castanheira', 'Cogula', 'Cótimos', 'Feital', 'Fiães', 'Freches', 'Granja', 'Guilheiro', 'Moimentinha', 'Moreira de Rei', 'Palhais', 'Póvoa do Concelho', 'Reboleiro', 'Rio de Mel', 'Santa Maria (Trancoso)', 'São Pedro (Trancoso)', 'Sebadelhe da Serra', 'Souto Maior', 'Tamanhos', 'Terrenho', 'Torre do Terrenho', 'Torres', 'Valdujo', 'Vale do Seixo', 'Vila Franca das Naves', 'Vila Garcia', 'Vilares'],
        'Concelho de Vila Nova de Foz Côa': ['Almendra', 'Castelo Melhor', 'Cedovim', 'Chãs', 'Custóias', 'Freixo de Numão', 'Horta', 'Mós', 'Murça', 'Muxagata', 'Numão', 'Santa Comba', 'Santo Amaro', 'Sebadelhe', 'Seixas', 'Touça', 'Vila Nova de Foz Côa'],
    },
    "Distrito de Leiria": {
        "Alcobaça": ["Alcobaça e Vestiaria", "Alfeizerão", "Aljubarrota (Prazeres e São Vicente)", "Bárrio", "Benedita", "Cela", "Coz, Alpedriz e Montes", "Évora de Alcobaça", "Maiorga", "Pataias e Martingança", "São Martinho do Porto", "Turquel", "Vimeiro"],
        "Alvaiázere": ["Almoster", "Alvaiázere", "Maçãs de Caminho", "Maçãs de Dona Maria", "Pelmá", "Pussos São Pedro", "Rego da Murta"],
        "Ansião": ["Alvorge", "Ansião", "Avelar", "Chão de Couce", "Pousaflores", "Santiago da Guarda"],
        "Batalha": ["Batalha", "Golpilheira", "Reguengo do Fetal", "São Mamede"],
        "Bombarral": ["Bombarral e Vale Covo", "Carvalhal", "Pó", "Roliça"],
        "Caldas da Rainha": ["A-dos-Francos", "Alvorninha", "Carvalhal Benfeito", "Foz do Arelho", "Landal", "Nadadouro", "Nossa Senhora do Pópulo, Coto e São Gregório", "Salir de Matos", "Salir do Porto", "Santa Catarina", "Santo Onofre e Serra do Bouro", "Tornada e Salir do Porto", "Vidais"],
        "Castanheira de Pera": ["Castanheira de Pera e Coentral"],
        "Figueiró dos Vinhos": ["Aguda", "Arega", "Bairradas", "Campelo", "Figueiró dos Vinhos e Bairradas"],
        "Leiria": ["Amor", "Arrabal", "Azoia", "Bajouca", "Barosa", "Bidoeira de Cima", "Boa Vista", "Caranguejeira", "Coimbrão", "Colmeias e Memória", "Cortes", "Leiria, Pousos, Barreira e Cortes", "Maceira", "Marrazes e Barosa", "Milagres", "Monte Real e Carvide", "Monte Redondo e Carreira", "Ortigosa", "Parceiros e Azoia", "Regueira de Pontes", "Santa Catarina da Serra e Chainça", "Santa Eufémia e Boa Vista", "Souto da Carpalhosa e Ortigosa"],
        "Marinha Grande": ["Marinha Grande", "Moita", "Vieira de Leiria"],
        "Nazaré": ["Famalicão", "Nazaré", "Valado dos Frades"],
        "Óbidos": ["A dos Negros", "Amoreira", "Gaeiras", "Olho Marinho", "Santa Maria, São Pedro e Sobral da Lagoa", "Usseira", "Vau"],
        "Pedrógão Grande": ["Graça", "Pedrógão Grande", "Vila Facaia"],
        "Peniche": ["Atouguia da Baleia", "Ferrel", "Peniche", "Serra d'El-Rei"],
        "Pombal": ["Abiul", "Almagreira", "Carnide", "Carriço", "Guia, Ilha e Mata Mourisca", "Louriçal", "Meirinhas", "Pelariga", "Pombal", "Redinha", "Santiago e São Simão de Litém e Albergaria dos Doze", "Vermoil", "Vila Cã"],
        "Porto de Mós": ["Alcaria", "Alqueidão da Serra", "Alvados e Alcaria", "Arrimal e Mendiga", "Calvaria de Cima", "Juncal", "Mira de Aire", "Pedreiras", "Porto de Mós - São João Baptista e São Pedro", "São Bento", "Serro Ventoso"]
    },
    'Distrito de Lisboa': {
        'Concelho de Alenquer': ['Abrigada', 'Aldeia Galega da Merceana', 'Aldeia Gavinha', 'Cabanas de Torres', 'Cadafais', 'Carnota', 'Carregado', 'Meca', 'Olhalvo', 'Ota', 'Pereiro de Palhacana', 'Ribafria', 'Santo Estêvão (Alenquer)', 'Triana (Alenquer)', 'Ventosa', 'Vila Verde dos Francos'],
        'Concelho da Amadora': ['Alfornelos (Amadora)', 'Alfragide', 'Brandoa', 'Buraca (Amadora)', 'Damaia (Amadora)', 'Falagueira (Amadora)', 'Mina (Amadora)', 'Reboleira (Amadora)', 'São Brás (Amadora)', 'Venda Nova (Amadora)', 'Venteira (Amadora)'],
        'Concelho de Arruda dos Vinhos': ['Arranhó', 'Arruda dos Vinhos', 'Cardosas', 'Santiago dos Velhos'],
        'Concelho da Azambuja': ['Alcoentre', 'Aveiras de Baixo', 'Aveiras de Cima', 'Azambuja', 'Maçussa', 'Manique do Intendente', 'Vale do Paraíso', 'Vila Nova da Rainha', 'Vila Nova de São Pedro'],
        'Concelho do Cadaval': ['Alguber', 'Cadaval', 'Cercal', 'Figueiros', 'Lamas', 'Painho', 'Peral', 'Pêro Moniz', 'Vermelha', 'Vilar'],
        'Concelho de Cascais': ['Alcabideche', 'Carcavelos', 'Cascais', 'Estoril', 'Parede', 'São Domingos de Rana'],
        'Concelho de Lisboa': ['Ajuda (2.º Bairro)', 'Alcântara (2.º Bairro)', 'Alto do Pina (4.º Bairro)', 'Alvalade (3.º Bairro)', 'Ameixoeira (3.º Bairro)', 'Anjos (1.º Bairro)', 'Beato (4.º Bairro)', 'Benfica (3.º Bairro)', 'Campo Grande (3.º Bairro)', 'Campolide (3.º Bairro)', 'Carnide (3.º Bairro)', 'Castelo (1.º Bairro)', 'Charneca (3.º Bairro)', 'Coração de Jesus (1.º Bairro)', 'Encarnação (1.º Bairro)', 'Graça (1.º Bairro)', 'Lapa (2.º Bairro)', 'Lumiar (3.º Bairro)', 'Madalena (1.º Bairro)', 'Mártires (1.º Bairro)', 'Marvila (4.º Bairro)', 'Mercês (Lisboa) (1.º Bairro)', 'Nossa Senhora de Fátima (3.º Bairro)', 'Pena (1.º Bairro)', 'Penha de França (4.º Bairro)', 'Prazeres (2.º Bairro)', 'Sacramento (1.º Bairro)', 'Santa Catarina (1.º Bairro)', 'Santa Engrácia (1.º Bairro)', 'Santa Isabel (2.º Bairro)', 'Santa Justa (1.º Bairro)', 'Santa Maria de Belém (2.º Bairro)', 'Santa Maria dos Olivais (4.º Bairro)', 'Santiago (1.º Bairro)', 'Santo Condestável (2.º Bairro)', 'Santo Estêvão (1.º Bairro)', 'Santos-o-Velho (2.º Bairro)', 'São Cristóvão e São Lourenço (1.º Bairro)', 'São Domingos de Benfica (3.º Bairro)', 'São Francisco Xavier (2.º Bairro)', 'São João (4.º Bairro)', 'São João de Brito (3.º Bairro)', 'São João de Deus (4.º Bairro)', 'São Jorge de Arroios (4.º Bairro)', 'São José (1.º Bairro)', 'São Mamede (1.º Bairro)', 'São Miguel (1.º Bairro)', 'São Nicolau (1.º Bairro)', 'São Paulo (1.º Bairro)', 'São Sebastião da Pedreira (3.º Bairro)', 'São Vicente de Fora (1.º Bairro)', 'Sé (1.º Bairro)', 'Socorro (1.º Bairro)', 'Oriente (4º Bairro)'],
        'Concelho de Loures': ['Apelação', 'Bobadela', 'Bucelas', 'Camarate', 'Fanhões', 'Frielas', 'Loures', 'Lousa', 'Moscavide', 'Portela', 'Prior Velho', 'Sacavém', 'Santa Iria de Azóia', 'Santo Antão do Tojal', 'Santo António dos Cavaleiros', 'São João da Talha', 'São Julião do Tojal', 'Unhos'],
        'Concelho da Lourinhã': ['Atalaia', 'Lourinhã', 'Marteleira', 'Miragaia', 'Moita dos Ferreiros', 'Moledo', 'Reguengo Grande', 'Ribamar', 'Santa Bárbara', 'São Bartolomeu dos Galegos', 'Vimeiro'],
        'Concelho de Mafra': ['Azueira', 'Carvoeira', 'Cheleiros', 'Encarnação', 'Enxara do Bispo', 'Ericeira', 'Gradil', 'Igreja Nova', 'Mafra', 'Malveira', 'Milharado', 'Santo Estêvão das Galés', 'Santo Isidoro', 'São Miguel de Alcainça', 'Sobral da Abelheira', 'Venda do Pinheiro', 'Vila Franca do Rosário'],
        'Concelho de Odivelas': ['Caneças', 'Famões', 'Odivelas', 'Olival Basto', 'Pontinha', 'Póvoa de Santo Adrião', 'Ramada'],
        'Concelho de Oeiras': ['Algés', 'Barcarena', 'Carnaxide', 'Caxias', 'Cruz Quebrada - Dafundo', 'Linda-a-Velha', 'Oeiras e São Julião da Barra', 'Paço de Arcos', 'Porto Salvo', 'Queijas'],
        'Concelho de Sintra': ['Agualva', 'Algueirão - Mem Martins', 'Almargem do Bispo', 'Belas', 'Cacém', 'Casal de Cambra', 'Colares', 'Massamá', 'Mira-Sintra', 'Monte Abraão', 'Montelavar', 'Pêro Pinheiro', 'Queluz', 'Rio de Mouro', 'Santa Maria e São Miguel (Sintra)', 'São João das Lampas', 'São Marcos', 'São Martinho (Sintra)', 'São Pedro de Penaferrim (Sintra)', 'Terrugem'],
        'Concelho do Sobral de Monte Agraço': ['Santo Quintino (Sobral de Monte Agraço)', 'Sapataria', 'Sobral de Monte Agraço'],
        'Concelho de Torres Vedras': ['A dos Cunhados', 'Campelos', 'Carmões', 'Carvoeira', 'Dois Portos', 'Freiria', 'Maceira', 'Matacães', 'Maxial', 'Monte Redondo', 'Outeiro da Cabeça', 'Ponte do Rol', 'Ramalhal', 'Runa', 'Santa Maria do Castelo e São Miguel (Torres Vedras)', 'São Pedro da Cadeira', 'São Pedro e Santiago (Torres Vedras)', 'Silveira', 'Turcifal', 'Ventosa'],
        'Concelho de Vila Franca de Xira': ['Alhandra', 'Alverca do Ribatejo', 'Cachoeiras', 'Calhandriz', 'Castanheira do Ribatejo', 'Forte da Casa', 'Póvoa de Santa Iria', 'São João dos Montes', 'Sobralinho', 'Vialonga', 'Vila Franca de Xira'],
    },
    'Distrito de Portalegre': {
        'Concelho de Alter do Chão': ['Alter do Chão', 'Chancelaria', 'Cunheira', 'Seda'],
        'Concelho de Arronches': ['Assunção (Arronches)', 'Esperança', 'Mosteiros'],
        'Concelho de Avis': ['Alcôrrego', 'Aldeia Velha', 'Avis', 'Benavila', 'Ervedal', 'Figueira e Barros', 'Maranhão', 'Valongo'],
        'Concelho de Campo Maior': ['Nossa Senhora da Expectação (Campo Maior)', 'Nossa Senhora da Graça dos Degolados', 'São João Baptista (Campo Maior)'],
        'Concelho de Castelo de Vide': ['Nossa Senhora da Graça de Póvoa e Meadas', 'Santa Maria da Devesa (Castelo de Vide)', 'Santiago Maior (Castelo de Vide)', 'São João Baptista (Castelo de Vide)'],
        'Concelho do Crato': ['Aldeia da Mata', 'Crato e Mártires (Crato)', 'Flor da Rosa', 'Gáfete', 'Monte da Pedra', 'Vale do Peso'],
        'Concelho de Elvas': ['Ajuda, Salvador e Santo Ildefonso', 'Alcáçova', 'Assunção', 'Barbacena', 'Caia e São Pedro', 'Santa Eulália', 'São Brás e São Lourenço', 'São Vicente e Ventosa', 'Terrugem', 'Vila Boim', 'Vila Fernando'],
        'Concelho de Fronteira': ['Cabeço de Vide', 'Fronteira', 'São Saturnino'],
        'Concelho do Gavião': ['Atalaia', 'Belver', 'Comenda', 'Gavião', 'Margem'],
        'Concelho de Marvão': ['Beirã', 'Santa Maria de Marvão', 'Santo António das Areias', 'São Salvador da Aramenha'],
        'Concelho de Portalegre': ['Alagoa', 'Alegrete', 'Carreiras', 'Fortios', 'Reguengo', 'Ribeira de Nisa', 'São Julião', 'São Lourenço (Portalegre)', 'Sé (Portalegre)', 'Urra'],
        'Concelho de Sousel': ['Cano', 'Casa Branca', 'Santo Amaro', 'Sousel'],
    },
    'Distrito do Porto': {
        'Concelho de Amarante': ['Aboadela', 'Aboim', 'Ansiães', 'Ataíde', 'Bustelo', 'Canadelo', 'Candemil', 'Carneiro', 'Carvalho de Rei', 'Cepelos (Amarante)', 'Chapa', 'Fregim', 'Freixo de Baixo', 'Freixo de Cima', 'Fridão', 'Gatão', 'Gondar', 'Jazente', 'Lomba', 'Louredo', 'Lufrei', 'Madalena (Amarante)', 'Mancelos', 'Oliveira', 'Olo', 'Padronelo', 'Real', 'Rebordelo', 'Salvador do Monte', 'Sanche', 'Santa Cristina de Figueiró', 'Santiago de Figueiró', 'São Gonçalo (Amarante)', 'São Simão de Gouveia', 'Telões', 'Travanca', 'Várzea', 'Vila Caiz', 'Vila Chã do Marão', 'Vila Garcia'],
        'Concelho de Baião': ['Ancede', 'Campelo (Baião)', 'Frende', 'Gestaçô', 'Gove', 'Grilo', 'Loivos da Ribeira', 'Loivos do Monte', 'Mesquinhata', 'Ovil', 'Ribadouro', 'Santa Cruz do Douro', 'Santa Leocádia', 'Santa Marinha do Zêzere', 'São Tomé de Covelas', 'Teixeira', 'Teixeiró', 'Tresouras', 'Valadares', 'Viariz'],
        'Concelho de Felgueiras': ['Aião', 'Airães', 'Borba de Godim', 'Caramos', 'Friande', 'Idães', 'Jugueiros', 'Lagares', 'Lordelo', 'Macieira da Lixa', 'Margaride (Felgueiras)', 'Moure', 'Pedreira', 'Penacova', 'Pinheiro', 'Pombeiro da Ribavizela', 'Rande', 'Refontoura', 'Regilde', 'Revinhade', 'Santão', 'São Jorge de Vizela', 'Sendim', 'Sernande', 'Sousa', 'Torrados', 'Unhão', 'Várzea', 'Varziela', 'Vila Cova da Lixa', 'Vila Fria', 'Vila Verde'],
        'Concelho de Gondomar': ['Baguim do Monte', 'Covelo', 'Fânzeres', 'Foz do Sousa', 'Jovim', 'Lomba', 'Medas', 'Melres', 'Rio Tinto', 'São Cosme (Gondomar)', 'São Pedro da Cova', 'Valbom'],
        'Concelho de Lousada': ['Alvarenga', 'Aveleda', 'Boim', 'Caíde de Rei', 'Casais', 'Cernadelo', 'Covas', 'Cristelos', 'Figueiras', 'Lodares', 'Lustosa', 'Macieira', 'Meinedo', 'Nespereira', 'Nevogilde', 'Nogueira', 'Ordem', 'Pias', 'Santa Margarida de Lousada', 'Santo Estêvão de Barrosas', 'São Miguel de Lousada', 'Silvares', 'Sousela', 'Torno', 'Vilar do Torno e Alentém'],
        'Concelho da Maia': ['Águas Santas', 'Barca', 'Folgosa', 'Gemunde', 'Gondim', 'Gueifães (Maia)', 'Maia', 'Milheirós', 'Moreira', 'Nogueira', 'Pedrouços', 'Santa Maria de Avioso', 'São Pedro de Avioso', 'São Pedro Fins', 'Silva Escura', 'Vermoim (Maia)', 'Vila Nova da Telha'],
        'Concelho de Marco de Canaveses': ['Alpendurada e Matos', 'Ariz', 'Avessadas', 'Banho e Carvalhosa', 'Constance', 'Favões', 'Folhada', 'Fornos', 'Freixo', 'Magrelos', 'Manhuncelos', 'Maureles', 'Paços de Gaiolo', 'Paredes de Viadores', 'Penha Longa', 'Rio de Galinhas', 'Rosem', 'Sande', 'Santo Isidoro', 'São Lourenço do Douro', 'São Nicolau', 'Soalhães', 'Sobretâmega', 'Tabuado', 'Torrão', 'Toutosa', 'Tuias', 'Várzea da Ovelha e Aliviada', 'Várzea do Douro', 'Vila Boa de Quires', 'Vila Boa do Bispo'],
        'Concelho de Matosinhos': ['Custóias', 'Guifões', 'Lavra', 'Leça da Palmeira', 'Leça do Balio', 'Matosinhos', 'Perafita', 'Santa Cruz do Bispo', 'São Mamede de Infesta', 'Senhora da Hora'],
        'Concelho de Paços de Ferreira': ['Arreigad', 'Carvalhosa', 'Codessos', 'Eiriz', 'Ferreira', 'Figueiró', 'Frazão', 'Freamunde', 'Lamoso', 'Meixomil', 'Modelos', 'Paços de Ferreira', 'Penamaior', 'Raimonda', 'Sanfins de Ferreira', 'Seroa'],
        'Concelho de Paredes': ['Aguiar de Sousa', 'Astromil', 'Baltar', 'Beire', 'Besteiros', 'Bitarães', 'Castelões de Cepeda', 'Cete', 'Cristelo', 'Duas Igrejas', 'Gandra', 'Gondalães', 'Louredo', 'Madalena', 'Mouriz', 'Parada de Todeia', 'Rebordosa', 'Recarei', 'São Salvador de Lordelo', 'Sobreira', 'Sobrosa', 'Vandoma', 'Vila Cova de Carros', 'Vilela'],
        'Concelho de Penafiel': ['Abragão', 'Boelhe', 'Bustelo', 'Cabeça Santa', 'Canelas', 'Capela', 'Castelões', 'Croca', 'Duas Igrejas', 'Eja', 'Figueira', 'Fonte Arcada', 'Galegos', 'Guilhufe', 'Irivo', 'Lagares', 'Luzim', 'Marecos', 'Milhundos', 'Novelas', 'Oldrões', 'Paço de Sousa', 'Paredes', 'Penafiel', 'Perozelo', 'Pinheiro', 'Portela', 'Rãs', 'Rio de Moinhos', 'Rio Mau', 'Santa Marta', 'Santiago de Subarrifana', 'São Mamede de Recezinhos', 'São Martinho de Recezinhos', 'Sebolido', 'Urrô', 'Valpedre', 'Vila Cova'],
        'Concelho do Porto': ['Aldoar', 'Bonfim', 'Campanhã', 'Cedofeita', 'Foz do Douro', 'Lordelo do Ouro', 'Massarelos', 'Miragaia', 'Nevogilde', 'Paranhos', 'Ramalde', 'Santo Ildefonso', 'São Nicolau', 'Sé', 'Vitória'],
        'Concelho da Póvoa de Varzim': ['A Ver-o-Mar', 'Aguçadoura', 'Amorim', 'Argivai', 'Balasar', 'Beiriz', 'Estela', 'Laundos', 'Póvoa de Varzim (sede)', 'Navais', 'Rates', 'Terroso'],
        'Concelho de Santo Tirso': ['Agrela', 'Água Longa', 'Areias', 'Burgães', 'Carreira', 'Guimarei', 'Lama', 'Lamelas', 'Monte Córdova', 'Palmeira', 'Rebordões', 'Refojos de Riba de Ave', 'Reguenga', 'Roriz', 'Santa Cristina do Couto', 'Santo Tirso', 'São Mamede de Negrelos', 'São Martinho do Campo', 'São Miguel do Couto', 'São Salvador do Campo', 'São Tomé de Negrelos', 'Sequeiró', 'Vila das Aves', 'Vilarinho'],
        'Concelho da Trofa': ['Alvarelhos', 'Covelas', 'Guidões', 'Muro', 'São Mamede de Coronado', 'São Martinho de Bougado (Trofa)', 'São Romão do Coronado', 'Santiago de Bougado (Trofa)'],
        'Concelho de Valongo': ['Alfena', 'Campo', 'Ermesinde', 'Sobrado', 'Valongo'],
        'Concelho de Vila do Conde': ['Arcos', 'Árvore', 'Aveleda', 'Azurara', 'Bagunte', 'Canidelo', 'Fajozes', 'Ferreiró', 'Fornelo', 'Gião', 'Guilhabreu', 'Junqueira', 'Labruge', 'Macieira da Maia', 'Malta', 'Mindelo', 'Modivas', 'Mosteiró', 'Outeiro Maior', 'Parada', 'Retorta', 'Rio Mau', 'Tougues', 'Touguinha', 'Touguinhó', 'Vairão', 'Vila Chã', 'Vila do Conde', 'Vilar', 'Vilar de Pinheiro'],
        'Concelho de Vila Nova de Gaia': ['Arcozelo', 'Avintes', 'Canelas', 'Canidelo', 'Crestuma', 'Grijó', 'Gulpilhares', 'Lever', 'Madalena', 'Mafamude (Vila Nova de Gaia)', 'Olival', 'Oliveira do Douro', 'Pedroso', 'Perosinho', 'Sandim', 'São Félix da Marinha', 'São Pedro da Afurada (Vila Nova de Gaia)', 'Seixezelo', 'Sermonde', 'Serzedo', 'Valadares', 'Vila Nova de Gaia (Santa Marinha)', 'Vilar de Andorinho', 'Vilar do Paraíso'],
    },
    'Distrito de Santarém': {
        "Abrantes": ["Aldeia do Mato e Souto", "Alferrarede", "Bemposta", "Carvalhal", "Fontes", "Mação", "Mouriscas", "Pego", "Rio de Moinhos", "São Facundo e Vale das Mós", "São João", "São Miguel do Rio Torto e Rossio ao Sul do Tejo", "Tramagal"],
        "Alcanena": ["Alcanena e Vila Moreira", "Bugalhos", "Espinheiro", "Malhou, Louriceira e Espinheiro", "Minde", "Monsanto", "Moitas Venda", "Serra de Santo António"],
        "Almeirim": ["Almeirim", "Benfica do Ribatejo", "Fazendas de Almeirim", "Raposa"],
        "Alpiarça": ["Alpiarça"],
        "Benavente": ["Barrosa", "Benavente", "Vale da Pinta", "Samora Correia", "Santo Estêvão"],
        "Cartaxo": ["Cartaxo e Vale da Pinta", "Ereira e Lapa", "Pontével", "Valada", "Vila Chã de Ourique"],
        "Chamusca": ["Carregueira", "Chamusca e Pinheiro Grande", "Parreira e Chouto", "Ulme", "Vale de Cavalos"],
        "Constância": ["Constância", "Montalvo", "Santa Margarida da Coutada"],
        "Coruche": ["Branca", "Biscainho", "Couço", "Coruche, Fajarda e Erra", "Santana do Mato", "São José da Lamarosa"],
        "Entroncamento": ["Entroncamento", "São João Baptista", "Nossa Senhora de Fátima", "São João Baptista"],
        "Ferreira do Zêzere": ["Águas Belas", "Areias e Pias", "Beco", "Chãos", "Ferreira do Zêzere", "Igreja Nova do Sobral", "Nossa Senhora do Pranto"],
        "Golegã": ["Azinhaga", "Golegã", "Pombalinho"],
        "Mação": ["Aboboreira", "Amêndoa", "Cardigos", "Carvoeiro", "Envendos", "Mação, Penhascoso e Aboboreira", "Ortiga"],
        "Ourém": ["Alburitel", "Atouguia", "Caxarias", "Espite", "Fátima", "Freixianda, Ribeira do Fárrio e Formigais", "Gondemaria e Olival", "Matas e Cercal", "Nossa Senhora da Piedade", "Nossa Senhora das Misericórdias", "Seiça", "Urqueira"],
        "Rio Maior": ["Alcobertas", "Arrouquelas", "Asseiceira", "Azambujeira e Malaqueijo", "Fráguas", "Marmeleira e Assentiz", "Outeiro da Cortiçada e Arruda dos Pisões", "Rio Maior", "São João da Ribeira e Ribeira de São João", "São Sebastião"],
        "Salvaterra de Magos": ["Glória do Ribatejo e Granho", "Marinhais", "Muge", "Salvaterra de Magos e Foros de Salvaterra"],
        "Santarém": ["Abitureiras", "Achete, Azoia de Baixo e Póvoa de Santarém", "Alcanhões", "Almoster", "Amiais de Baixo", "Arneiro das Milhariças", "Azoia de Cima e Tremês", "Casével e Vaqueiros", "Moçarria", "Pernes", "Pombalinho", "Romeira e Várzea", "Santarém", "São Vicente do Paul e Vale de Figueira", "Vale de Santarém", "Várzea"],
        "Sardoal": ["Alcaravela", "Santiago de Montalegre", "Sardoal", "Valhascos"],
        "Tomar": ["Além da Ribeira e Pedreira", "Asseiceira", "Carregueiros", "Casais e Alviobeira", "Madalena e Beselga", "Olalhas", "Paialvo", "Sabacheira", "São João Baptista e Santa Maria dos Olivais", "São Pedro de Tomar", "Serra e Junceira"],
        "Torres Novas": ["Assentiz", "Brogueira, Parceiros de Igreja e Alcorochel", "Chancelaria", "Meia Via", "Olaia e Paço", "Pedrógão", "Riachos", "Torres Novas (São Pedro), Lapas e Ribeira Branca", "Zibreira"],
        "Vila Nova da Barquinha": ["Atalaia", "Praia do Ribatejo", "Tancos", "Vila Nova da Barquinha", "Moita do Norte"],
        "Alcanede": ["Alcanede", "Aldeia da Ribeira", "Arneiro das Milhariças", "Azoia de Cima", "Azoia de Baixo", "Amiais de Baixo", "Valverde"]
    },
    'Distrito de Setúbal': {
        'Concelho de Alcácer do Sal': ['Comporta', 'Santa Maria do Castelo (Alcácer do Sal)', 'Santa Susana', 'Santiago (Alcácer do Sal)', 'São Martinho', 'Torrão'],
        'Concelho de Alcochete': ['Alcochete', 'Samouco', 'São Francisco'],
        'Concelho de Almada': ['Almada', 'Cacilhas', 'Caparica', 'Charneca da Caparica', 'Costa de Caparica', 'Cova da Piedade', 'Feijó', 'Laranjeiro', 'Pragal', 'Sobreda', 'Trafaria'],
        'Concelho do Barreiro': ['Alto do Seixalinho (Barreiro)', 'Barreiro (Barreiro', 'Coina', 'Lavradio', 'Palhais', 'Santo André', 'Santo António da Charneca', 'Verderena (Barreiro)'],
        'Concelho do concelho de Grândola': ['Azinheira dos Barros', 'São Mamede do Sádão', 'Carvalhal', 'Grândola', 'Melides', 'Santa Margarida da Serra'],
        'Concelho da Moita': ['Alhos Vedros', 'Baixa da Banheira', 'Gaio-Rosário', 'Moita', 'Sarilhos Pequenos', 'Vale da Amoreira'],
        'Concelho do Montijo': ['Afonsoeiro (Montijo)', 'Alto Estanqueiro - Jardia', 'Atalaia', 'Canha', 'Montijo', 'Pegões', 'Santo Isidro de Pegões', 'Sarilhos Grandes'],
        'Concelho de Palmela': ['Marateca', 'Palmela', 'Pinhal Novo', 'Poceirão', 'Quinta do Anjo'],
        'Concelho de Santiago do Cacém': ['Abela', 'Alvalade', 'Cercal do Alentejo', 'Ermidas-Sado', 'Santa Cruz', 'Santiago do Cacém', 'Santo André', 'São Bartolomeu da Serra', 'São Domingos', 'São Francisco da Serra', 'Vale de Água'],
        'Concelho do Seixal': ['Aldeia de Paio Pires', 'Amora', 'Arrentela (Seixal)', 'Corroios', 'Fernão Ferro', 'Seixal'],
        'Concelho de Sesimbra': ['Castelo', 'Quinta do Conde', 'Santiago'],
        'Concelho de Setúbal': ['Gâmbia - Pontes - Alto da Guerra', 'Nossa Senhora da Anunciada (Setúbal)', 'Sado', 'Santa Maria da Graça (Setúbal)', 'São Julião', 'São Lourenço', 'São Sebastião', 'São Simão'],
        'Concelho de Sines': ['Sines', 'Porto Côvo'],
    },
    'Distrito de Viana do Castelo': {
        'Concelho de Arcos de Valdevez': ['Aboim das Choças', 'Aguiã', 'Aldora', 'Ázere', 'Cabana Maior', 'Cabreiro', 'Carralcova', 'Cendufe', 'Couto', 'Eiras', 'Ermelo', 'Extremo', 'Gavieira', 'Giela', 'Gondoriz', 'Grade', 'Guilhadeses', 'Loureda', 'Madalena de Jolda', 'Mei', 'Miranda', 'Monte Redondo', 'Oliveira', 'Paçô', 'Padroso', 'Parada', 'Portela', 'Prozelo', 'Rio Cabrão', 'Rio de Moinhos', 'Rio Frio', 'Sá', 'Sabadim', 'Salvador', 'Salvador de Padreiro', 'Santa Cristina de Padreiro', 'Santa Maria de Távora', 'Santar', 'São Cosme e São Damião', 'São Jorge', 'São Paio', 'São Paio de Jolda', 'São Vicente de Távora', 'Senharei', 'Sistelo', 'Soajo', 'Souto', 'Tabaçô', 'Vale', 'Vila Fonche', 'Vilela'],
        'Concelho de Caminha': ['Âncora', 'Arga de Baixo', 'Arga de Cima', 'Arga de São João', 'Argela', 'Azevedo', 'Caminha', 'Cristelo', 'Dem', 'Gondar', 'Lanhelas', 'Moledo', 'Orbacém', 'Riba de Âncora', 'Seixas', 'Venade', 'Vila Praia de Âncora', 'Vilar de Mouros', 'Vilarelho(Caminha)', 'Vile'],
        'Concelho de Melgaço': ['Alvaredo', 'Castro Laboreiro', 'Chaviães', 'Cousso', 'Cristoval', 'Cubalhão', 'Fiães', 'Gave', 'Lamas de Mouro', 'Paços', 'Paderne', 'Parada do Monte', 'Penso', 'Prado', 'Remoães', 'Roussas', 'São Paio', 'Vila (Melgaço)'],
        'Concelho de Monção': ['Abedim', 'Anhões', 'Badim', 'Barbeita', 'Barroças e Taias', 'Bela', 'Cambeses', 'Ceivães', 'Cortes', 'Lapela', 'Lara', 'Longos Vales', 'Lordelo', 'Luzio', 'Mazedo', 'Merufe', 'Messegães', 'Monção', 'Moreira', 'Parada', 'Pias', 'Pinheiros', 'Podame', 'Portela', 'Riba de Mouro', 'Sá', 'Sago', 'Segude', 'Tangil', 'Troporiz', 'Troviscoso', 'Trute', 'Valadares'],
        'Concelho de Paredes de Coura': ['Agualonga', 'Bico', 'Castanheira', 'Cossourado', 'Coura', 'Cristelo', 'Cunha', 'Ferreira', 'Formariz', 'Infesta', 'Insalde', 'Linhares', 'Mozelos', 'Padornelo', 'Parada', 'Paredes de Coura', 'Porreiras', 'Resende', 'Romarigães', 'Rubiães', 'Vascões'],
        'Concelho de Ponte da Barca': ['Azias', 'Boivães', 'Bravães', 'Britelo', 'Crasto', 'Cuide de Vila Verde', 'Entre Ambos-os-Rios', 'Ermida', 'Germil', 'Grovelas', 'Lavradas', 'Lindoso', 'Nogueira', 'Oleiros', 'Paço Vedro de Magalhães', 'Ponte da Barca', 'Ruivos', 'Salvador de Touvedo', 'Sampriz', 'Santiago de Vila Chã', 'São João Baptista de Vila Chã', 'São Lourenço de Touvedo', 'São Pedro de Vade', 'São Tomé de Vade', 'Vila Nova da Muía'],
        'Concelho de Ponte de Lima': ['Anais', 'Arca', 'Arcos', 'Arcozelo', 'Ardegão', 'Bárrio', 'Beiral do Lima', 'Bertiandos', 'Boalhosa', 'Brandara', 'Cabaços', 'Cabração', 'Calheiros', 'Calvelo', 'Cepões', 'Correlhã', 'Estorãos', 'Facha', 'Feitosa', 'Fojo Lobal', 'Fontão', 'Fornelos', 'Freixo', 'Friastelas', 'Gaifar', 'Gandra', 'Gemieira', 'Gondufe', 'Labruja', 'Labrujó', 'Mato', 'Moreira do Lima', 'Navió', 'Poiares', 'Ponte de Lima', 'Queijada', 'Refóios do Lima', 'Rendufe', 'Ribeira', 'Sá', 'Sandiães', 'Santa Comba', 'Santa Cruz do Lima', 'Santa Maria de Rebordões', 'Seara', 'Serdedelo', 'Souto de Rebordões', 'Vilar das Almas', 'Vilar do Monte', 'Vitorino das Donas', 'Vitorino dos Piães'],
        'Concelho de Valença': ['Arão', 'Boivão', 'Cerdal', 'Cristelo Covo', 'Fontoura', 'Friestas', 'Gandra', 'Ganfei', 'Gondomil', 'Sanfins', 'São Julião', 'São Pedro da Torre', 'Silva', 'Taião', 'Valença', 'Verdoejo'],
        'Concelho de Viana do Castelo': ['Afife', 'Alvarães', 'Amonde', 'Anha', 'Areosa (Viana do Castelo)', 'Barroselas', 'Cardielos', 'Carreço', 'Carvoeiro', 'Castelo do Neiva', 'Chafé', 'Darque (Viana do Castelo)', 'Deão', 'Deocriste', 'Freixieiro de Soutelo', 'Lanheses', 'Mazarefes', 'Meadela (Viana do Castelo)', 'Meixedo', 'Monserrate (Viana do Castelo)', 'Montaria', 'Moreira de Geraz do Lima', 'Mujães', 'Neiva', 'Nogueira', 'Outeiro', 'Perre', 'Portela Susã', 'Santa Marta de Portuzelo', 'Santa Leocádia de Geraz do Lima', 'Santa Maria de Geraz do Lima', 'Santa Maria Maior (Viana do Castelo)', 'Serreleis', 'Subportela', 'Torre', 'Vila de Punhe', 'Vila Franca', 'Vila Fria', 'Vila Mou', 'Vilar de Murteda'],
        'Concelho de Vila Nova de Cerveira': ['Campos', 'Candemil', 'Cornes', 'Covas', 'Gondar', 'Gondarém', 'Loivo', 'Lovelhe', 'Mentrestido', 'Nogueira', 'Reboreda', 'Sapardos', 'Sopo', 'Vila Meã', 'Vila Nova de Cerveira'],
    },
    'Distrito de Vila Real': {
        'Concelho de Alijó': ['Alijó', 'Amieiro', 'Carlão', 'Casal de Loivos', 'Castedo', 'Cotas', 'Favaios', 'Pegarinhos', 'Pinhão', 'Pópulo', 'Ribalonga', 'São Mamede de Ribatua', 'Sanfins do Douro', 'Santa Eugénia', 'Vale de Mendiz', 'Vila Chã', 'Vila Verde', 'Vilar de Maçada', 'Vilarinho de Cotas'],
        'Concelho de Boticas': ['Alturas do Barroso', 'Ardãos', 'Beça', 'Bobadela', 'Boticas', 'Cerdedo', 'Codessoso', 'Covas do Barroso', 'Curros', 'Dornelas', 'Fiães do Tâmega', 'Granja', 'Pinho', 'São Salvador de Viveiro', 'Sapiãos', 'Vilas'],
        'Concelho de Chaves': ['Águas Frias', 'Anelhe', 'Arcossó', 'Bobadela', 'Bustelo', 'Calvão', 'Cela', 'Cimo de Vila da Castanheira', 'Curalha', 'Eiras', 'Ervededo', 'Faiões', 'Lama de Arcos', 'Loivos', 'Madalena (Chaves)', 'Mairos', 'Moreiras', 'Nogueira da Montanha', 'Oucidres', 'Oura', 'Outeiro Seco', 'Paradela', 'Póvoa de Agrações', 'Redondelo', 'Roriz', 'Samaiões', 'Sanfins', 'Sanjurge', 'Santa Cruz - Trindade', 'Santa Leocádia', 'Santa Maria Maior', 'Santo António de Monforte', 'Santo Estêvão', 'São Julião de Montenegro', 'São Pedro de Agostém', 'São Vicente', 'Seara Velha', 'Selhariz', 'Soutelinho da Raia', 'Soutelo', 'Travancas', 'Tronco', 'Vale de Anta', 'Vidago', 'Vila Verde da Raia', 'Vilar de Nantes', 'Vilarelho da Raia', 'Vilarinho das Paranheiras', 'Vilas Boas', 'Vilela do Tâmega', 'Vilela Seca'],
        'Concelho de Mesão Frio': ['Barqueiros', 'Cidadelhe', 'Oliveira', 'São Nicolau (Mesão Frio)', 'Santa Cristina (Mesão Frio)', 'Vila Jusã (Mesão Frio)', 'Vila Marim'],
        'Concelho de Mondim de Basto': ['Atei', 'Bilhó', 'Campanhó', 'Ermelo', 'Mondim de Basto', 'Paradança', 'Pardelhas', 'Vilar de Ferreiros'],
        'Concelho de Montalegre': ['Cabril', 'Cambeses do Rio', 'Cervos', 'Chã', 'Contim', 'Covelães', 'Covelo do Gerês', 'Donões', 'Ferral', 'Fervidelas', 'Fiães do Rio', 'Gralhas', 'Meixedo', 'Meixide', 'Montalegre', 'Morgade', 'Mourilhe', 'Negrões', 'Outeiro', 'Padornelos', 'Padroso', 'Paradela', 'Pitões das Júnias', 'Pondras', 'Reigoso', 'Salto', 'Santo André', 'Sarraquinhos', 'Sezelhe', 'Solveira', 'Tourém', 'Venda Nova', 'Viade de Baixo', 'Vila da Ponte', 'Vilar de Perdizes'],
        'Concelho de Murça': ['Candedo', 'Carva', 'Fiolhoso', 'Jou', 'Murça', 'Noura', 'Palheiros', 'Valongo de Milhais', 'Candedo'],
        'Concelho do Peso da Régua': ['Canelas', 'Covelinhas', 'Fontelas', 'Galafura', 'Godim (Peso da Régua)', 'Loureiro', 'Moura Morta', 'Peso da Régua', 'Poiares', 'Sedielos', 'Vilarinho dos Freires', 'Vinhós'],
        'Concelho de Ribeira de Pena': ['Alvadia', 'Canedo', 'Cerva', 'Limões', 'Salvador', 'Santa Marinha', 'Santo Aleixo de Além-Tâmega'],
        'Concelho de Sabrosa': ['Celeirós', 'Covas do Douro', 'Gouvães do Douro', 'Gouvinhas', 'Parada de Pinhão', 'Paradela de Guiães', 'Paços', 'Provesende', 'Sabrosa', 'São Cristóvão do Douro', 'São Lourenço de Ribapinhão', 'São Martinho de Antas', 'Souto Maior', 'Torre do Pinhão', 'Vilarinho de São Romão'],
        'Concelho de Santa Marta de Penaguião': ['Alvações do Corgo', 'Cumieira', 'Fontes', 'Fornelos', 'Louredo', 'Medrões', 'Sanhoane', 'São João Baptista de Lobrigos', 'São Miguel de Lobrigos (Santa Marta de Penaguião)', 'Sever'],
        'Concelho de Valpaços': ['Água Revés e Crasto', 'Algeriz', 'Alvarelhos', 'Barreiros', 'Bouçoães', 'Canaveses', 'Carrazedo de Montenegro', 'Curros', 'Ervões', 'Fiães', 'Fornos do Pinhal', 'Friões', 'Lebução', 'Nozelos', 'Padrela e Tazem', 'Possacos', 'Rio Torto', 'Sanfins', 'Santa Maria de Emeres', 'Santa Valha', 'Santiago da Ribeira de Alhariz', 'São João da Corveira', 'São Pedro de Veiga de Lila', 'Serapicos', 'Sonim', 'Tinhela', 'Vales', 'Valpaços', 'Vassal', 'Veiga de Lila', 'Vilarandelo'],
        'Concelho de Vila Pouca de Aguiar': ['Afonsim', 'Alfarela de Jales', 'Bornes de Aguiar', 'Bragado', 'Capeludos', 'Gouvães da Serra', 'Lixa do Alvão', 'Parada de Monteiros', 'Pensalvos', 'Sabroso de Aguiar', 'Santa Marta da Montanha', 'Soutelo de Aguiar', 'Telões', 'Tresminas', 'Valoura', 'Vila Pouca de Aguiar', 'Vreia de Bornes', 'Vreia de Jales'],
        'Concelho de Vila Real': ['Abaças', 'Adoufe', 'Andrães', 'Arroios', 'Borbela', 'Campeã', 'Constantim', 'Ermida', 'Folhadela', 'Guiães', 'Justes', 'Lamares', 'Lamas de Olo', 'Lordelo', 'Mateus', 'Mondrões', 'Mouçós', 'Nogueira', 'Nossa Senhora da Conceição (Vila Real)', 'Parada de Cunhos', 'Pena', 'Quintã', 'São Dinis (Vila Real)', 'São Pedro (Vila Real)', 'São Tomé do Castelo', 'Torgueda', 'Vale de Nogueiras', 'Vila Cova', 'Vila Marim', 'Vilarinho de Samardã'],
    },
    'Distrito de Viseu': {
        'Concelho de Armamar': ['Aldeias', 'Aricera', 'Armamar', 'Cimbres', 'Coura', 'Folgosa', 'Fontelo', 'Goujoim', 'Queimada', 'Queimadela', 'Santa Cruz', 'Santiago', 'Santo Adrião', 'São Cosmado', 'São Martinho das Chãs', 'São Romão', 'Tões', 'Vacalar', 'Vila Seca'],
        'Concelho de Carregal do Sal': ['Beijós', 'Cabanas de Viriato', 'Currelos (Carregal do Sal)', 'Oliveira do Conde (Carregal do Sal)', 'Papízios', 'Parada', 'Sobral'],
        'Concelho de Castro Daire': ['Almofala', 'Alva', 'Cabril', 'Castro Daire', 'Cujó', 'Ermida', 'Ester', 'Gafanhão', 'Gosende', 'Mamouros', 'Mezio', 'Mões', 'Moledo', 'Monteiras', 'Moura Morta', 'Parada de Ester', 'Pepim', 'Picão', 'Pinheiro', 'Reriz', 'Ribolhos', 'São Joaninho'],
        'Concelho de Cinfães': ['Alhões', 'Bustelo', 'Cinfães', 'Espadanedo', 'Ferreiros de Tendais', 'Fornelos', 'Gralheira', 'Moimenta', 'Nespereira', 'Oliveira do Douro', 'Ramires', 'Santiago de Piães', 'São Cristóvão de Nogueira', 'Souselo', 'Tarouquela', 'Tendais', 'Travanca'],
        'Concelho de Lamego': ['Almacave (Lamego)', 'Avões', 'Bigorne', 'Britiande', 'Cambres', 'Cepões', 'Ferreirim', 'Ferreiros de Avões', 'Figueira', 'Lalim', 'Lazarim', 'Magueija', 'Meijinhos', 'Melcões', 'Parada do Bispo', 'Penajóia', 'Penude', 'Pretarouca', 'Samodães', 'Sande', 'Sé (Lamego)', 'Valdigem', 'Várzea de Abrunhais', 'Vila Nova de Souto d\'El-Rei'],
        'Concelho de Mangualde': ['Abrunhosa-a-Velha', 'Alcafache', 'Chãs de Tavares', 'Cunha Alta', 'Cunha Baixa', 'Espinho', 'Fornos de Maceira Dão', 'Freixiosa', 'Lobelhe do Mato', 'Mangualde', 'Mesquitela', 'Moimenta de Maceira Dão', 'Póvoa de Cervães', 'Quintela de Azurara', 'Santiago de Cassurrães', 'São João da Fresta', 'Travanca de Tavares', 'Várzea de Tavares'],
        'Concelho de Moimenta da Beira': ['Aldeia de Nacomba', 'Alvite', 'Arcozelos', 'Ariz', 'Baldos', 'Cabaços', 'Caria', 'Castelo', 'Leomil', 'Moimenta da Beira', 'Nagosa', 'Paradinha', 'Passô', 'Pêra Velha', 'Peva', 'Rua', 'Sarzedo', 'Segões', 'Sever', 'Vilar'],
        'Concelho de Mortágua': ['Almaça', 'Cercosa', 'Cortegaça', 'Espinho', 'Marmeleira', 'Mortágua', 'Pala', 'Sobral', 'Trezói', 'Vale de Remígio'],
        'Concelho de Nelas': ['Aguieira', 'Canas de Senhorim', 'Carvalhal Redondo', 'Lapa do Lobo', 'Moreira', 'Nelas', 'Santar', 'Senhorim', 'Vilar Seco'],
        'Concelho de Oliveira de Frades': ['Arca', 'Arcozelo das Maias', 'Destriz', 'Oliveira de Frades', 'Pinheiro', 'Reigoso', 'Ribeiradio', 'São João da Serra', 'São Vicente de Lafões', 'Sejães', 'Souto de Lafões', 'Varzielas'],
        'Concelho de Penalva do Castelo': ['Antas', 'Castelo de Penalva', 'Esmolfe', 'Germil', 'Ínsua', 'Lusinde', 'Mareco', 'Matela', 'Pindo', 'Real', 'Sezures', 'Trancozelos', 'Vila Cova do Covelo'],
        'Concelho de Penedono': ['Antas', 'Beselga', 'Castainço', 'Granja', 'Ourozinho', 'Penedono', 'Penela da Beira', 'Póvoa de Penela', 'Souto'],
        'Concelho de Resende': ['Anreade', 'Barrô', 'Cárquere', 'Feirão', 'Felgueiras', 'Freigil', 'Miomães', 'Ovadas', 'Panchorra', 'Paus', 'Resende', 'São Cipriano', 'São João de Fontoura', 'São Martinho de Mouros', 'São Romão de Aregos'],
        'Concelho de Santa Comba Dão': ['Couto do Mosteiro', 'Nagozela', 'Ovoa', 'Pinheiro de Ázere', 'Santa Comba Dão', 'São Joaninho', 'São João de Areias', 'Treixedo', 'Vimieiro'],
        'Concelho de São João da Pesqueira': ['Castanheiro do Sul', 'Ervedosa do Douro', 'Espinhosa', 'Nagozelo do Douro', 'Paredes da Beira', 'Pereiros', 'Riodades', 'São João da Pesqueira', 'Soutelo do Douro', 'Trevões', 'Vale de Figueira', 'Valongo dos Azeites', 'Várzea de Trevões', 'Vilarouco', 'Vidigal'],
        'Concelho de São Pedro do Sul': ['Baiões', 'Bordonhos', 'Candal', 'Carvalhais', 'Covas do Rio', 'Figueiredo de Alva', 'Manhouce', 'Pindelo dos Milagres', 'Pinho', 'Santa Cruz da Trapa', 'São Cristóvão de Lafões', 'São Félix', 'São Martinho das Moitas', 'São Pedro do Sul', 'Serrazes', 'Sul', 'Valadares', 'Várzea', 'Vila Maior'],
        'Concelho de Sátão': ['Águas Boas', 'Avelal', 'Decermilo', 'Ferreira de Aves', 'Forles', 'Mioma', 'Rio de Moinhos', 'Romãs', 'São Miguel de Vila Boa', 'Sátão', 'Silvã de Cima', 'Vila Longa'],
        'Concelho de Sernancelhe': ['Arnas', 'Carregal', 'Chosendo', 'Cunha', 'Escurquela', 'Faia', 'Ferreirim', 'Fonte Arcada', 'Freixinho', 'Granjal', 'Lamosa', 'Macieira', 'Penso', 'Quintela', 'Sarzeda', 'Sernancelhe', 'Vila da Ponte'],
        'Concelho de Tabuaço': ['Adorigo', 'Arcos', 'Barcos', 'Chavães', 'Desejosa', 'Granja do Tedo', 'Granjinha', 'Longa', 'Paradela', 'Pereiro', 'Pinheiros', 'Santa Leocádia', 'Sendim', 'Tabuaço', 'Távora', 'Vale de Figueira', 'Valença do Douro'],
        'Concelho de Tarouca': ['Dálvares', 'Gouviães', 'Granja Nova', 'Mondim da Beira', 'Salzedas', 'São João de Tarouca', 'Tarouca', 'Ucanha', 'Várzea da Serra', 'Vila Chã da Beira'],
        'Concelho de Tondela': ['Barreiro de Besteiros', 'Campo de Besteiros', 'Canas de Santa Maria', 'Caparrosa', 'Castelões', 'Dardavaz', 'Ferreirós do Dão', 'Guardão', 'Lajeosa do Dão', 'Lobão da Beira', 'Molelos', 'Mosteirinho', 'Mosteiro de Fráguas', 'Mouraz', 'Nandufe', 'Parada de Gonta', 'Sabugosa', 'Santiago de Besteiros', 'São João do Monte', 'São Miguel do Outeiro', 'Silvares', 'Tonda', 'Tondela', 'Tourigo', 'Vila Nova da Rainha', 'Vilar de Besteiros'],
        'Concelho de Vila Nova de Paiva': ['Alhais', 'Fráguas', 'Pendilhe', 'Queiriga', 'Touro', 'Vila Cova à Coelheira', 'Vila Nova de Paiva'],
        'Concelho de Viseu': ['Abraveses', 'Barreiros', 'Boa Aldeia', 'Bodiosa', 'Calde', 'Campo', 'Cavernães', 'Cepões', 'Coração de Jesus (Viseu)', 'Cota', 'Couto de Baixo', 'Couto de Cima', 'Fail', 'Farminhão', 'Fragosela', 'Lordosa', 'Mundão', 'Orgens', 'Povolide', 'Ranhados', 'Repeses', 'Ribafeita', 'Rio de Loba', 'Santa Maria de Viseu (Viseu)', 'Santos Evos', 'São Cipriano', 'São João de Lourosa', 'São José (Viseu)', 'São Pedro de France', 'São Salvador', 'Silgueiros', 'Torredeita', 'Vil de Souto', 'Vila Chã de Sá'],
        'Concelho de Vouzela': ['Alcofra', 'Cambra', 'Campia', 'Carvalhal de Vermilhas', 'Fataunços', 'Figueiredo das Donas', 'Fornelo do Monte', 'Paços de Vilharigues', 'Queirã', 'São Miguel do Mato', 'Ventosa', 'Vouzela'],
    },
    'Região Autónoma dos Açores': {
        "Corvo": ["Corvo"],
        "Faial": ["Angústias", "Capelo", "Castelo Branco", "Cedros", "Conceição", "Feteira", "Flamengos", "Pedro Miguel", "Praia do Almoxarife", "Praia do Norte", "Ribeirinha", "Salão"],
        "Flores": ["Caveira", "Cedros", "Fajã Grande", "Fajãzinha", "Lajedo", "Lajes das Flores", "Lomba", "Mosteiro", "Ponta Delgada", "Santa Cruz das Flores"],
        "Graciosa": ["Algodão", "Cercal", "Covilhã", "Guadalupe", "Luz", "Praia", "Santa Cruz da Graciosa", "São Mateus"],
        "Pico": ["Bandeiras", "Candelária", "Criação Velha", "Lajes do Pico", "Madalena", "Piedade", "Prainha", "Ribeiras", "Santa Luzia", "Santo Amaro", "São Caetano", "São João", "São Mateus", "São Roque do Pico"],
        "Santa Maria": ["Almagreira", "Cedros", "Covilhão", "Lajeosa do Douro", "Lajeosa do Sul", "Lomba", "Mosteiro", "Santa Bárbara", "Santo Espírito", "São Pedro", "Vila do Porto"],
        "São Jorge": ["Calheta", "Norte Grande", "Norte Pequeno", "Ribeira Seca", "Rosais", "Santo Amaro", "Topo", "Urzelina", "Velas"],
        "São Miguel": ["Água de Pau", "Ajuda da Bretanha", "Arrifes", "Candelária", "Covoada", "Fenais da Ajuda", "Fenais da Luz", "Feteiras", "Furnas", "Ginetes", "Lagoa", "Lomba da Maia", "Lomba de São Pedro", "Maia", "Mosteiros", "Nordeste", "Pico da Pedra", "Ponta Delgada", "Ponta Garça", "Povoação", "Rabo de Peixe", "Ribeira Chã", "Ribeira das Tainhas", "Ribeira Grande", "Ribeira Seca", "São Brás", "São José", "São Miguel", "Vila Franca do Campo"],
        "Terceira": ["Agualva", "Altares", "Angra do Heroísmo", "Biscoitos", "Cabo da Praia", "Calheta", "Doze Ribeiras", "Feteira", "Fontinhas", "Lajes", "Porto Judeu", "Praia da Vitória", "Quatro Ribeiras", "Raminho", "Ribeirinha", "Santa Bárbara", "São Bartolomeu dos Regatos", "São Bento", "São Brás", "São Mateus da Calheta", "São Pedro", "Serreta", "Terra Chã", "Vila de São Sebastião"]
    },
    'Região Autónoma da Madeira': {
        "Calheta": ["Arco da Calheta", "Calheta", "Estreito da Calheta", "Jardim do Mar", "Paul do Mar", "Prazeres", "Fajã da Ovelha"],
        "Câmara de Lobos": ["Câmara de Lobos", "Curral das Freiras", "Estreito de Câmara de Lobos", "Jardim da Serra", "Quinta Grande"],
        "Funchal": ["Imaculado Coração de Maria", "Monte", "São Gonçalo", "São Martinho", "São Pedro", "São Roque", "Sé", "Santa Luzia", "Santo António", "Santa Maria Maior"],
        "Machico": ["Água de Pena", "Caniçal", "Machico", "Porto da Cruz", "Santo António da Serra"],
        "Ponta do Sol": ["Canhas", "Madalena do Mar", "Ponta do Sol"],
        "Porto Moniz": ["Achadas da Cruz", "Porto Moniz", "Ribeira da Janela", "Seixal"],
        "Porto Santo": ["Porto Santo"],
        "Ribeira Brava": ["Campanário", "Ribeira Brava", "Serra de Água", "Tabua"],
        "Santa Cruz": ["Camacha", "Caniço", "Gaula", "Santa Cruz", "Santo António da Serra"],
        "Santana": ["Arco de São Jorge", "Faial", "Ilha", "Santana", "São Jorge", "São Roque do Faial"],
        "São Vicente": ["Boaventura", "Ponta Delgada", "São Vicente"]
    }
}


wellcome = ('Em nome de toda a equipe do Nova Direita, é com grande prazer que confirmo a aceitação de sua filiação como membro activo de nosso Partido Político\n\n'
            'A sua decisão de se juntar a nós, é o testemunho do seu compromisso com os valores e objectivos que defendemos e implica a aceitação dos estatutos e declaração de princípios,\n'
            'aprovados no Congresso Fundador e que se encontram em anexo.\n'
            'Para começar a sua jornada connosco, gostaria de convidá-lo a efectuar o pagamento da sua quota anual de membro, no valor de 30€, para o IBAN do\n'
            'partido que se encontra em anexo. De seguida, envie o comprovativo para o email\n'
            'secretariageral@novadireita.pt, e a sua filiação torna-se efectiva a partir da data de pagamento da quota, conforme os estatutos do Partido.\n'
            'Se precisar de assistência durante o processo de pagamento ou tiver'
            'alguma dúvida sobre a sua filiação, não hesite em entrar em contacto connosco para o referido email.\n'
            'Estamos aqui para ajudar e garantir que sua experiência no ND seja positiva e gratificante.\n\n'
            'Agradeço de coração pelo seu compromisso com o Nova Direita e aguardo ansiosamente para juntos trabalharmos em prol de nossos ideais comuns.\n\n'
            'Cordialmente,\n\n'
            'Ossanda Liber\n'
            'Presidente da Comissão Política Nacional\n'
            'Nova Direita'
            '\n\n------------------------------------------------------------------------------------------------\n'
            'AVISO DE CONFIDENCIALIDADE\n'
            'Esta mensagem de correio electrónico e qualquer dos seus ficheiros anexos, caso existam, são confidenciais e destinados apenas á(s) pessoa(s) ou entidade(s) acima referida(s),\n'
            'podendo conter informação confidencial, privilegiada, a qual não deverá ser divulgada, copiada, gravada ou distribuída nos termos da lei vigente.\n'
            'Se não é o destinatário da mensagem, ou se ela lhe foi enviada por engano, agradecemos que não faça uso ou divulgação da mesma.\n'
            'A distribuição ou utilização da informação nela contida é VEDADA. Se recebeu esta mensagem por engano, por favor avise-nos de imediato,\n'
            'por correio electrónico, para o endereço acima e apague este e-mail do seu sistema. Obrigado.'
            '\n\n'
            'CONFIDENTIALITY NOTICE'
            '\n'
            'This e-mail transmission and eventual attached files are intended only for the use of the individual or entity named above and may contain information that is confidential,\n'
            'privileged and exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying,\n'
            'distribution or use of any of the information contained in this transmission is strictly VOIDED. If you have received this transmission in error,\n'
            'please notify us immediately by e-mail at the above address and delete this e-mail from your system. Thank you.')

update = ('Os seus dados foram atualizados no sistema da Nova Direita, bem como em todas as plataformas digitais.\n'
          'Para esclarecer mais a sua filiação, por favor contacte-nos através do email militantes@novadireita.pt,\n'
          'em observância com o normativo RGPD.\n'
          '\n\n------------------------------------------------------------------------------------------------\n'
          'AVISO DE CONFIDENCIALIDADE\n'
          'Esta mensagem de correio electrónico e qualquer dos seus ficheiros anexos, caso existam, são confidenciais e destinados apenas á(s) pessoa(s) ou entidade(s) acima referida(s),\n'
          'podendo conter informação confidencial, privilegiada, a qual não deverá ser divulgada, copiada, gravada ou distribuída nos termos da lei vigente.\n'
          'Se não é o destinatário da mensagem, ou se ela lhe foi enviada por engano, agradecemos que não faça uso ou divulgação da mesma.\n'
          'A distribuição ou utilização da informação nela contida é VEDADA. Se recebeu esta mensagem por engano, por favor avise-nos de imediato,\n'
          'por correio electrónico, para o endereço acima e apague este e-mail do seu sistema. Obrigado.'
          '\n\n'
          'CONFIDENTIALITY NOTICE'
          '\n'
          'This e-mail transmission and eventual attached files are intended only for the use of the individual or entity named above and may contain information that is confidential,\n'
          'privileged and exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying,\n'
          'distribution or use of any of the information contained in this transmission is strictly VOIDED. If you have received this transmission in error,\n'
          'please notify us immediately by e-mail at the above address and delete this e-mail from your system. Thank you.')

delete = ('Lamentamos a sua saída.\n'
          'Cabe-nos informar que o seu registo e dados pessoais foram definitivamente removidos da nossa base de dados central,\nem observância com o normativo RGPD.\n'
          'Caso tenha mais alguma dúvida ou questão a colocar, por favor não hesite em responder a este e-mail para militantes@novadireita.pt.\n'
          'Obrigado,\n'
          'Ossanda Liber\n'
          'Presidente da Comissão Política Nacional\n'
          'Nova Direita'
          '\n\n------------------------------------------------------------------------------------------------\n'
          'AVISO DE CONFIDENCIALIDADE\n'
          'Esta mensagem de correio electrónico e qualquer dos seus ficheiros anexos, caso existam, são confidenciais e destinados apenas á(s) pessoa(s) ou entidade(s) acima referida(s),\n'
          'podendo conter informação confidencial, privilegiada, a qual não deverá ser divulgada, copiada, gravada ou distribuída nos termos da lei vigente.\n'
          'Se não é o destinatário da mensagem, ou se ela lhe foi enviada por engano, agradecemos que não faça uso ou divulgação da mesma.\n'
          'A distribuição ou utilização da informação nela contida é VEDADA. Se recebeu esta mensagem por engano, por favor avise-nos de imediato,\n'
          'por correio electrónico, para o endereço acima e apague este e-mail do seu sistema. Obrigado.'
          '\n\n'
          'CONFIDENTIALITY NOTICE'
          '\n'
          'This e-mail transmission and eventual attached files are intended only for the use of the individual or entity named above and may contain information that is confidential,\n'
          'privileged and exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying,\n'
          'distribution or use of any of the information contained in this transmission is strictly VOIDED. If you have received this transmission in error,\n'
          'please notify us immediately by e-mail at the above address and delete this e-mail from your system. Thank you.'
          )


def email_body(name):
    body = {
        'welcome': f'Saudações, sr.(a)  {name},\n\n{wellcome}',
        'update': f'Saudações, sr.(a) {name},\n\n{update}',
        'delete': f'Saudações, sr.(a) {name},\n\n{delete}'
    }
    return body


text_rgpd = (
    'Responsável pelo tratamento: Partido Nova Direita, com sede na Av. António Serpa 32 8b, 1050-027 Lisboa, Portugal; tlf: 217 961 260; email: todosjuntos@novadireita.pt. \n\n'
    'Finalidade do tratamento: inscrição e gestão da condição de militante na ND, cujo fundamento de licitude é o artigo 9.º, n.º 2, alínea d), do Regulamento Geral sobre a Proteção de Dados.\n\n'
    'Podem os dados pessoais do militante ser objeto de processamento informático e de utilização no âmbito das atividades das estruturas internas e autónomas e diferentes candidaturas eleitorais'
    'internas de militantes recebidas, nos termos dos Estatutos e dos Regulamentos Eleitorais do Partido Nova Direita,'
    'com a garantia de não serem divulgados a outras entidades para outras atividades que não se enquadrem no âmbito das atividades do Partido.'
    'Caso se venha a equacionar a cedência de dados a terceiros para uma finalidade legítima, tal carecerá sempre da obtenção prévia do consentimento do militante.\n\n'
    'Prazo de conservação: os seus dados serão conservados enquanto perdurar a condição de militante e, caso se aplique alguma norma estatutária ou regulamentar que implique a conservação dos dados para lá desse momento,'
    'nomeadamente de ordem disciplinar, até ao final do prazo estatutariamente ou em regulamento previsto para a efetivação dessa norma.\n\n'
    'Direitos dos titulares: O titular dos dados pode exercer os seus direitos de acesso, retificação, oposição, eliminação ou limitação dos seus dados pessoais, nos termos do RGPD, devendo,'
    'para o efeito, remeter o seu pedido, por escrito, para militantes@novadireita.pt.\n\n'
    'Encarregado de Proteção de Dados: Em cumprimento do RGPD, o Encarregado da Proteção de Dados pode ser contactado através do endereço eletrónico militantes@novadireita.pt.\n\n'
    'Direito de queixa: caso assim o entenda, o titular dos dados tem o direito de apresentar queixa junto da autoridade de controlo nacional, a Comissão Nacional de Proteção de Dados. Declaro sob compromisso de honra\n\n'
    'que todos os dados indicados aqui correspondem à verdade e que não me encontro numa das situações previstas na Lei, nos Estatutos Nacionais do Partido e dos seus Regulamentos internos que impossibilitem a minha inscrição.'
)
