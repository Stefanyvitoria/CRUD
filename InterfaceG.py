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


    def labels_user(self, cmd):
        self.l_Name  = tkinter.Label(self.janela, text='Name:')
        self.entry_Name = tkinter.Entry(self.janela)
        self.l_Email  = tkinter.Label(self.janela, text='Email:')
        self.entry_Email = tkinter.Entry(self.janela)
        self.botao_confirm = tkinter.Button(self.janela, text='Confirmar', command= cmd)

    def pack_labels_users1(self):
        self.l_Name.pack()
        self.entry_Name.pack()  
        self.l_Email.pack()
        self.entry_Email.pack()  
        self.botao_confirm.pack()

    def pack_labels_users2(self):
        self.l_Name.pack()
        self.entry_Name.pack() 
        self.botao_confirm.pack()

    def unpack_labels_users(self):
        self.l_Name.pack_forget()
        self.entry_Name.pack_forget()  
        self.l_Email.pack_forget()
        self.entry_Email.pack_forget()  
        self.botao_confirm.pack_forget()


    def pack_res(self):
        self.resultado.pack()
        self.botao_ok.pack()

    def unpack_res(self):
        self.resultado.pack_forget()
        self.botao_ok.pack_forget()
        self.pack_labels()

    def res(self, txt):
        self.unpack_labels_users()
        self.resultado = tkinter.Label(self.janela, text=txt)
        self.botao_ok = tkinter.Button(self.janela, text='Ok', command= self.unpack_res)
        self.pack_res()

    def add(self):
        self.name = self.entry_Name.get().lower()
        self.email = self.entry_Email.get().lower()
        self.res(self.DB.Create(self.name, self.email))
        
    def get(self):
        self.name = self.entry_Name.get().lower()
        self.email = None
        self.res(txt=self.DB.Read(self.name))

    def set(self):
        self.name = self.entry_Name.get().lower()
        self.email = self.entry_Email.get().lower()
        self.res(txt=self.DB.Update(self.name, self.email))


    def create(self):
        self.unpack_labels()
        self.labels_user(cmd=self.add)
        self.pack_labels_users1()
        
    def read(self):
        self.unpack_labels()
        self.labels_user(self.get)
        self.pack_labels_users2()
        
    def update(self):
        self.unpack_labels()
        self.labels_user(cmd=self.set)
        self.pack_labels_users1()
        
    def delete(self):
        self.unpack_labels()
        


if __name__ == '__main__':
    functions_DB.init_DB()
    crud(functions_DB)