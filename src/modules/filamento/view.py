import tkinter as tk
from tkinter.ttk import Frame, Label, Button, Entry, Scrollbar, Treeview
from tkinter import messagebox

from .model import Filamento, FilamentoModel

class FilamentoView(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.filamento_id = None

        self.crearVentana()

    
    def crearVentana(self):
        self.title = Label(self, text="Filamento", style="title.TLabel")
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

        self.tipo = tk.StringVar()
        l_tipo = Label(self.entry_crud, text="Tipo:", style="entry.TLabel")
        l_tipo.pack(side="left", padx=5, pady=10)
        self.e_tipo = Entry(self.entry_crud, textvariable=self.tipo)
        self.e_tipo.pack(side="left", padx=5, pady=10)

        self.color = tk.StringVar()
        l_color = Label(self.entry_crud, text="Color:", style="entry.TLabel")
        l_color.pack(side="left", padx=5, pady=10)
        self.e_color = Entry(self.entry_crud, textvariable=self.color)
        self.e_color.pack(side="left", padx=5, pady=10)

        self.detalle = tk.StringVar()
        l_detalle = Label(self.entry_crud, text="Detalle:", style="entry.TLabel")
        l_detalle.pack(side="left", padx=5, pady=10)
        self.e_detalle = Entry(self.entry_crud, textvariable=self.detalle)
        self.e_detalle.pack(side="left", padx=5, pady=10)

        self.btn_crud = Frame(self.crud)
        self.btn_crud.pack(pady=6)

        self.btn_create = Button(self.btn_crud, text="Crear", style="success.TButton", command=self.enabled_crud)
        self.btn_create.pack(side=tk.LEFT, expand=False)

        self.btn_confirm = Button(self.btn_crud, text="Confirmar", style="warning.TButton", command=self.confirm)
        self.btn_confirm.pack(side=tk.LEFT, expand=False)

        self.btn_cancel = Button(self.btn_crud, text="Cancelar", style="danger.TButton", command=self.cancel)
        self.btn_cancel.pack(side=tk.LEFT, expand=False)

    def confirm(self):
        filamento = Filamento(
            self.id.get(),
            self.tipo.get(),
            self.color.get(),
            self.detalle.get()
        )

        if (filamento.is_valid()):
            if self.filamento_id == None:
                FilamentoModel.insertFilamento(filamento)
            else:
                FilamentoModel.updateFilamento(filamento)
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
        self.e_tipo.config(state='normal')
        self.e_color.config(state='normal')
        self.e_detalle.config(state='normal')

        self.btn_confirm.config(state='normal')
        self.btn_cancel.config(state='normal')
        self.btn_create.config(state='disabled')

    def disabled_crud(self):
        self.e_id.config(state='disabled')
        self.e_tipo.config(state='disabled')
        self.e_color.config(state='disabled')
        self.e_detalle.config(state='disabled')

        self.btn_confirm.config(state='disabled')
        self.btn_cancel.config(state='disabled')
        self.btn_create.config(state='normal')

    def clear_crud(self):
        self.id.set(0)
        self.tipo.set('')
        self.color.set('')
        self.detalle.set('')
        self.filamento_id = None

# ------- TABLA -------

    def mostrar_tabla(self):

        self.tabla_tra = Frame(self.tra)
        self.tabla_tra.pack(expand=True, fill='both')

        tree_scroll =  Scrollbar(self.tabla_tra)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = Treeview(self.tabla_tra, columns=('ID', 'Tipo', 'Color', 'Detalle'), show='headings', yscrollcommand=tree_scroll.set)
        
        self.tree.column('#0', minwidth=0, width=0, stretch=False)
        self.tree.column('ID', minwidth=25, width=25, stretch=False)
        self.tree.column('Tipo', minwidth=150, width=150, stretch=False)
        self.tree.column('Color', minwidth=150, width=150, stretch=False)
        self.tree.column('Detalle')

        self.tree.heading('#0', text='')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Tipo', text='Tipo')
        self.tree.heading('Color', text='Color')
        self.tree.heading('Detalle', text='Detalle')

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
        self.filamentos = FilamentoModel.getFilamentos()

        for f in self.filamentos:
            self.tree.insert('','end',text=f[0], values= (f[0],f[1],f[2],f[3]) )
        

    def edit(self):
        try:
            self.filamento_id = self.tree.item(self.tree.selection())['text']
            filamento = FilamentoModel.getFilamento(self.filamento_id)
            
            self.id.set(int(filamento[0]))
            self.tipo.set(filamento[1])
            self.color.set(filamento[2])
            self.detalle.set(filamento[3])

            self.enabled_crud()
        except:
            pass
    
    def delete(self):
        try:
            if (messagebox.askyesno(message="¿Esta seguro que desea eliminar el registro?", title="Desea eliminar?")):
                self.filamento_id = self.tree.item(self.tree.selection())['text']
                FilamentoModel.deleteFilamento(self.filamento_id)
        except:
            pass
        finally:
            self.act_tabla()
            self.clear_crud()
