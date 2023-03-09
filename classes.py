class Moto():
    rodes = 2
    ample = 0,7
    llarg = 2
    
    en_marxa = False
    
    def arrencar(self):
        self.en_marxa = True
        
    def estat(self):
        if self.en_marxa == True:
            print("La moto esta en marxa")
        elif self.en_marxa == False:
            print("La moto està parada")
            
