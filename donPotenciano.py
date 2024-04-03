class Campo:
    
    def __init__(self):
        self.superficieTotal=15
        self.superficieSembrada=10
        self.cultivo=Trigo(10)
        self.saldo=5000
        
    def cosechar(self):
        self.ingresoTotal=self.cultivo.vender()
        self.saldo=self.saldo+self.ingresoTotal
        self.superficieSembrada=0
        self.cultivo=None
        return self.saldo
    
    def sembrar(self,cereal): 
        self.cereal=cereal
        self.superficiePorSembrar=self.cereal.hectareas
        if self.superficiePorSembrar<=self.superficieTotal:
            self.cultivo=self.cereal
            self.superficieSembrada=self.cultivo.hectareas
            
    def aplicarFertilizante(self):
        self.cultivo.fertilizar()
        
    def ampliarSuperficieAlMaximo(self):
        self.superficiePorSembrar=self.superficieTotal-self.superficieSembrada
        self.cultivo.hectareas=self.cultivo.hectareas+self.superficiePorSembrar
        
    def resembrarEnSequia(self,cereal):
        self.cultivo.hectareas=self.superficieSembrada
        self.sembrar(cereal)
        
    def comenzarNuevaTemporada(self,cereal):
        self.cosechar()
        self.sembrar(cereal)
        
            
        
class Cereal:

    def __init__(self,hectareas):
        self.hectareas=hectareas
        self.fertilizado=False
    
    def fertilizar(self):
        self.fertilizado=True     
    
    def costo(self):
        pass
    
    def vender(self):
        pass        
        
class Trigo(Cereal):
    
    def __init__(self,hectareas):
        super().__init__(hectareas)
        self.tipo="trigo"
        
    def costo(self):
        return self.hectareas*500
    
    def vender(self):
        self.precioPorQuintal=1000
        self.rendimiento=10*self.hectareas
        if self.fertilizado==True:
            self.rendimiento=self.rendimiento+2
        return self.rendimiento*self.precioPorQuintal

class Soja(Cereal):
    
    def __init__(self,hectareas):
        super().__init__(hectareas)
        self.tipo="soja"
        self.precioQuintal=0
        
    def costo(self):
        return self.hectareas*500
    
    def precioDelQuintal(self,precioDolarChicago=400,precioPesos=100):
        self.precioDolarChicago=precioDolarChicago
        self.precioPesos=precioPesos
        self.precioQuintal=self.precioDolarChicago*self.precioPesos
        return self.precioQuintal
    
    def vender(self):
        
        if self.fertilizado==True:
            self.rendimiento=40*self.hectareas
        else:
            self.rendimiento=20*self.hectareas
        return self.rendimiento*self.precioDelQuintal()*0.65

class Maiz(Cereal):
    def __init__(self, hectareas,precio):
        super().__init__(hectareas)
        self.tipo="maiz"
        self.precio=precio
        
    def costo(self):
        self.costo=self.hectareas*500
        if self.costo>5000:
            self.costo=5000
        return self.costo
    
    def vender(self):
        return 15*self.hectareas*self.precio/2
    
class PrecioSoja:
    def __init__(self,precioDolar=400,precioPesos=100):
        self.precioDolar=precioDolar
        self.precioPesos=precioPesos
        self.precioSoja=self.precioDolar*self.precioPesos
        

        
campo = Campo()
campo.cosechar()
precioSojaActual=PrecioSoja().precioSoja
maiz = Maiz(5,precioSojaActual)
campo.sembrar(maiz)
campo.ampliarSuperficieAlMaximo()
print(maiz.hectareas)
print(campo.superficieSembrada)
campo.cosechar()
print(campo.saldo)




