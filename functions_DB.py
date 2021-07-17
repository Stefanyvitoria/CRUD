import dbm

def init_DB():
    db = dbm.open('Banco', 'c')
    db.close()

def Create(user: str, email: str):
    """Adiciona um novo registro."""
    db = dbm.open('Banco', 'w')
    if user in db:
        return f'Usuário já existe nos registros!'
    else:
        db[user] = email
        return f'Usuário criado com sucesso!'

def Read(user: str):
    """Consulta um registro."""
    db = dbm.open('Banco', 'r')
    if user in db: 
        return f'E-mail: {db[user].decode()}'
    else:
        return 'Usuário não encontrado nos registros!'
    
def Update(user: str, email: str): 
    """Atualiza um registro."""
    db = dbm.open('Banco', 'w')
    if user in db:
        db[user] = email
        return 'Usuário Atualizado!'
    else:
        return 'Usuário não encontrado nos registros!'

def Delete(user):
    """Apaga um registro."""
    db = dbm.open('Banco', 'w')
    if user in db:
        del db[user]
        return 'Usuário Deletado!'
    else:
        return 'Usuário não encontrado nos registros!'