from loteria_caixa import (MegaSena, LotoFacil, Quina, LotoMania, TimeMania,
                      DuplaSena, Federal, Loteca, DiadeSorte, SuperSet)
# pip install loteria-caixa
# ######### https://pypi.org/project/loteria-caixa/ ##############
#concurso = LotoFacil(3012)
#resultado = concurso.todosDados()
#print(resultado['dataApuracao'])
#print(concurso.todosDados())
#print('Tipo Jogo :' + concurso.tipoJogo())
#print(concurso.numero())
#print(concurso.nomeMunicipioUFSorteio())
####print('dataApuracao :' +concurso.dataApuracao())
#print(concurso.valorArrecadado())
#print(concurso.valorEstimadoProximoConcurso())
#print(concurso.valorAcumuladoProximoConcurso())
#print(concurso.valorAcumuladoConcursoEspecial())
#print(concurso.valorAcumuladoConcurso_0_5())
#print(concurso.acumulado())
#print(concurso.indicadorConcursoEspecial())
#print(concurso.dezenasSorteadasOrdemSorteio())
#print(concurso.listaResultadoEquipeEsportiva())
#print(concurso.numeroJogo())
#print(concurso.nomeTimeCoracaoMesSorte())
#print(concurso.tipoPublicacao())
#print(concurso.observacao())
#print(concurso.localSorteio())
#print(concurso.dataProximoConcurso())
#print(concurso.numeroConcursoAnterior())
#print(concurso.numeroConcursoProximo())
#print(concurso.valorTotalPremioFaixaUm())
#print(concurso.numeroConcursoFinal_0_5())
#print(concurso.listaMunicipioUFGanhadores())
#print('Premio = ' + str(concurso.listaRateioPremio()))
#print('listaDezenas :' + str(concurso.listaDezenas()))
#print(concurso.listaDezenasSegundoSorteio())
#print(concurso.id())

# Premio = [{'descricaoFaixa': '15 acertos', 'faixa': 1, 'numeroDeGanhadores': 0, 'valorPremio': 0.0},
#           {'descricaoFaixa': '14 acertos', 'faixa': 2, 'numeroDeGanhadores': 243, 'valorPremio': 1520.99},
#           {'descricaoFaixa': '13 acertos', 'faixa': 3, 'numeroDeGanhadores': 7448, 'valorPremio': 30.0},
#           {'descricaoFaixa': '12 acertos', 'faixa': 4, 'numeroDeGanhadores': 92543, 'valorPremio': 12.0},
#           {'descricaoFaixa': '11 acertos', 'faixa': 5, 'numeroDeGanhadores': 527104, 'valorPremio': 6.0}
#           ]
# listaDezenas :['01', '02', '03', '05', '06', '07', '14', '15', '16', '17', '20', '21', '23', '24', '25']

#concurso = LotoFacil()
#concurso = MegaSena(2683)
concurso = DiadeSorte(871)
resultado = concurso.todosDados()
Premio = concurso.listaRateioPremio()
print('Concurso : '+ str(concurso.numero()) + '  Data Apuracao :' +concurso.dataApuracao())
print('Dezenas Sorteadas :' + str(concurso.listaDezenas()))
print(concurso.tipoJogo())
#print(resultado)

# print('Nº próximo sorteio : '+ str(concurso.numeroConcursoProximo()))
# print(resultado)



#'listaRateioPremio': [
#      {'descricaoFaixa': '7 acertos', 'faixa': 1, 'numeroDeGanhadores': 0, 'valorPremio': 0.0},
#      {'descricaoFaixa': '6 acertos', 'faixa': 2, 'numeroDeGanhadores': 33, 'valorPremio': 2581.02},
#      {'descricaoFaixa': '5 acertos', 'faixa': 3, 'numeroDeGanhadores': 1357, 'valorPremio': 25.0},
#      {'descricaoFaixa': '4 acertos', 'faixa': 4, 'numeroDeGanhadores': 17988, 'valorPremio': 5.0},
#      {'descricaoFaixa': 'Mês da Sorte', 'faixa': 5, 'numeroDeGanhadores': 44807, 'valorPremio': 2.5}],

last_Faixa = Premio[-1]['faixa']
print(last_Faixa)
print(Premio)
for i in range(last_Faixa):
    Valor = f'  Valor : R$ {Premio[i]["valorPremio"]:.2f}'
    print(Premio[i]['descricaoFaixa'] +
          '  Ganhadores : ' + str(Premio[i]['numeroDeGanhadores']) + Valor +
          '... Faixa ' + str(Premio[i]['faixa']))
          #' Valor : ' + str(Premio[i]['valorPremio']))
