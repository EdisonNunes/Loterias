from Funcoes import *
import customtkinter as ctk
#import locale
import os
from PIL import Image
######### Retorno da API -----------------------------------------------------------
# {'acumulado': True,
#  'dataApuracao': '03/02/2024',
#  'dataProximoConcurso': '06/02/2024',
#  'dezenasSorteadasOrdemSorteio': ['07', '11', '04', '25', '02', '29', '03'],
#  'exibirDetalhamentoPorCidade': True,
#  'id': None,
#  'indicadorConcursoEspecial': 1,
#  'listaDezenas': ['02', '03', '04', '07', '11', '25', '29'],
#  'listaDezenasSegundoSorteio': None,
#  'listaMunicipioUFGanhadores': [],
#  'listaRateioPremio': [
#      {'descricaoFaixa': '7 acertos', 'faixa': 1, 'numeroDeGanhadores': 0, 'valorPremio': 0.0},
#      {'descricaoFaixa': '6 acertos', 'faixa': 2, 'numeroDeGanhadores': 33, 'valorPremio': 2581.02},
#      {'descricaoFaixa': '5 acertos', 'faixa': 3, 'numeroDeGanhadores': 1357, 'valorPremio': 25.0},
#      {'descricaoFaixa': '4 acertos', 'faixa': 4, 'numeroDeGanhadores': 17988, 'valorPremio': 5.0},
#      {'descricaoFaixa': 'Mês da Sorte', 'faixa': 5, 'numeroDeGanhadores': 44807, 'valorPremio': 2.5}],
#  'listaResultadoEquipeEsportiva': None,
#  'localSorteio': 'ESPAÇO DA SORTE',
#  'nomeMunicipioUFSorteio': 'SÃO PAULO, SP',
#  'nomeTimeCoracao:'',
#  'MesSorte': 'Janeiro',
#  'numero': 871,
#  'numeroConcursoAnterior': 870,
#  'numeroConcursoFinal_0_5': 0,
#  'numeroConcursoProximo': 872,
#  'numeroJogo': 11,
#  'observacao': '',
#  'premiacaoContingencia': None,
#  'tipoJogo': 'DIA_DE_SORTE',
#  'tipoPublicacao': 3,
#  'ultimoConcurso': True,
#  'valorArrecadado': 1479750.0,
#  'valorAcumuladoConcurso_0_5': 0.0,
#  'valorAcumuladoConcursoEspecial': 0.0,
#  'valorAcumuladoProximoConcurso': 363118.4,
#  'valorEstimadoProximoConcurso': 600000.0,
#  'valorSaldoReservaGarantidora': 0.0,
#  'valorTotalPremioFaixaUm': 0.0}


#locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

### Janela para mostrar o Resultado do Sorteio -----------------------------------
class ToplevelWindowResultado(ctk.CTkToplevel):
    concurso = None
    def __init__(self,ResultadoTotal):
        self.concurso = ResultadoTotal
        super().__init__()

        self.title('Resultados !')
        # Calcula centro da Tela
        self.x = int((self.winfo_screenwidth() / 2) - (WIDTH / 2))
        self.y = int((self.winfo_screenheight() / 2) - (HEIGHT / 2))
        self.geometry(f"860x600+{self.x}+{self.y}")


        texto = self.concurso['tipoJogo'] + \
                '     Concurso : '+ str(self.concurso['numero']) + \
                '     Data : ' + self.concurso['dataApuracao']
        texto = texto.replace('_',' ')

        self.label = ctk.CTkLabel(self,
                                  text= texto,
                                  fg_color="transparent",
                                  padx=0,
                                  pady=40,
                                  font=('Arial', 30),
                                  )
        self.label.pack(padx=20, pady=20)
        self.lista = list(self.concurso['listaDezenas'])
        self.DesenhaBola(self.lista)

        if self.concurso['tipoJogo'] == 'DIA_DE_SORTE':
            self.label = ctk.CTkLabel(self,
                                      text='MÊS SORTEADO :  ' + self.concurso['nomeTimeCoracaoMesSorte'],
                                      fg_color="transparent",
                                      padx=0,
                                      pady=50,
                                      font=('Arial', 30)
                                      ).place(x=250, y=300)

        self.MostraAcertadores()

    def FormataPremios(self,Resultado, i):
        fat = float(Resultado[i]["valorPremio"])
        fat = f'{fat:,.2f}'
        fat = fat.replace('.', '_').replace(',', '.').replace('_', ',')
        fat = 'R$ ' + fat
        Valor = f' Valor : {fat:<16}' # Alinhamento a esquerda

        gan = float(Resultado[i]["numeroDeGanhadores"])
        ganhadores = f'{gan:,.0f}'
        ganhadores = ganhadores.replace(',', '.')
        ganhadores = f'{ganhadores:>12}' # Alinhamento a direita
        desc = Resultado[i]['descricaoFaixa']
        desc = f'{desc:<12}' # Alinhamento a esquerda

        Texto = ganhadores + ' Ganhador(es) com ' + desc + Valor
        return Texto

    def MostraAcertadores(self):
        Premios =[]
        Texto = ctk.StringVar(value="")
        Premios = self.concurso['listaRateioPremio']
        last_Faixa = Premios[-1]['faixa']
        x_frame = 0.10
        y_frame = 0.77
        for i in range(last_Faixa):
            Texto = self.FormataPremios(Premios, i)
            #print(Texto)
            label = ctk.CTkLabel(self,
                                      text= Texto,
                                      #textvariable= Texto,
                                      fg_color="transparent",
                                      #padx=50,
                                      #pady=310,
                                      font=('Courier', 14)
                                      ).place(relx=x_frame, rely=y_frame)
            y_frame += 0.04



    # Desenha circunferências com o número sorteado no centro
    def DesenhaBola(self,lista):
        x = 80
        y = 120
        xmax = 6 * 120
        lista_sem_zero_esquerda = []
        for k in lista:
            while k[0] == '0':
                k = k[1]
            lista_sem_zero_esquerda.append(k)

        for idx, num in enumerate(lista):
            figura = fr"{caminho}/Fotos/{str(lista_sem_zero_esquerda[idx])}.png"
            self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), figura )
            self.image = ctk.CTkImage(light_image= Image.open(self.image_path), size=(100,100))
            self.image_label = ctk.CTkLabel(self, image = self.image, text= '')
            self.image_label.place(x= x, y= y)
            x += 120
            if x > xmax:
                x = 80
                y += 120

