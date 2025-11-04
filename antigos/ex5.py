class Animal:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print("O animal emitiu um som generico.")

   
class Cachorro(Animal):

    def emitir_som(self):
        print(f"O cachorro {self.nome} latiu.")

class Gato(Animal):
    def emitir_som(self):
        print(f"O gato {self.nome} miou.")


# Testando as classes
animal = Animal("Animal Generico", 5)
animal.emitir_som()
cachorro = Cachorro("Totó", 3)
cachorro.emitir_som()
gato = Gato("Mimi", 2)
gato.emitir_som()




