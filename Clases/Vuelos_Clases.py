class Vuelos (object):
    avion = "" #modelo unico del avion que se va a utilizar en sese vuelo
    pasajeros = [] #lista de pasajeros de ese vuelo
    tripulantes = [] #lista de tripulantes que posee ese vuelo
    fecha = 0 #fecha de salida del vuelo
    hora = 0 #hora de salida del vuelo
    origen = "" #origen del vuelo
    destino = "" #destino al cual llega el vuelo

    def __init__(self):
        pasajeros = []  # lista de pasajeros de ese vuelo
        tripulantes = []  # lista de tripulantes que posee ese vuelo

    def setAvion (self, avion):
        self.avion = avion

    def FechaSalida(self, fecha):
        self.fecha = fecha

    def HoraSalida(self, hora):
        self.hora = hora

    def Origen(self, origen):
        self.origen = origen

    def Destino(self, destino):
        self.destino = destino

    def setPasajeros (self, pasajero):
        self.pasajeros.append(pasajero)

    def setTripulantes (self, tripulante):
        self.tripulantes.append (tripulante)






class Aviones (object):
    modelo = "" #modelo unico de avion
    cant_pasajeros = 0 #cantidad de pasajeros que soporta el avion
    cant_tripulacion = 0 #cantidad de tripulacion necesaria para poder volar

    def setModeloAvion (self, modelo):
        self.modelo = modelo

    def setCantidadPasajeros (self, pasajeros):
        self.cant_pasajeros = pasajeros

    def setCantidadTripulacion (self, tripulacion):
        self.cant_tripulacion = tripulacion

    #metodo que compruebe que el modelo es unico de ese avion


class Persona (object):
    Nombre = ""
    Apellido = ""
    FechadeNacimiento = 0
    DNI = 0

    def setNombre (self, nombre):
        self.Nombre = nombre

    def setApellido (self, apellido):
        self.Apellido = apellido

    def setFechaNacimiento (self, fecha):
        self.FechadeNacimiento = fecha

    def setDni (self, dni):
        self.DNI = dni


class Tripulacion (Persona):
    modelo_permitido = 0
    idiomas = ""

    def setModeloPermitido (self, modelo):
        self.modelo_permitido = modelo

    def setIdiomas (self, idioma):
        self.idiomas = idioma


class Pasajero (Persona):
    cantidad_millas = 0
    pasajero_vip = ""
    necesidades_especiales = ""


    def setCantidadMillas (self, millas):
        self.cantidad_millas = millas

    def setPasajeroVip (self, vip):
        self.pasajero_vip = vip

    def setNecesidadEspecial (self, necesidad):
        self.necesidades_especiales = necesidad


