"""
Sistema de CRUD simples em python.
Autor: Stefany Izidio.
Github: https://github.com/Stefanyvitoria
Email: izidiostefany@gmail.com
"""

#Importação das bibliotecas
import functions_DB

def Entrada():
    """Recebe o comando de entrada e verifica se a entrada entá correta."""
    ent = input("Insira (c/create) para adicionar, (r/read) para consultar, \
(u/update) para atualizar ou (d/delete) para excluir um registro.\nEntrada: ").strip().lower() 
    
    opcoes = ['c','create', 'r','read', 'u', 'update','d','delete']

    while ent not in opcoes:
        if len(ent) == 0:
            raise Exception("Fim")

        print('\nEntrada Inválida!\n')
        ent = input("Insira (c/create) para adicionar, (r/read) para consultar, \
(u/update) para atualizar ou (d/delete) para excluir um registro.\nEntrada: ").strip().lower()
    
    
    return ent

def root():
    """Cria o banco de dados e gerencia as execuções. """

    functions_DB.init_DB()

    entrada = Entrada()

    if entrada.startswith('c'):
        user = input('Nome do usuário: ').lower().strip()
        email = input('E-mail: ').lower().strip()
        print(functions_DB.Create(user, email))

    elif entrada.startswith('r'): 
        user = input('Nome do usuário: ').lower().strip()
        print(functions_DB.Read(user))

    elif entrada.startswith('u'):
        user = input('Nome do usuário: ').lower().strip()
        email = input('E-mail: ').lower().strip()
        print(functions_DB.Update(user, email))
    
    elif entrada.startswith('d'):  
        user = input('Apagar usuário: ').lower().strip()
        print(functions_DB.Delete(user))

if __name__ == "__main__":
    try:   
        while True:
            root()
    except Exception as e:
         print(e.args[0])