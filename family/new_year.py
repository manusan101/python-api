from patricio import Patricio
from lula import Lula

def mostrar_conocimiento(Persona):
   return Persona.show_knowledge()

pato=Patricio(5)

lula= Lula(234)

pato.estudiar()
print(mostrar_conocimiento(pato))
print(mostrar_conocimiento(lula))