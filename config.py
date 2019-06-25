controle = [
    { 'diretorio': 'bucketsort',
      'linhas_de_interesse': [13],
      'rotulos': ['comparações'],
      'num_de_ensaios': 3,
      'complexidade': { 'pior':   'n^2',
                        'medio':  'n',
                        'melhor': 'n'
                      },
      'instancias': { 'pior':   ['Decrescente'],
                      'medio':  ['Aleatorio',
                                 'QuaseCresc10',
                                 'QuaseCresc20',
                                 'QuaseCresc30',
                                 'QuaseCresc40',
                                 'QuaseCresc50',
                                 'QuaseDecresc10',
                                 'QuaseDecresc20',
                                 'QuaseDecresc30',
                                 'QuaseDecresc40',
                                 'QuaseDecresc50'
                                ],
                      'melhor': ['Crescente']
                    },
      'graficos': { 'legenda_experimento': 'medições',
                    'eixos':  [{ 'abscissa': { 'col': 0,
                                               'rotulo': 'n (tamanho do vetor)'
                                             },
                                 'ordenada': { 'col': 2,
                                               'rotulo': 'tempo (s)'
                                             }
                               },
                               { 'abscissa': { 'col': 0,
                                               'rotulo': 'n (tamanho do vetor)'
                                             },
                                 'ordenada': { 'col': 1,
                                               'rotulo': 'número de comparações'
                                             }
                               },
                              ]
                     },
    }
]
