class Entity():
    def __init__(self, id : int):
        self.id = id

class Aluno():
    def __init__(self, name : str, email : str):
        super()
        self.name = name
        self.email = email