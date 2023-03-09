class race_types:
    pass
    def __init__(self, type1, type_race):
        self.type1 = type1
        self.type_race = type_race
        
    def frase(self):
        return '{} és un tipus de cursa de {}'.format(self.type1, self.type_race)
        
class road(race_types):
    def Road(self, typeroad):
        return '{} tipus de cursa: {}'.format(self.type1, typeroad)
        
class mountain(race_types):
    def Mountain(self, typemountain):
        return '{} tipus de cursa: {}'.format(self.type1, typemountain)
        
class track(race_types):
    def Track(self, typetrack):
        return '{} tipus de cursa: {}'.format(self.type1, typetrack)
        
type_of_race = mountain('Skyrunning', '25 km')
print(type_of_race.frase())