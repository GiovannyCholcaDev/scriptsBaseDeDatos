class Coche:
    gasolina = 0
    personas = ''
    kilometraje = 0
    tanqueLleno = True
    origen = ''
    destino = ''

    def __init__(self, gasolina, personas, kilometraje):
        self.gasolina = gasolina
        self.personas = personas
        self.kilometraje = kilometraje
        print ("Inicia con:", self.gasolina, "galones" , end=", ")
        print ("Subieron:", self.personas, "personas", end=", ")
        print ("Arranca con:", self.kilometraje, "km")
        
    
    def arrancar(self):
        if self.gasolina > 0:
            print ("Arranca")
            return
        else:
            print ("No arranca")

    def conducirX(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print ("Quedan", self.gasolina, "litros")
        else:
            print ('No se mueve')

    def conducir(self, gasolina, personas, kilometraje):
        if self.gasolina > 0:
            self.gasolina -= gasolina
            self.personas -= personas
            self.kilometraje += kilometraje
        else:
            print ('***********************No se mueve*******************************************')


    def origenDestino(self, origen, destino):
        self.origen = origen
        self.destino = destino

    def carga(self, gasolina, personas):
        self.gasolina += gasolina
        self.personas += personas
  

    def imprimir(self):
        print ("Origen:", self.origen, end=" --> ")
        print ("Destino:", self.destino)
        print ("Total Gasolina:", self.gasolina, "galones" , end=", ")
        print ("Total Personas:", self.personas, "personas", end=", ")
        print ("Total Kilometraje:", self.kilometraje, "km")

       
car = Coche(10, 10, 1500)

car.origenDestino('Matriz ITS-Japon','Campues Sur')
car.arrancar()
car.conducir(3,5,100)
car.imprimir()

car.origenDestino('Campus Sur','Trayecto a Santo Domingo')
car.carga(0,3)
car.imprimir()

car.origenDestino('Campus Sur','Santo Domingo')
car.arrancar()

car.carga(10,0)
car.imprimir()

car.conducir(12,3,500)
car.imprimir()

car.origenDestino('Santo Domingo','Matriz ITS-Japon')
car.arrancar()

car.carga(10,0)
car.imprimir()

car.conducir(15,0,700)
car.imprimir()


#car.carga(10,3)
#car.imprimir()

#car.arrancar()
#car.conducir()