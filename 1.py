class Elements_electrònics:
    pass
    def __init__(self, any_fabricació, codi, marca):
        self.any_fabricació = any_fabricació
        self.codi = codi
        self.marca = marca
    def frase(self):
        return "Aquest element es va fabricar l'any {}, porta aquest codi: {}. És de la marca {}.".format(
            self.any_fabricació, self.codi, self.marca
        )

class Perifèrics(Elements_electrònics):
    pass
    def __init__(self, any_fabricaió, codi, marca, tipus):
        Perifèrics.__init__(tipus)
        self.tipus = tipus
    def frase(self):
        return "Aquest Perifèric es de tipus: {}".format(self.tipus)

class Portàtils(Elements_electrònics):
    pass
    def __init__(self, any_fabricació, codi, marca, sistema_operatiu):
        Portàtils.__init__(sistema_operatiu)
        self.sistema_operatiu = sistema_operatiu
    def frase(self):
        return "Aquest Portàtil porta el següent sistema operatiu: {}.".format(self.sistema_operatiu)

class Chromebooks(Portàtils):
    pass
    def __init__(self, any_fabricació, codi, marca, sistema_operatiu, Persona):
        Chromebooks.__init__(Persona)
        self.Persona = Persona
    def frase(self):
        return "El chromebook pertany a un {}.".format(self.Persona)
    
Element_nou = Perifèrics(1999, 'frnti34ugnk3n4gn', 'Windows', 'Portàtil')
print(Element_nou.frase())

