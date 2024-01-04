from abc import ABC, abstractclassmethod

class Person(ABC):
    @abstractclassmethod
    def __init__ (self,knowledge):
        self.__knowledge=knowledge
    
    def knowledge(self):
        return self.__knowledge

    def setKnowledge(self,knowledge):
        self.__knowledge = knowledge

    @abstractclassmethod
    def study(self):
        pass