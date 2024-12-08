import tkinter as tk
from tkinter.ttk import Frame, Label, Button, Entry, Scrollbar, Treeview, Combobox
from tkinter import messagebox

from .model import Impresion, ImpresionModel
from ..modelo.model import ModeloModel
from ..filamento.model import FilamentoModel

class ImpresionView(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.impresion_id = None

        self.crearVentana()

    
    def crearVentana(self):
        self.title = Label(self, text="Impresion", style="title.TLabel")
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
        # l_id.pack(side="left", padx=5, pady=10)
        l_id.grid(row=1,column=1)
        self.e_id = Entry(self.entry_crud, state="disabled", textvariable=self.id, width=5)
        # self.e_id.pack(side="left", padx=5, pady=10)
        self.e_id.grid(row=1,column=2)

        self.modelos_aux = ModeloModel.getModelos()
        modelos_combo = []
        for m in self.modelos_aux:
            modelos_combo.append(m[1])

        self.modelos = ['Sel. Modelo'] + modelos_combo
        self.e_modelo = Combobox(self.entry_crud, state="readonly")
        self.e_modelo['values'] = self.modelos
        self.e_modelo.current(0)
        self.e_modelo.config(width=25)
        self.e_modelo.bind("<<ComboboxSelected>>")
        # self..pack(side="left", padx=5, pady=10)
        self.e_modelo.grid(row=1,column=3)

        self.t_impresion_est = tk.IntVar()
        l_t_impresion_est = Label(self.entry_crud, text="Tiempo estimado:", style="entry.TLabel")
        # l_t_impresion_est.pack(side="left", padx=5, pady=10)
        l_t_impresion_est.grid(row=1,column=4)
        self.e_t_impresion_est = Entry(self.entry_crud, textvariable=self.t_impresion_est)
        # self.e_t_impresion_est.pack(side="left", padx=5, pady=10)
        self.e_t_impresion_est.grid(row=1,column=5)

        self.t_impresion_fin = tk.IntVar()
        l_t_impresion_fin = Label(self.entry_crud, text="Tiempo final:", style="entry.TLabel")
        # l_t_impresion_fin.pack(side="left", padx=5, pady=10)
        l_t_impresion_fin.grid(row=2,column=4)
        self.e_t_impresion_fin = Entry(self.entry_crud, textvariable=self.t_impresion_fin)
        # self.e_t_impresion_fin.pack(side="left", padx=5, pady=10)
        self.e_t_impresion_fin.grid(row=2,column=5)

        self.filamentos_aux = FilamentoModel.getFilamentos()
        filamentos_combo = []
        for f in self.filamentos_aux:
            filamentos_combo.append(self.format_filamento(f))

        self.fialmentos = ['Sel. Filamento'] + filamentos_combo
        self.e_filamento = Combobox(self.entry_crud, state="readonly")
        self.e_filamento['values'] = self.fialmentos
        self.e_filamento.current(0)
        self.e_filamento.config(width=25)
        self.e_filamento.bind("<<ComboboxSelected>>")
        # self.e_filamento.pack(side="left", padx=5, pady=10)
        self.e_filamento.grid(row=2,column=3)

        self.gr_consumidos = tk.IntVar()
        l_gr_consumidos = Label(self.entry_crud, text="gr. consumidos:", style="entry.TLabel")
        # l_gr_consumidos.pack(side="left", padx=5, pady=10)
        l_gr_consumidos.grid(row=2,column=1)
        self.e_gr_consumidos = Entry(self.entry_crud, textvariable=self.gr_consumidos)
        # self.e_gr_consumidos.pack(side="left", padx=5, pady=10)
        self.e_gr_consumidos.grid(row=2,column=2)

        self.parametros = tk.StringVar()
        l_parametros = Label(self.entry_crud, text="Parametros:", style="entry.TLabel")
        # l_parametros.pack(side="left", padx=5, pady=10)
        l_parametros.grid(row=3, column=1)
        self.e_parametros = Entry(self.entry_crud, textvariable=self.parametros)
        self.e_parametros.grid(row=3, column=2)

        self.btn_crud = Frame(self.crud)
        self.btn_crud.pack(pady=6)

        self.btn_create = Button(self.btn_crud, text="Crear", style="success.TButton", command=self.enabled_crud)
        self.btn_create.pack(side=tk.LEFT, expand=False)

        self.btn_confirm = Button(self.btn_crud, text="Confirmar", style="warning.TButton", command=self.confirm)
        self.btn_confirm.pack(side=tk.LEFT, expand=False)

        self.btn_cancel = Button(self.btn_crud, text="Cancelar", style="danger.TButton", command=self.cancel)
        self.btn_cancel.pack(side=tk.LEFT, expand=False)

    def confirm(self):
        modelo_id = 0
        for m in self.modelos_aux:
            if (m[1]==self.e_modelo.get()):
                modelo_id = m[0]
                break
        filamento_id = 0
        for f in self.filamentos_aux:
            if (self.format_filamento(f)==self.e_filamento.get()):
                filamento_id = f[0]
                break

        impresion = Impresion(
            self.id.get(),
            modelo_id,
            self.t_impresion_est.get(),
            self.t_impresion_fin.get(),
            filamento_id,
            self.gr_consumidos.get(),
            self.parametros.get()
        )

        if (impresion.is_valid()):
            if self.impresion_id == None:
                ImpresionModel.insertImpresion(impresion)
            else:
                ImpresionModel.updateImpresion(impresion)
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
        self.e_modelo.config(state='normal')
        self.e_t_impresion_est.config(state='normal')
        self.e_t_impresion_fin.config(state='normal')
        self.e_filamento.config(state='normal')
        self.e_gr_consumidos.config(state='normal')
        self.e_parametros.config(state='normal')

        self.btn_confirm.config(state='normal')
        self.btn_cancel.config(state='normal')
        self.btn_create.config(state='disabled')

    def disabled_crud(self):
        self.e_id.config(state='disabled')
        self.e_modelo.config(state='disabled')
        self.e_t_impresion_est.config(state='disabled')
        self.e_t_impresion_fin.config(state='disabled')
        self.e_filamento.config(state='disabled')
        self.e_gr_consumidos.config(state='disabled')
        self.e_parametros.config(state='disabled')

        self.btn_confirm.config(state='disabled')
        self.btn_cancel.config(state='disabled')
        self.btn_create.config(state='normal')

    def clear_crud(self):
        self.id.set(0)
        self.e_modelo.current(0)
        self.t_impresion_est.set(0)
        self.t_impresion_fin.set(0)
        self.e_filamento.current(0)
        self.gr_consumidos.set(0)
        self.parametros.set('')
        self.impresion_id = None

# ------- TABLA -------

    def mostrar_tabla(self):

        self.tabla_tra = Frame(self.tra)
        self.tabla_tra.pack(expand=True, fill='both')

        self.tree = Treeview(self.tabla_tra,
                            columns=('ID', 'Modelo', 'Tiempo Est.', 'Tiempo Fin', 'Filamento', 'gr. Consu.', 'Parametros'),
                            show='headings')

        tree_scroll_y =  Scrollbar(self.tabla_tra, command=self.tree.yview)
        tree_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        tree_scroll_x =  Scrollbar(self.tabla_tra, orient=tk.HORIZONTAL, command=self.tree.xview)
        tree_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.tree.configure(yscrollcommand=tree_scroll_y.set,
                            xscrollcommand=tree_scroll_x.set)
        

        self.tree.column('#0', minwidth=0, width=0, stretch=False)
        self.tree.column('ID', minwidth=25, width=25, stretch=False)
        self.tree.column('Modelo', minwidth=210, width=210, stretch=False)
        self.tree.column('Tiempo Est.', minwidth=110, width=110, stretch=False)
        self.tree.column('Tiempo Fin', minwidth=110, width=110, stretch=False)
        self.tree.column('Filamento', minwidth=150, width=150, stretch=False)
        self.tree.column('gr. Consu.', minwidth=65, width=65, stretch=False)
        self.tree.column('Parametros')

        self.tree.heading('#0', text='')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Modelo', text='Modelo')
        self.tree.heading('Tiempo Est.', text='Tiempo Est. (min.)')
        self.tree.heading('Tiempo Fin', text='Tiempo Fin (min.)')
        self.tree.heading('Filamento', text='Filamento')
        self.tree.heading('gr. Consu.', text='gr. Consu.')
        self.tree.heading('Parametros', text='Parametros')

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
        self.impresiones = ImpresionModel.getImpresiones()

        for i in self.impresiones:
            modelo = ModeloModel.getModelo(i[1])
            filamento = FilamentoModel.getFilamento(i[4])

            self.tree.insert('','end',text=i[0], values= (i[0],modelo[1],f'{i[2]} min.',f'{i[3]} min.',self.format_filamento(filamento),f'{i[5]} gr.',i[6]) )
        

    def edit(self):
        try:
            if (self.impresion_id!=None):
                self.impresion_id = self.tree.item(self.tree.selection())['text']
                impresion = ImpresionModel.getImpresion(self.impresion_id)

                modelo = ModeloModel.getModelo(int(impresion[1]))
                filamento = FilamentoModel.getFilamento(int(impresion[4]))
                
                self.id.set(int(impresion[0]))
                self.e_modelo.current(self.modelos.index(modelo[1]))
                self.t_impresion_est.set(int(impresion[2]))
                self.t_impresion_fin.set(int(impresion[3]))
                self.e_filamento.current(self.fialmentos.index(self.format_filamento(filamento)))
                self.gr_consumidos.set(int(impresion[5]))
                self.parametros.set(impresion[6])

                self.enabled_crud()
        except Exception as e:
            print(e)
    
    def delete(self):
        try:
            if (self.impresion_id!=None):
                if (messagebox.askyesno(message="¿Esta seguro que desea eliminar el registro?", title="Desea eliminar?")):
                    self.impresion_id = self.tree.item(self.tree.selection())['text']
                    ImpresionModel.deleteImpresion(self.impresion_id)
        except:
            pass
        finally:
            self.act_tabla()
            self.clear_crud()

    def format_filamento(self, filamento):
        return f'{filamento[1]} - {filamento[2]}'
