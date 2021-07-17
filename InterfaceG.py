#importações das bibliotecas
import  functions_DB 
import tkinter

class crud():
    def __init__(self, DB):
        self.janela = tkinter.Tk()
        self.janela.title("CRUD")
        self.janela.geometry("250x200")

        self.name = None
        self.email = None

        self.DB = DB
        self.labels_Init()
        self.janela.mainloop()

    def labels_Init(self):
        self.botaoC = tkinter.Button(text='Create', width= '15', height='2', command= self.create)
        self.botaoR = tkinter.Button(text='Read', width= '15', height='2', command= self.read)    
        self.botaoU = tkinter.Button(text='Update', width= '15', height='2', command= self.update)
        self.botaoD = tkinter.Button(text='Delete', width= '15', height='2', command= self.delete)
        self.pack_labels()
    
    def labels_user(self):
        self.l_Name  = tkinter.Label(self.janela, text='Name:')
        self.entry_Name = tkinter.Entry(self.janela)
        self.l_Email  = tkinter.Label(self.janela, text='Email:')
        self.entry_Email = tkinter.Entry(self.janela)
        self.botao_confirm = tkinter.Button(self.janela, text='Confirmar', command= self.add)

    def pack_labels_users(self):
        self.l_Name.pack()
        self.entry_Name.pack()  
        self.l_Email.pack()
        self.entry_Email.pack()  
        self.botao_confirm.pack()

    def unpack_labels_users(self):
        self.l_Name.pack_forget()
        self.entry_Name.pack_forget()  
        self.l_Email.pack_forget()
        self.entry_Email.pack_forget()  
        self.botao_confirm.pack_forget()

    def res(self):
        self.unpack_labels_users()
        self.resultado = tkinter.Label(self.janela, text=self.DB.Create(self.name, self.email))
        self.botao_ok = tkinter.Button(self.janela, text='Ok', command= self.unpack_res)
        self.pack_res()

    def pack_res(self):
        self.resultado.pack()
        self.botao_ok.pack()

    def unpack_res(self):
        self.resultado.pack_forget()
        self.botao_ok.pack_forget()
        self.pack_labels()

    def add(self):
        self.name = self.entry_Name.get().lower()
        self.email = self.entry_Email.get().lower()
        self.res()
        

    def create(self):
        self.unpack_labels()
        self.labels_user()
        self.pack_labels_users()
        
    def read(self):
        self.unpack_labels()
        
    def update(self):
        self.unpack_labels()
        
    def delete(self):
        self.unpack_labels()
        

    def pack_labels(self):
        self.botaoC.pack()
        self.botaoR.pack()
        self.botaoU.pack()
        self.botaoD.pack()

    def unpack_labels(self):
        self.botaoC.pack_forget()
        self.botaoR.pack_forget()
        self.botaoU.pack_forget()
        self.botaoD.pack_forget()


if __name__ == '__main__':
    functions_DB.init_DB()
    crud(functions_DB)