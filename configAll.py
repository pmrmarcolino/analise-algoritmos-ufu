controle = [
    { 'diretorio': 'bolha',
      'linhas_de_interesse': [15],
      'rotulos': ['comparações'],
      'num_de_ensaios': 3,
      'complexidade': { 'pior':   'n^2',
                        'medio':  'n^2',
                        'melhor': 'n^2'
                      },
      'instancias': { 'pior':   ['Crescente'],
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
                      'melhor': ['Decrescente']
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
    },
    { 'diretorio': 'insertionsort',
      'linhas_de_interesse': [15],
      'rotulos': ['comparações'],
      'num_de_ensaios': 3,
      'complexidade': { 'pior':   'n^2',
                        'medio':  'n^2',
                        'melhor': 'n'
                      },
      'instancias': { 'pior':   ['Decrescente'],
                      'medio':  ['Aleatorio',
                                 'QuaseCresc10',
                                 'QuaseCresc20',
                                 'QuaseCresc30',
                                 'QuaseDecresc10',
                                 'QuaseDecresc20',
                                 'QuaseDecresc30',
                                 'QuaseDecresc40',
                                 'QuaseDecresc50'
                                ],
                      'melhor': ['Crescente',
                                 'QuaseCresc40',
                                 'QuaseCresc50']
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
    },
    { 'diretorio': 'selectionsort',
      'linhas_de_interesse': [15],
      'rotulos': ['comparações'],
      'num_de_ensaios': 3,
      'complexidade': { 'pior':   'n^2',
                        'medio':  'n^2',
                        'melhor': 'n^2'
                      },
      'instancias': { 'pior':   [],
                      'medio':  ['Crescente',
                                 'Aleatorio',
                                 'QuaseCresc10',
                                 'QuaseCresc20',
                                 'QuaseCresc30',
                                 'QuaseCresc40',
                                 'QuaseCresc50',
                                 'QuaseDecresc10',
                                 'QuaseDecresc20',
                                 'QuaseDecresc30',
                                 'QuaseDecresc40',
                                 'QuaseDecresc50',
                                 'Decrescente'
                                ],
                      'melhor': []
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
    },
    { 'diretorio': 'mergesort',
      'linhas_de_interesse': [16],
      'rotulos': ['comparações'],
      'num_de_ensaios': 3,
      'complexidade': { 'pior':   'nln(n)',
                        'medio':  'nln(n)',
                        'melhor': 'nln(n)'
                      },
      'instancias': { 'pior':   [],
                      'medio':  ['Crescente',
                                 'Aleatorio',
                                 'QuaseCresc10',
                                 'QuaseCresc20',
                                 'QuaseCresc30',
                                 'QuaseCresc40',
                                 'QuaseCresc50',
                                 'QuaseDecresc10',
                                 'QuaseDecresc20',
                                 'QuaseDecresc30',
                                 'QuaseDecresc40',
                                 'QuaseDecresc50',
                                 'Decrescente'
                                ],
                      'melhor': []
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
    },
    { 'diretorio': 'heapsort',
      'linhas_de_interesse': [16],
      'rotulos': ['comparações'],
      'num_de_ensaios': 3,
      'complexidade': { 'pior':   'nln(n)',
                        'medio':  'nln(n)',
                        'melhor': 'nln(n)'
                      },
      'instancias': { 'pior':   [],
                      'medio':  ['Crescente',
                                 'Aleatorio',
                                 'QuaseCresc10',
                                 'QuaseCresc20',
                                 'QuaseCresc30',
                                 'QuaseCresc40',
                                 'QuaseCresc50',
                                 'QuaseDecresc10',
                                 'QuaseDecresc20',
                                 'QuaseDecresc30',
                                 'QuaseDecresc40',
                                 'QuaseDecresc50',
                                 'Decrescente'
                                ],
                      'melhor': []
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
    },
    { 'diretorio': 'quicksort',
      'linhas_de_interesse': [12],
      'rotulos': ['comparações'],
      'num_de_ensaios': 3,
      'complexidade': { 'pior':   'n^2',
                        'medio':  'n^2',
                        'melhor': 'nln(n)'
                      },
      'instancias': { 'pior':   ['Decrescente'],
                      'medio':  ['Crescente',
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
                      'melhor': ['Aleatorio']
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
    },
    { 'diretorio': 'countingsort',
      'linhas_de_interesse': [13],
      'rotulos': ['comparações'],
      'num_de_ensaios': 3,
      'complexidade': { 'pior':   'n',
                        'medio':  'n',
                        'melhor': 'n'
                      },
      'instancias': { 'pior':   ['Crescente'],
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
                      'melhor': ['Decrescente']
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
    },
    { 'diretorio': 'radixsort',
      'linhas_de_interesse': [16],
      'rotulos': ['comparações'],
      'num_de_ensaios': 3,
      'complexidade': { 'pior':   'n',
                        'medio':  'n',
                        'melhor': 'n'
                      },
      'instancias': { 'pior':   ['Crescente'],
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
                      'melhor': ['Decrescente']
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
    },
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
