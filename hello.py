class Pessoa:
    #construtor
    def __init__(self, n, i, a):
        self.nome = n
        self.i = i
        self.a = a
    #metodo para representar o objeto como uma string
    def __str__(self):
        return "Nome:"+self.nome+" Idade:"+str(self.i)+" Altura:"+str(self.a)  

    def ehMaiorIdade(self):
        return self.i >= 18

    def ehMaior(self, outra):
        return self.a > outra.a


class Aluno(Pessoa):
    def __init__(self,n,i,a,d):
        Pessoa.__init__(self,n,i,a)  #chama o construtor padrao da classe Pessoa
        self.disciplinas = d

    def cursando(self, disc):
        return disc in self.disciplinas
    def __str__(self):
        return Pessoa.__str__(self)+" Disciplinas:"+str(self.disciplinas)

class Professor(Pessoa):
    def __init__(self,n,i,a,dept):
        Pessoa.__init__(self,n,i,a)  #chama o construtor padrao da classe Pessoa
        self.departamento = dept
    
    def __str__(self):
        return Pessoa.__str__(self)+" Departamento:"+self.departamento



eduardo = Professor("Eduardo", 17, 1.75, "CIC")
pedro = Aluno("Pedro", 35, 1.64, ["ED", "APC", "C2"])
paulo = Pessoa("Paulo", 50, 1.50)



print(eduardo)
print(pedro)
print(paulo)
print(eduardo.nome)
print(pedro.i)
print(eduardo.ehMaiorIdade())
print(pedro.ehMaiorIdade())
print(pedro.ehMaior(eduardo))
print(eduardo.ehMaior(pedro))
print(eduardo.ehMaior(eduardo))
print(eduardo.departamento)
print(pedro.disciplinas) 
