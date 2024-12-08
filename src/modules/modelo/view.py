import tkinter as tk
from tkinter.ttk import Frame, Label, Button, Entry, Scrollbar, Treeview
from tkinter import messagebox

from .model import Modelo, ModeloModel

class ModeloView(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.modelo_id = None

        self.crearVentana()

    
    def crearVentana(self):
        self.title = Label(self, text="Modelo", style="title.TLabel")
        self.title.pack(pady=8)

        self.crud = Frame(self)
        self.crud.pack()
        
        self.tra = Frame(self)
        self.tra.pack(side=tk.BOTTOM, fill='both', expand=True)

        self.crear_crud()
        self.mostrar_tabla()
        self.disabled_crud()

# ------- CRUD -------

    def crear_crud(self):

        self.entry_crud = Frame(self.crud)
        self.entry_crud.pack()

        self.id = tk.IntVar()
        l_id = Label(self.entry_crud, text="Id:", style="entry.TLabel", width=5)
        l_id.pack(side="left", padx=5, pady=10)
        self.e_id = Entry(self.entry_crud, state="disabled", textvariable=self.id, width=5)
        self.e_id.pack(side="left", padx=5, pady=10)

        self.nombre = tk.StringVar()
        l_nombre = Label(self.entry_crud, text="Nombre:", style="entry.TLabel")
        l_nombre.pack(side="left", padx=5, pady=10)
        self.e_nombre = Entry(self.entry_crud, textvariable=self.nombre)
        self.e_nombre.pack(side="left", padx=5, pady=10)

        # TODO soporte para archivos

        # l_stl = tk.Label(self, text="Id:", font=FONT_CRUD, fg="#666a88", bg=COLOR_FONDO, width=5)
        # l_stl.pack(side="left", padx=5, pady=10)
        # self.id = ttk.Entry(self, font=FONT_CRUD, state="readonly", width=5)
        # self.id.pack(side="left", padx=5, pady=10)

        # l_nombre = tk.Label(self, text="Nombre:", font=FONT_CRUD, fg="#666a88", bg=COLOR_FONDO)
        # l_nombre.pack(side="left", padx=5, pady=10)
        # self.nombre = ttk.Entry(self, font=FONT_CRUD)
        # self.nombre.pack(side="left", padx=5, pady=10)

        self.btn_crud = Frame(self.crud)
        self.btn_crud.pack(pady=6)

        self.btn_create = Button(self.btn_crud, text="Crear", style="success.TButton", command=self.enabled_crud)
        self.btn_create.pack(side=tk.LEFT, expand=False)

        self.btn_confirm = Button(self.btn_crud, text="Confirmar", style="warning.TButton", command=self.confirm)
        self.btn_confirm.pack(side=tk.LEFT, expand=False)

        self.btn_cancel = Button(self.btn_crud, text="Cancelar", style="danger.TButton", command=self.cancel)
        self.btn_cancel.pack(side=tk.LEFT, expand=False)

    def confirm(self):
        modelo = Modelo(
            self.id.get(),
            self.nombre.get()
        )

        if (modelo.is_valid()):
            if self.modelo_id == None:
                ModeloModel.insertModelo(modelo)
            else:
                ModeloModel.updateModelo(modelo)
        else:
            messagebox.showerror(message="Los datos ingresados no son validos.", title="Error")
        
        self.disabled_crud()
        self.clear_crud()
        self.act_tabla()

    def cancel(self):
        self.disabled_crud()
        self.clear_crud()


    def enabled_crud(self):
        self.e_id.config(state='readonly')
        self.e_nombre.config(state='normal')
        self.btn_confirm.config(state='normal')
        self.btn_cancel.config(state='normal')
        self.btn_create.config(state='disabled')

    def disabled_crud(self):
        self.e_id.config(state='disabled')
        self.e_nombre.config(state='disabled')
        self.btn_confirm.config(state='disabled')
        self.btn_cancel.config(state='disabled')
        self.btn_create.config(state='normal')

    def clear_crud(self):
        self.id.set(0)
        self.nombre.set('')
        self.modelo_id = None

# ------- TABLA -------

    def mostrar_tabla(self):

        self.tabla_tra = Frame(self.tra)
        self.tabla_tra.pack(expand=True, fill='both')

        tree_scroll =  Scrollbar(self.tabla_tra)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = Treeview(self.tabla_tra, columns=('ID', 'Nombre'), show='headings', yscrollcommand=tree_scroll.set)
        
        self.tree.column('#0', minwidth=0, width=0, stretch=False)
        self.tree.column('ID', minwidth=25, width=25, stretch=False)
        self.tree.column('Nombre')

        self.tree.heading('#0', text='')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Nombre', text='Nombre')

        self.tree.pack(expand=True, fill='both')
        
        self.tree.tag_configure('oddrow', background='#ffffe0')
        self.tree.tag_configure('evenrow', background='#eafbea')                        

        self.act_tabla()
        
        self.btn_tra = Frame(self.tra)
        self.btn_tra.pack(pady=6)

        btn_edit = Button(self.btn_tra, text="Editar", style="warning.TButton", command=self.edit)
        btn_edit.pack(side=tk.LEFT, expand=False)

        btn_delete = Button(self.btn_tra, text="Eliminar", style="danger.TButton", command=self.delete)
        btn_delete.pack(side=tk.LEFT, expand=False)

    def act_tabla(self):
        self.tree.delete(*self.tree.get_children())
        self.modelos = ModeloModel.getModelos()

        for m in self.modelos:
            self.tree.insert('','end',text=m[0], values= (m[0],m[1]) )
        

    def edit(self):
        try:
            self.modelo_id = self.tree.item(self.tree.selection())['text']
            modelo = ModeloModel.getModelo(self.modelo_id)
            
            self.id.set(int(modelo[0]))
            self.nombre.set(modelo[1])

            self.enabled_crud()
        except:
            pass
    
    def delete(self):
        try:
            if (messagebox.askyesno(message="¿Esta seguro que desea eliminar el registro?", title="Desea eliminar?")):
                self.modelo_id = self.tree.item(self.tree.selection())['text']
                ModeloModel.deleteModelo(self.modelo_id)
        except:
            pass
        finally:
            self.act_tabla()
            self.clear_crud()
