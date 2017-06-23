class Aluno():

    def __init__(self, id, nome, matricula, curso, semestre, idade):
        self.id = id
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.semestre = semestre
        self.idade = idade

class Curso():

    def __init__(self, id, nome, horasduracao):
        self.id = id
        self.nome = nome
        self.horasduracao = horasduracao

class Materia():

    def __init__(self, id, nome, numaulas):
        self.id = id
        self.nome = nome
        self.numaulas = numaulas

class Nota():

    def __init__(self, id, NP1, NP2, alunoid, materiaid):
        self.id = id
        self.NP1 = NP1
        self.NP2 = NP2
        self.NP3 = None
        self.NF = None
        self.situacao = None
        self.alunoid = alunoid
        self.materiaid = materiaid
