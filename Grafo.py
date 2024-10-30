"""
Created on Tuesday 29/10/24

@author: Victor Mendoza
"""
class Grafo:
    def __init__(self):
        self.Relaciones = []
        self.Recorrido1 = []
        self.Recorrido2 = []
        self.suma = 0

    def insertar_aristas(self, origen, destino, costo):
        self.Relaciones.append((origen,destino, costo))

    def mostrar_relaciones(self):
        for origen, destino, costo in self.Relaciones:
            print(f"{origen} - {destino} : {costo}")
    
    def recorrido_sinrepetir(self):
        self.suma = 0
        for origen, destino, costo in self.Relaciones:
            if origen not in self.Recorrido1:
                self.Recorrido1.append(origen)
                print(f"{origen} - {destino} : {costo}")
                self.suma += costo
        print("\nEl costo de este recorrido es:",self.suma)

    def recorrido_conrepeticion(self):
        self.suma = 0
        for origen, destino, costo in self.Relaciones:
            if origen not in self.Recorrido2:
                self.Recorrido2.append(origen)
                print(f"{origen} - {destino} : {costo}")
                self.suma += costo
        print(f"{self.Relaciones[-2][1]} - {self.Relaciones[0][0]} : {self.Relaciones[5][2]}")
        self.suma += self.Relaciones[5][2]
        print("\nEl costo de este recorrido es:",self.suma)

G = Grafo()

Estados = ["Sinaloa", "Sonora", "Chihuahua", "Coahuila", "Nuevo León", "Zacatecas", "Durango",]
Costos = [230, 520, 250, 310, 440, 230, 400, 250, 340]

for i in range(7):
    if i == 0:
        G.insertar_aristas(Estados[i], Estados[i + 1], Costos[i])
        G.insertar_aristas(Estados[i], Estados[i + 2], Costos[i + 1])
        G.insertar_aristas(Estados[i], Estados[i + 6], Costos[i + 2])
    elif i > 0 and i < 5:
        G.insertar_aristas(Estados[i], Estados[i + 1], Costos[i + 3])
    elif i > 5:
        G.insertar_aristas(Estados[i], Estados[i - 1], Costos[i + 1])
        G.insertar_aristas(Estados[i], Estados[i - 3], Costos[i + 2])

print("La relacion - costo de los estados es la siguiente:\n")
G.mostrar_relaciones()

print("\nEl recorrido de los 7 estados sin repetir es:\n")
G.recorrido_sinrepetir()

print("\nEl recorrido con al menos una repetición es:\n")
G.recorrido_conrepeticion()