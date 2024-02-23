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
import os
from PIL import Image
import random


WIDTH = 600
HEIGHT = 400
MES = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO',
       'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
caminho = os.getcwd()

### Janela para mostrar o Resultado do Sorteio
class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.jogo = app.radio_var.get()

        self.title('Boa sorte !')
        # Calcula centro da Tela
        self.x = int((self.winfo_screenwidth() / 2) - (WIDTH / 2))
        self.y = int((self.winfo_screenheight() / 2) - (HEIGHT / 2))
        self.geometry(f"860x600+{self.x}+{self.y}")

        if self.jogo == 1:
            texto = 'LOTO FÁCIL'
        if self.jogo == 2:
            texto = 'MEGA SENA'
        if self.jogo == 3:
            texto = 'DIA DE SORTE'
        self.label = ctk.CTkLabel(self,
                                  text= texto,
                                  fg_color="transparent",
                                  padx=0,
                                  pady=50,
                                  font=('Arial', 30),
                                  )
        self.label.pack(padx=20, pady=20)
        self.lista = self.gerasorteio(self.jogo)
        self.DesenhaBola(self.lista)

        if self.jogo == 3:
            n = random.randint(0, 11)
            self.label = ctk.CTkLabel(self,
                                      text='MÊS SORTEADO :  ' + MES[n],
                                      fg_color="transparent",
                                      padx=0,
                                      pady=50,
                                      font=('Arial', 30),
                                      ).place(x= 250, y= 500)
    # Gera numeros em função do tipo de jogo escolhido
    def gerasorteio(self,jogo):
        randomlist = []
        if jogo == 1:
            max_jogos = 25
            total_jogos = 15
        if jogo == 2:
            max_jogos = 60
            total_jogos = 6
        if jogo == 3:
            max_jogos = 31
            total_jogos = 7
        while len(randomlist) < total_jogos:
            n = random.randint(1, max_jogos)
            if n not in randomlist:
                randomlist.append(n)
        # print(randomlist)
        randomlist.sort(reverse=False)
        return randomlist.copy()

    # Desenha circunferências com o número sorteado no centro
    def DesenhaBola(self,lista):
        x = 80
        y = 120
        xmax = 6 * 120
        for idx, num in enumerate(lista):
            figura = fr"{caminho}/Fotos/{str(lista[idx])}.png"
            self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), figura )
            self.image = ctk.CTkImage(light_image= Image.open(self.image_path), size=(100,100))
            self.image_label = ctk.CTkLabel(self, image = self.image, text= '')
            self.image_label.place(x= x, y= y)
            x += 120
            if x > xmax:
                x = 80
                y += 120


### Tela de Apresentação
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Calcula centro da Tela
        self.x = int((self.winfo_screenwidth() / 2) - (WIDTH / 2))
        self.y = int((self.winfo_screenheight() / 2) - (HEIGHT / 2))
        self.geometry(f"{WIDTH}x{HEIGHT}+{self.x}+{self.y}")

        ctk.set_appearance_mode('dark')
        self.title('Sorteio da sorte.... ' + caminho)
        self.label = ctk.CTkLabel(self,
                     text="NÚMEROS DA SORTE",
                     fg_color="transparent",
                     padx= 0,
                     pady= 50,
                     font= ('Arial',30),
                     )
        self.label.pack()

        self.radio_var = ctk.IntVar(value=1)
        self.radiobutton_1 = ctk.CTkRadioButton(self,
                                                text="Loto Fácil",
                                                font=('Arial', 18),
                                                command=self.radiobutton_event,
                                                        variable= self.radio_var, value=1)
        self.radiobutton_2 = ctk.CTkRadioButton(self,
                                                text="Megasena",
                                                font=('Arial', 18),
                                                command=self.radiobutton_event,
                                                        variable= self.radio_var, value=2)
        self.radiobutton_3 = ctk.CTkRadioButton(self,
                                                text="Dia da sorte",
                                                font=('Arial', 18),
                                                command=self.radiobutton_event,
                                                variable=self.radio_var, value=3)
        x = 120
        self.radiobutton_1.place(x= x, y= 100)
        self.radiobutton_2.place(x= x + 120, y= 100)
        self.radiobutton_3.place(x= x + 240, y= 100)

        button = ctk.CTkButton(self,
                               text="Sortear",
                               corner_radius=10,
                               font=('Arial', 18),
                               width=200,
                               height=50,
                               command = self.open_toplevel).place(x=200, y=150)

        self.resizable(False,False)
        self.toplevel_window = None

    ### OnClick RadioButton
    def radiobutton_event(self):
        # print("radiobutton toggled, current value:", self.radio_var.get() )
        jogo = self.radio_var.get()
        # print('Jogo escolhido : ' + str(jogo))


    ### Cria tela para mostrar os números sorteados
    def open_toplevel(self):
        #jogo = self.radio_var.get()

        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed

            self.toplevel_window.focus()  # if window exists focus it
        else:
            self.toplevel_window.focus()  # if window exists focus it

app = App()
app.mainloop()


