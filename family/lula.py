from persona import Persona

class Lula(Persona):

    def __init__ (self,knowledge):
        super().__init__(knowledge)
        self.knowledge=knowledge

   
    def estudiar(self):
        self.knowledge= self.knowledge+100 
    