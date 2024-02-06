from Funcoes import *
import customtkinter as ctk
import random
import os
from PIL import Image

### Janela para mostrar o Resultado do Sorteio -----------------------------------
class ToplevelWindowSortear(ctk.CTkToplevel):
    Qtd = 0
    jogo = 1
    def __init__(self,QtdNumeros, Tipo):
        self.Qtd = QtdNumeros
        self.jogo = Tipo
        super().__init__()
    # def __init__(self, QtdNumeros, *args, **kwargs):
    #     super().__init__(*args, **kwargs)


        self.title('Boa sorte !')
        # Calcula centro da Tela
        self.x = int((self.winfo_screenwidth() / 2) - (WIDTH / 2))
        self.y = int((self.winfo_screenheight() / 2) - (HEIGHT / 2))
        self.geometry(f"860x600+{self.x}+{self.y}")
        print ('Qtd Jogos = ', str(self.Qtd))
        print('Tipo = ', str(self.jogo))

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
        self.lista = self.gerasorteio(self.jogo, self.Qtd)
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
    def gerasorteio(self,jogo, Qtd):
        self.randomlist = []
        if jogo == 1:
            self.max_jogos = 25
        elif jogo == 2:
            self.max_jogos = 60
        else:
            self.max_jogos = 31

        self.total_jogos = int(Qtd)
        while len(self.randomlist) < self.total_jogos:
            n = random.randint(1, self.max_jogos)
            if n not in self.randomlist:
                self.randomlist.append(n)
        # print(randomlist)
        self.randomlist.sort(reverse=False)
        return self.randomlist.copy()

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

