import tkinter as tk
import webbrowser

from tkinter.ttk import Label, Frame, Button
from .util.util_ventana import centrar_ventana
from .config.style import Style

from .modules.modelo.view import ModeloView
from .modules.filamento.view import FilamentoView
from .modules.impresion.view import ImpresionView


class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Impresiones')
        w, h = 1000, 650
        w_max, h_max = int(w*1.5), int(h*1.5)
        
        centrar_ventana(self, w, h)
        self.minsize(w, h)
        self.maxsize(w_max, h_max)
        
        self.paneles()
        self.controles_menu_lateral()

        Style(self)

    def paneles(self):

        # Crear paneles: barra superior, menú lateral y cuerpo principal
        self.barra_superior = Frame(self, style='menusuperior.TFrame', height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')      

        self.menu_lateral = Frame(self, style='menulateral.TFrame', width=150, padding=10)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False) 
        
        # self.cuerpo_principal = ModelView(self)
        # self.cuerpo_principal = FilamentoView(self)
        # self.cuerpo_principal = ImpresionView(self)
        self.cuerpo_principal = About(self)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    
    def controles_menu_lateral(self):
        ancho_menu = 20

        self.buttonModelo = Button(self.menu_lateral, text="Modelo", width=ancho_menu, command=self.abrir_modelo)
        self.buttonModelo.pack(side=tk.TOP, pady=6)

        self.buttonImpresion = Button(self.menu_lateral, text="Impresion", width=ancho_menu, command=self.abrir_impresion)
        self.buttonImpresion.pack(side=tk.TOP, pady=6)

        self.buttonFilamento = Button(self.menu_lateral, text="Filamento", width=ancho_menu, command=self.abrir_filamento)
        self.buttonFilamento.pack(side=tk.TOP, pady=6)

        self.buttonFilamento = Button(self.menu_lateral, text="Acerca de", width=ancho_menu, command=self.abrir_about)
        self.buttonFilamento.pack(side=tk.BOTTOM, pady=12)

    def abrir_modelo(self):
        self.cuerpo_principal.destroy()
        self.cuerpo_principal = ModeloView(self)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def abrir_impresion(self):
        self.cuerpo_principal.destroy()
        self.cuerpo_principal = ImpresionView(self)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def abrir_filamento(self):
        self.cuerpo_principal.destroy()
        self.cuerpo_principal = FilamentoView(self)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def abrir_about(self):
        self.cuerpo_principal.destroy()
        self.cuerpo_principal = About(self)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)


class About(Frame):
    def __init__(self, master):
        super().__init__(master)

        Label(self,text="Trabajo final para python intermedio", style="about.TLabel").pack(pady=10)
        Label(self,text="Sistema de control de impresiones 3D", style="about.TLabel").pack(pady=20)

        Label(self,text="Desarrollado por:", style="about.TLabel").pack()
        Label(self,text="Julian Torossian", style="about.TLabel").pack()
        l_mail = Label(self,text="julian.torossian@outlook.com", style="about.TLabel")
        l_mail.pack()
        l_mail.configure(cursor='hand2')
        # l_mail.bind("<Button-1>", lambda e: self.callback("https://mail.google.com/mail/u/0/?to=julian.torossian@outlook.com&tf=cm"))
        l_mail.bind("<Button-1>", lambda e: self.callback("mailto:julian.torossian@outlook.com"))

        Label(self,text="2024", style="about.TLabel").pack(side=tk.BOTTOM)



        
    def callback(self, url):
        webbrowser.open_new(url)

