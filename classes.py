class Dog:
    def __init__(self, cor_de_pelo, idade, tamanho, nome):
        self.cor_de_pelo = cor_de_pelo
        self.idade = idade
        self.tamanho = tamanho
        self.nome = nome
    def latir(self):
        print('AU AU')
    def correr(self):
        print(f'{self.nome} está correndo')

dog_1 = Dog('branco', 4, 'medio', 'danny')

dog_1.idade = 6

print(dog_1.idade)
dog_1.latir()
dog_1.correr()

dog_2 = Dog('preto', 3, 'grande', 'Bob')
