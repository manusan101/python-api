from person import Person

class Lula(Person):
    def __init__ (self,knowledge):
        super().__init__(knowledge)

    def study(self):
        self.setKnowledge(self.knowledge()+120)

    def amnesia(self):
        self.setKnowledge(self.knowledge()-50)