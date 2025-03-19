Prioridades = {
    "Emergencia": "Alta", 
    "Abastecimiento": "Alta", 
    "Publico": "Media", 
    "Particular": "Baja"
}

class Automovil:
    def __init__(self, matricula, tipo=None):
        if tipo is None:  
            tipo = "Emergencia"  
        elif tipo.lower() in ["camion de verdura", "camion de carnet", "camion de carga"]:
            tipo = "Abastecimiento"
        elif tipo.lower() == "minubus":
            tipo = "Publico"
        elif tipo not in Prioridades:
            tipo = "Particular"  
        
        self.matricula = matricula
        self.tipo = tipo  
    
    def asignarAuto(ColaGeneral):
        colaAlta = []
        colaMedia = []
        colaBaja = []
        
        for auto in ColaGeneral:
            if Prioridades[auto.tipo] == "Alta":
                colaAlta.append(auto)
            elif Prioridades[auto.tipo] == "Media":
                colaMedia.append(auto)
            else:
                colaBaja.append(auto)
        
        return colaAlta, colaMedia, colaBaja

autos = [
    Automovil("123", "Emergencia"),
    Automovil("1457", "Publico"),
    Automovil("1478", "Particular"),
    Automovil("1564", "Abastecimiento"),
    Automovil("9999", "Minubus"),  
    Automovil("8888", "Camion de verdura"), 
    Automovil("6666", "Moto"),  
]

alta, media, baja = Automovil.asignarAuto(autos) 

def MostrarAutos(lista, nivel):
    print(f"Autos tipo {nivel}:")
    for auto in lista:
        print(f"Matrícula: {auto.matricula}, Tipo: {auto.tipo}")

MostrarAutos(alta, "Alta")
MostrarAutos(media, "Media")
MostrarAutos(baja, "Baja")
