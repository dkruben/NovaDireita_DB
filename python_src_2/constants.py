# -*- coding: utf-8 -*-
db_name = 'militantes'

icon = '../src_files/logos/logo.ico'
pdf_image = '../src_files/logos/nova_direita.png'

councils_options = {
    'Distrito de Aveiro': ['Águeda', 'Albergaria-a-Velha', 'Anadia', 'Arouca', 'Aveiro', 'Castelo de Paiva',
                           'Espinho', 'Estarreja', 'Ílhavo', 'Mealhada', 'Murtosa', 'Oliveira de Azeméis',
                           'Oliveira do Bairro', 'Ovar', 'Santa Maria da Feira', 'São João da Madeira', 'Sever do Vouga',
                           'Vagos', 'Vale de Cambra'],

    'Distrito de Beja': ['Aljustrel', 'Almodôvar', 'Alvito', 'Barrancos', 'Beja', 'Castro Verde', 'Cuba',
                         'Ferreira do Alentejo', 'Mértola', 'Moura', 'Odemira', 'Ourique', 'Serpa', 'Vidigueira'],

    'Distrito de Braga': ['Amares', 'Barcelos', 'Braga', 'Cabeceiras de Basto', 'Celorico de Basto', 'Esposende', 'Fafe',
                          'Guimarães', 'Póvoa de Lanhoso', 'Terras de Bouro', 'Vieira do Minho', 'Vila Nova de Famalicão',
                          'Vila Verde', 'Vizela'],

    'Distrito de Bragança': ['Alfândega da Fé', 'Bragança', 'Carrazeda de Ansiães', 'Freixo de Espada à Cinta', 'Macedo de Cavaleiros',
                             'Miranda do Douro', 'Mirandela', 'Mogadouro', 'Torre de Moncorvo', 'Vila Flor', 'Vimioso', 'Vinhais'],

    'Distrito de Castelo Branco': ['Belmonte', 'Castelo Branco', 'Covilhã', 'Fundão', 'Idanha-a-Nova', 'Oleiros', 'Penamacor', 'Proença-a-Nova',
                                   'Sertã', 'Vila de Rei', 'Vila Velha de Ródão'],

    'Distrito de Coimbra': ['Arganil', 'Cantanhede', 'Coimbra', 'Condeixa-a-Nova', 'Figueira da Foz', 'Góis', 'Lousã', 'Mealhada',
                            'Mira', 'Miranda do Corvo', 'Montemor-o-Velho', 'Oliveira do Hospital', 'Pampilhosa da Serra', 'Penacova',
                            'Penela', 'Soure', 'Tábua', 'Vila Nova de Poiares'],

    'Distrito de Évora': ['Alandroal', 'Arraiolos', 'Borba', 'Estremoz', 'Évora', 'Montemor-o-Novo', 'Mourão', 'Portel',
                          'Redondo', 'Reguengos de Monsaraz', 'Vendas Novas', 'Viana do Alentejo', 'Vila Viçosa'],

    'Distrito de Faro': ['Albufeira', 'Alcoutim', 'Aljezur', 'Castro Marim', 'Faro', 'Lagoa', 'Lagos', 'Loulé', 'Monchique',
                         'Olhão', 'Portimão', 'São Brás de Alportel', 'Silves', 'Tavira', 'Vila do Bispo', 'Vila Real de Santo António'],

    'Distrito da Guarda': ['Aguiar da Beira', 'Almeida', 'Celorico da Beira', 'Figueira de Castelo Rodrigo', 'Fornos de Algodres',
                           'Gouveia', 'Guarda', 'Manteigas', 'Mêda', 'Pinhel', 'Sabugal', 'Seia', 'Trancoso', 'Vila Nova de Foz Côa'],

    'Distrito de Leiria': ['Alcobaça', 'Alvaiázere', 'Ansião', 'Batalha', 'Bombarral', 'Caldas da Rainha', 'Castanheira de Pera',
                           'Figueiró dos Vinhos', 'Leiria', 'Marinha Grande', 'Nazaré', 'Óbidos', 'Pedrógão Grande', 'Peniche',
                           'Pombal', 'Porto de Mós'],

    'Distrito de Lisboa': ['Alenquer', 'Amadora', 'Arruda dos Vinhos', 'Azambuja', 'Cadaval', 'Cascais', 'Lisboa', 'Loures',
                           'Lourinhã', 'Mafra', 'Odivelas', 'Oeiras', 'Sintra', 'Sobral de Monte Agraço', 'Torres Vedras',
                           'Vila Franca de Xira'],

    'Distrito de Portalegre': ['Alter do Chão', 'Arronches', 'Avis', 'Campo Maior', 'Castelo de Vide', 'Crato', 'Elvas',
                               'Fronteira', 'Gavião', 'Marvão', 'Monforte', 'Nisa', 'Ponte de Sor', 'Portalegre', 'Sousel'],

    'Distrito do Porto': ['Amarante', 'Baião', 'Felgueiras', 'Gondomar', 'Lousada', 'Maia', 'Marco de Canaveses', 'Matosinhos',
                          'Paços de Ferreira', 'Paredes', 'Penafiel', 'Porto', 'Póvoa de Varzim', 'Santo Tirso', 'Trofa',
                          'Valongo', 'Vila do Conde', 'Vila Nova de Gaia'],

    'Distrito de Santarém': ['Abrantes', 'Alcanena', 'Almeirim', 'Alpiarça', 'Benavente', 'Cartaxo', 'Chamusca', 'Constância',
                             'Coruche', 'Entroncamento', 'Ferreira do Zêzere', 'Golegã', 'Mação', 'Ourém', 'Rio Maior',
                             'Salvaterra de Magos', 'Santarém', 'Sardoal', 'Tomar', 'Torres Novas', 'Vila Nova da Barquinha'],

    'Distrito de Setúbal': ['Alcácer do Sal', 'Alcochete', 'Almada', 'Barreiro', 'Grândola', 'Moita', 'Montijo', 'Palmela',
                            'Santiago do Cacém', 'Seixal', 'Sesimbra', 'Setúbal', 'Sines'],

    'Distrito de Viana do Castelo': ['Arcos de Valdevez', 'Caminha', 'Melgaço', 'Monção', 'Paredes de Coura', 'Ponte da Barca',
                                     'Ponte de Lima', 'Valença', 'Viana do Castelo', 'Vila Nova de Cerveira'],

    'Distrito de Vila Real': ['Alijó', 'Boticas', 'Chaves', 'Mesão Frio', 'Mondim de Basto', 'Montalegre', 'Murça', 'Peso da Régua',
                              'Ribeira de Pena', 'Sabrosa', 'Santa Marta de Penaguião', 'Valpaços', 'Vila Pouca de Aguiar', 'Vila Real'],

    'Distrito de Viseu': ['Armamar', 'Carregal do Sal', 'Castro Daire', 'Cinfães', 'Lamego', 'Mangualde', 'Moimenta da Beira', 'Mortágua',
                          'Nelas', 'Oliveira de Frades', 'Penalva do Castelo', 'Penedono', 'Resende', 'Santa Comba Dão', 'São João da Pesqueira',
                          'São Pedro do Sul', 'Sátão', 'Sernancelhe', 'Tabuaço', 'Tarouca', 'Tondela', 'Vila Nova de Paiva', 'Viseu', 'Vouzela'],

    'Região Autónoma dos Açores': ['Angra do Heroísmo', 'Calheta (Açores)', 'Corvo', 'Horta', 'Lagoa (Açores)', 'Lajes das Flores', 'Lajes do Pico',
                                   'Madalena', 'Nordeste', 'Ponta Delgada', 'Povoação', 'Praia da Vitória', 'Ribeira Grande', 'Santa Cruz da Graciosa',
                                   'Santa Cruz das Flores', 'São Roque do Pico', 'Velas', 'Vila do Porto', 'Vila Franca do Campo'],

    'Região Autónoma da Madeira': ['Calheta (Madeira)', 'Câmara de Lobos', 'Funchal', 'Machico', 'Ponta do Sol', 'Porto Moniz', 'Porto Santo',
                                   'Ribeira Brava', 'Santa Cruz', 'Santana', 'São Vicente']
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
