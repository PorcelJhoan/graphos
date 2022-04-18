import sys
import tkinter
import heapq
class grafo():
    def __init__(self):
        self.listav = []
        self.listaA = []


    def __str__(self):
        return str(self.listav)
        return str(self.listaA)

    def agregarVertice(self, v):
        self.listav.append(v)

    def agregarArista(self,a):
        self.listaA.append(a)

class vertice():
    nombre = ""
    x =0
    y =0
    descripcion = ""
    def __init__(self, nombre, x, y,descipcion):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.descripcion = descipcion

class arista():
    frm=vertice("",0,0,"")
    to = vertice("", 0, 0,"")

    def __init__(self, frm, to, distancia):
        self.frm = frm
        self.to = to
        self.distancia = distancia
