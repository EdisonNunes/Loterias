import os
WIDTH = 600
HEIGHT = 400
MES = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO',
       'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
caminho = os.getcwd()

opcoes_LotoFacil  = ['15', '16', '17', '18', '19', '20']
opcoes_Megasena   = ['6',   '7',  '8',  '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
opcoes_DiaDeSorte = ['7',   '8',  '9', '10', '11', '12', '13', '14', '15']
opcoes = opcoes_LotoFacil.copy()
cor = '#1f6aa5'

dic_dados = {
       "1_15":["R$ 3,00       ","1 em 3.268.760 "],
       "1_16":["R$ 48,00      ","1 em 204.298   "],
       "1_17":["R$ 408,00     ","1 em 24.035    "],
       "1_18":["R$ 2.448,00   ","1 em 4.006     "],
       "1_19":["R$ 11.628,00  ","1 em 843       "],
       "1_20":["R$ 46.512,00  ","1 em 211       "],
        "2_6":["R$ 5,00       ","1 em 50.063.860"],
        "2_7":["R$ 35,00      ","1 em 7.151.980 "],
        "2_8":["R$ 140,00     ","1 em 1.797.995 "],
        "2_9":["R$ 420,00     ","1 em 595.998   "],
        "2_10":["R$ 1.050,00  ","1 em 238.399   "],
        "2_11":["R$ 2.310,00  ","1 em 108.363   "],
        "2_12":["R$ 4.620,00  ","1 em 54.182    "],
        "2_13":["R$ 8.580,00  ","1 em 29.175    "],
        "2_14":["R$ 15.105,00 ","1 em 16.671    "],
        "2_15":["R$ 25.025,00 ","1 em 10.003    "],
        "2_16":["R$ 40.040,00 ","1 em 6.252     "],
        "2_17":["R$ 61.880,00 ","1 em 4.045     "],
        "2_18":["R$ 92.820,00 ","1 em 2.697     "],
        "2_19":["R$ 135.660,00","1 em 1.845     "],
        "2_20":["R$ 193.800,00","1 em 1.292     "],
         "3_7":["R$ 2,50      ","1 em 2.629.575 "],
         "3_8":["R$ 20,00     ","1 em 328.696   "],
         "3_9":["R$ 90,00     ","1 em 73.043    "],
        "3_10":["R$ 300,00    ","1 em 21.913    "],
        "3_11":["R$ 825,00    ","1 em 7.968     "],
        "3_12":["R$ 1.980,00  ","1 em 3.320     "],
        "3_13":["R$ 4.290,00  ","1 em 1.532     "],
        "3_14":["R$ 8.580,00  ","1 em 766       "],
        "3_15":["R$ 16.087,50 ","1 em 408       "]
}


def PegaNoJogos(tipo):
       if tipo == 1:
              lista = opcoes_LotoFacil.copy()
       elif tipo == 2:
              lista = opcoes_Megasena
       else:
              lista = opcoes_DiaDeSorte

       # print(f'Qtd numeros a jogar: {lista[0]}  Tipo = {tipo}')
       return lista

# {"Chave":"1_15","Preço":"R$ 3,00","Probabilidade":"1 em 3.268.760"}
# {"Chave":"1_16","Preço":"R$ 48,00","Probabilidade":"1 em 204.298"}
# {"Chave":"1_17","Preço":"R$ 408,00","Probabilidade":"1 em 24.035"}
# {"Chave":"1_18","Preço":"R$ 2.448,00","Probabilidade":"1 em 4.006"}
# {"Chave":"1_19","Preço":"R$ 11.628,00","Probabilidade":"1 em 843"}
# {"Chave":"1_20","Preço":"R$ 46.512,00","Probabilidade":"1 em 211"}
# {"Chave":"2_6","Preço":"R$ 5,00","Probabilidade":"1 em 50.063.860"}
# {"Chave":"2_7","Preço":"R$ 35,00","Probabilidade":"1 em 7.151.980"}
# {"Chave":"2_8","Preço":"R$ 140,00","Probabilidade":"1 em 1.797.995"}
# {"Chave":"2_9","Preço":"R$ 420,00","Probabilidade":"1 em 595.998"}
# {"Chave":"2_10","Preço":"R$ 1.050,00","Probabilidade":"1 em 238.399"}
# {"Chave":"2_11","Preço":"R$ 2.310,00","Probabilidade":"1 em 108.363"}
# {"Chave":"2_12","Preço":"R$ 4.620,00","Probabilidade":"1 em 54.182"}
# {"Chave":"2_13","Preço":"R$ 8.580,00","Probabilidade":"1 em 29.175"}
# {"Chave":"2_14","Preço":"R$ 15.105,00","Probabilidade":"1 em 16.671"}
# {"Chave":"2_15","Preço":"R$ 25.025,00","Probabilidade":"1 em 10.003"}
# {"Chave":"2_16","Preço":"R$ 40.040,00","Probabilidade":"1 em 6.252"}
# {"Chave":"2_17","Preço":"R$ 61.880,00","Probabilidade":"1 em 4.045"}
# {"Chave":"2_18","Preço":"R$ 92.820,00","Probabilidade":"1 em 2.697"}
# {"Chave":"2_19","Preço":"R$ 135.660,00","Probabilidade":"1 em 1.845"}
# {"Chave":"2_20","Preço":"R$ 193.800,00","Probabilidade":"1 em 1.292"}
# {"Chave":"3_7","Preço":"R$ 2,50","Probabilidade":"1 em 2.629.575"}
# {"Chave":"3_8","Preço":"R$ 20,00","Probabilidade":"1 em 328.696"}
# {"Chave":"3_9","Preço":"R$ 90,00","Probabilidade":"1 em 73.043"}
# {"Chave":"3_10","Preço":"R$ 300,00","Probabilidade":"1 em 21.913"}
# {"Chave":"3_11","Preço":"R$ 825,00","Probabilidade":"1 em 7.968"}
# {"Chave":"3_12","Preço":"R$ 1.980,00","Probabilidade":"1 em 3.320"}
# {"Chave":"3_13","Preço":"R$ 4.290,00","Probabilidade":"1 em 1.532"}
# {"Chave":"3_14","Preço":"R$ 8.580,00","Probabilidade":"1 em 766"}
# {"Chave":"3_15","Preço":"R$ 16.087,50","Probabilidade":"1 em 408"}