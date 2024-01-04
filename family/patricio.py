from person import Person

# Patricio es una clase que hereda de Person
class Patricio(Person):
    def __init__ (self,knowledge):
        super().__init__(knowledge)

    # Redefinimos la funcion study
    def study(self):
        self.setKnowledge(self.knowledge()+100)

    # Simpre que se llama a un atributo de la clase Person,
    # vamos a utilizar los getters y setters.