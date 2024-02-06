# pip install customtkinter
# pip install packaging
# Documentação : https://customtkinter.tomschimansky.com/

# É possivel obter qualquer resultado de qualquer modalidade de loteria na forma de um JSON,
# acessando uma simples URL.
# Basta acessar diretamente as segintes URLs e será obtido o respectivo resultado do concurso mais recente:
#
# https://servicebus2.caixa.gov.br/portaldeloterias/api/quina
# https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena
# https://servicebus2.caixa.gov.br/portaldeloterias/api/duplasena
# https://servicebus2.caixa.gov.br/portaldeloterias/api/lotofacil
# https://servicebus2.caixa.gov.br/portaldeloterias/api/lotomania
# https://servicebus2.caixa.gov.br/portaldeloterias/api/diadesorte
# https://servicebus2.caixa.gov.br/portaldeloterias/api/timemania
# https://servicebus2.caixa.gov.br/portaldeloterias/api/federal
# https://servicebus2.caixa.gov.br/portaldeloterias/api/loteca
# https://servicebus2.caixa.gov.br/portaldeloterias/api/supersete
#
# Nesse esquema, o JSON do resultado de um determinado concurso poderá ser obtido adicionando-se o número do sorteio desejado ao final da respectiva URL.
#
# P.ex., para se obter o resultado do concurso 1234 da quina, basta um GET em
#
# https://servicebus2.caixa.gov.br/portaldeloterias/api/quina/1234

import customtkinter as ctk
from loteria_caixa import (MegaSena, LotoFacil, DiadeSorte)
from Funcoes import *
from ClasseToplevelSortear import *
from ClasseToplevelResultado import *


class Frame_Sortear(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.variable = ctk.StringVar()
        self.QtdNumeros = int(opcoes_LotoFacil[0])
        self.variable.set(opcoes_LotoFacil[0])
        self.Tipo= 1    # LotoFacil
        self.ListaResultado = []

        try:
            self.ResultLotoFacil = LotoFacil()
            self.ResultMegasena = MegaSena()
            self.ResultDiadeSorte = DiadeSorte()
            self.Atual = str(self.ResultLotoFacil.numero())
            self.NoConcurso = ctk.StringVar(value="2000")
            self.NoConcurso.set(self.Atual)
            self.label = ctk.CTkLabel(self,
                                      text="",
                                      fg_color="transparent",
                                      font=('Arial', 30),
                                      ).place(relx=0.23, rely=0.90)
        except:
            self.label = ctk.CTkLabel(self,
                                      text="  SEM ACESSO ! ",
                                      fg_color="orange",
                                      font=('Arial', 30),
                                      ).place(relx=0.23, rely=0.90)

        self.Valor = dic_dados["1_15"][0].ljust(20)
        self.Prob = dic_dados["1_15"][1].ljust(20)


        self.label = ctk.CTkLabel(self,
                     text="NÚMEROS DA SORTE",
                     fg_color="transparent",
                     font= ('Arial',30),
                     ).place(relx=0.23, rely=0.0)

        self.radio_var = ctk.IntVar(value=1)
        self.radiobutton_1 = ctk.CTkRadioButton(self,
                                                text="Loto Fácil",
                                                font=('Arial', 18),
                                                command=self.radiobutton_event,
                                                variable=self.radio_var, value=1
                                                ).place(relx=0.1, rely=0.2)
        self.radiobutton_2 = ctk.CTkRadioButton(self,
                                                text="Megasena",
                                                font=('Arial', 18),
                                                command=self.radiobutton_event,
                                                variable=self.radio_var, value=2
                                                ).place(relx=0.38, rely=0.2)
        self.radiobutton_3 = ctk.CTkRadioButton(self,
                                                text="Dia da sorte",
                                                font=('Arial', 18),
                                                command=self.radiobutton_event,
                                                variable=self.radio_var, value=3
                                                ).place(relx=0.65, rely=0.2)

        self.buttonSortear = ctk.CTkButton(self,
                                           text="Sortear",
                                           corner_radius=10,
                                           font=('Arial', 18),
                                           width=200,
                                           height=50,
                                           command=self.open_toplevelSortear
                                           ).place(relx=0.3, rely=0.5, anchor=ctk.CENTER)

        self.x_value = 0.55
        self.label1 = ctk.CTkLabel(self,
                                   text="Quantidade de jogos"
                                   ).place(relx=self.x_value, rely=0.4)

        self.combo = ctk.CTkComboBox(self,
                                     variable=self.variable,
                                     values= opcoes, # PegaNoJogos(self.Tipo),
                                     fg_color=cor,
                                     command=self.select_callback
                                     ).place(relx=self.x_value, rely=0.49)

        self.buttonResultado = ctk.CTkButton(self,
                                             text="Resultado",
                                             corner_radius=10,
                                             font=('Arial', 18),
                                             width=200,
                                             height=50,
                                             command=self.open_toplevelResultado
                                             ).place(relx=0.3, rely=0.80, anchor=ctk.CENTER)

        self.label2 = ctk.CTkLabel(self,
                                   text="Nº do Concurso"
                                   ).place(relx=self.x_value, rely=0.7)

        self.label3 = ctk.CTkLabel(self,
                                   text=self.Valor
                                   ).place(relx=self.x_value + 0.27, rely=0.44)
        self.label4 = ctk.CTkLabel(self,
                                   text=self.Prob
                                   ).place(relx=self.x_value + 0.27, rely=0.51)

        self.NoJogo = ctk.CTkEntry(self,
                                   fg_color=cor,
                                   textvariable=self.NoConcurso
                                   ).place(relx=self.x_value, rely=0.79)


    # ########## Combo Número Jogos selecionado
    def select_callback(self, choice):
        self.QtdNumeros = choice
        self.chave = str(self.Tipo) + '_' + str(self.QtdNumeros)

        self.Valor = dic_dados[self.chave][0].ljust(20)
        self.Prob = dic_dados[self.chave][1].ljust(20)
        self.label3 = ctk.CTkLabel(self,
                                   text=self.Valor
                                   ).place(relx=self.x_value + 0.27, rely=0.44)
        self.label4 = ctk.CTkLabel(self,
                                   text=self.Prob
                                   ).place(relx=self.x_value + 0.27, rely=0.51)


    def radiobutton_event(self):
        # print("radiobutton toggled, current value:", self.radio_var.get() )
        jogo = self.radio_var.get()
        opcoes = PegaNoJogos(jogo)  # Busca o quantidade de numeros a jogar para o tipo de jogo escolhido
        self.variable.set(opcoes[0])
        self.QtdNumeros = int(opcoes[0])
        self.Tipo = jogo
        if self.Tipo == 1:
            self.Atual = str(self.ResultLotoFacil.numero())
        elif self.Tipo == 2:
            self.Atual = str(self.ResultMegasena.numero())
        else:
            self.Atual = str(self.ResultDiadeSorte.numero())

        self.NoConcurso.set(self.Atual)
        self.chave = str(self.Tipo) + '_' + str(self.QtdNumeros)  # Valor da Aposta
        self.Valor = dic_dados[self.chave][0].ljust(20)
        self.Prob = dic_dados[self.chave][1].ljust(20)
        #print('Chave = ',self.chave,'  Valor = ', self.Valor )

        self.combo = ctk.CTkComboBox(self,
                                     #variable=self.variable,
                                     values=opcoes,
                                     fg_color=cor,
                                     command=self.select_callback
                                     ).place(relx=self.x_value, rely=0.49)
        self.label3 = ctk.CTkLabel(self,
                                   text=self.Valor
                                   ).place(relx=self.x_value + 0.27, rely=0.44)
        self.label4 = ctk.CTkLabel(self,
                                   text=self.Prob
                                   ).place(relx=self.x_value + 0.27, rely=0.51)

    def BuscaResultado(self):
        #self.Resultado = {}
        if self.Tipo == 1:
            self.concurso = LotoFacil(self.NoConcurso.get())
        elif self.Tipo == 2:
            self.concurso = MegaSena(self.NoConcurso.get())
        else:
            self.concurso = DiadeSorte(self.NoConcurso.get())

        #print(f'Resultado: {self.Resultado["listaDezenas"]}  Tipo = {self.Tipo}')
        return self.concurso.todosDados()

    ### Cria tela para mostrar os números sorteados
    def open_toplevelSortear(self):
        jogo = self.radio_var.get()
        # print('Numero jogos = '+ QtdJogos)
        self.toplevel_window = None
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindowSortear(self.QtdNumeros, self.Tipo)  # create window if its None or destroyed
            self.toplevel_window.focus()  # if window exists focus it
        else:
            self.toplevel_window.focus()  # if window exists focus it

    ### Cria tela para mostrar os números sorteados
    def open_toplevelResultado(self):
        try:
            self.ResultadoTotal = self.BuscaResultado()

            self.toplevel_window2 = None
            if self.toplevel_window2 is None or not self.toplevel_window2.winfo_exists():
                self.toplevel_window2 = ToplevelWindowResultado(self.ResultadoTotal)  # create window if its None or destroyed
                self.toplevel_window2.focus()  # if window exists focus it
            else:
                self.toplevel_window.focus()  # if window exists focus it

            self.label = ctk.CTkLabel(self,
                                      text="",
                                      fg_color="transparent",
                                      font=('Arial', 30),
                                      ).place(relx=0.23, rely=0.90)
        except:
            self.label = ctk.CTkLabel(self,
                                      text="  ACESSO INVÁLIDO ! ",
                                      fg_color="orange",
                                      font=('Arial', 30),
                                      ).place(relx=0.23, rely=0.90)


### Tela de Apresentação
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Calcula centro da Tela
        self.x = int((self.winfo_screenwidth() / 2) - (WIDTH / 2))
        self.y = int((self.winfo_screenheight() / 2) - (HEIGHT / 2))
        self.geometry(f"{WIDTH}x{HEIGHT}+{self.x}+{self.y}")

        ctk.set_appearance_mode('dark')
        self.title('Sorteio da sorte')

        self.Frame = Frame_Sortear(master=self,
                                   width=550,
                                   height=310,
                                   fg_color=None
                                   ).pack(padx=10, pady=40)


app = App()
app.mainloop()


