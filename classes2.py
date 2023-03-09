class Fraccions:

    def __init__(self, numerador, denominador):
        self.numerador = numerador    
        self.denominador = denominador

    def imprimeix(self):
        print("Fracció:", self.numerador, "/", self.denominador)

# Hem de tenir un mètode per a multiplicar
# El mètode inclourà self i el paràmetre que li especifiquem, en aquest
# cas b

    def multiplicar(self, b):
        n = self.numerador * b.numerador
        ' Numerador de a * numerador de b'
        d = self.denominador * b.denominador
        r = Fraccions(n,d)
        return r

# Hem creat el numerador i el denominar i un objecte dins la classe


def main():
    a = Fraccions(3,2)
    a.imprimeix()

    b = Fraccions(7,4)
    b.imprimeix()

# Ara tenim la fracció a i la fracció b, però n'haurem de tenir una altra
# r, la del resultat

    r = a.multiplicar(b)  # Aquí b, ja el tenim com una fracció 7/4
                        # Per què no posem a?
    r.imprimeix()

"""
No posem a perquè self està actuant com a "a"
a extà executant el mètode
"""

if __name__ == "__main__":
    main()