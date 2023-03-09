class grau_universitari:
    pass
    def __init__(self, nom, tipus):
        self.nom = nom
        self.tipus = tipus

    def descripció(self):
        return '{} és un grau de tipus {}'.format(self.nom, self.tipus)

class enginyeria(grau_universitari):
    def Tecnològic(self, tipustecnològic):
        return '{} tipus de grau: {}'.format(self.nom,tipustecnològic)

class història(grau_universitari):
    def Humanístic(self, tipushumanístic):
        return '{} tipus de grau: {}'.format(self.nom,tipushumanístic)

nou_grau_universitari = enginyeria('Enginyeria Electrònica','tecnològic')
print(nou_grau_universitari.descripció())