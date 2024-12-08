import tkinter as tk
from tkinter.ttk import Style

COLOR_FONDO = "#fff"
COLOR_FONDO_BUSQUEDA = "#f7f8fa"
COLOR_CUERPO_PRINCIPAL = "#f1faff"
COLOR_TEXTO_ENTRY = "#666a88"

COLOR_BARRA_SUPERIOR = "#1f2329"
COLOR_MENU_LATERAL = "#2a3138"
COLOR_CUERPO_PRINCIPAL = "#f1faff"
COLOR_MENU_CURSOR_ENCIMA = "#2f88c5"

FONT_TITLE = ('Times', 16)
FONT_CRUD = ('Times', 10)
FONT_BTN = ('Times', 12)
FONT_ABOUT = ('Times', 14, 'bold')


class Style(Style):

    def __init__(self, master):
        super().__init__(master)

    
        # THEME

        self.theme_use("clam") # set theam to clam

        # PAGINA PRINCIPAL

        self.configure("menusuperior.TFrame", background=COLOR_BARRA_SUPERIOR)
        self.configure("menulateral.TFrame", background=COLOR_MENU_LATERAL)

        self.configure("about.TLabel", font=FONT_ABOUT)

        # LABELS

        self.configure("title.TLabel", font=FONT_TITLE, anchor="center")

        # ENTRYS

        self.configure("entry.TLabel",font=FONT_CRUD, fg=COLOR_TEXTO_ENTRY, bg=COLOR_FONDO)

        self.configure("TEntry", font=FONT_CRUD)

        # BUTTONS

        self.configure("TButton", padding=6, background="#ccc")
        
        self.map("danger.TButton",
                    foreground=[('pressed', '#FFFFFF'), ('active', '#FFFFFF')],
                    background=[('active', '#F44336'), ('disabled', '#F8BBD0'), ('!disabled', '#D32F2F'), ('hover', '!disabled', '#F8BBD0'), ('pressed', '#F44336')]
                )
        
        self.map("warning.TButton",
                    foreground=[('pressed', '#000000'), ('active', '#000000')],
                    background=[('active', '#FFEB3B'), ('disabled', '#FFF59D'), ('!disabled', '#F9A825'), ('hover', '!disabled', '#FFD54F'), ('pressed', '#FFEB3B')]
                )
        
        self.map("success.TButton",
                    foreground=[('pressed', '#FFFFFF'), ('active', '#FFFFFF')],
                    background=[('active', '#4CAF50'), ('disabled', '#81C784'), ('!disabled', '#2E7D32'), ('hover', '!disabled', '#66BB6A'), ('pressed', '#2E7D32')]
                )
        
        # Tipo de botón Fondo Activo	Fondo Inactivo	Fondo Hover	Fondo Click	Texto Activo/Click	Texto Inactivo/Hover
        # Éxito	        #4CAF50	        #2E7D32	        #66BB6A	    #4CAF50	    #FFFFFF	            #FFFFFF
        # Advertencia	#FFEB3B	        #F9A825	        #FFD54F	    #FFEB3B	    #000000	            #000000
        # Peligro	    #F44336	        #D32F2F	        #F8BBD0	    #F44336	    #FFFFFF	            #FFFFFF

        # TREEVIEW

        self.configure("Treeview", background="#eafbea", foreground="#000")
        self.configure('Treeview.Heading', background="#6f9a8d", foreground="#fff")