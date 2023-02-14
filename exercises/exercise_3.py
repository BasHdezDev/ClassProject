# 3. A la clase del punto anterior, defínale los siguientes métodos:

# - Un método mostrar que imprima por consola las coordenadas del punto
# - Un método mover que cambie las coordenadas del punto
# - Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.

import math


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def show(self):
        print(f"You are located in {self.x} for x, and {self.y} for y, ({self.x},{self.y})")

    def move(self, distance_x: int, distance_y: int):

        math_x = self.x + distance_x
        math_y = self.y + distance_y

        self.x = math_x
        self.y = math_y

    def distance_math(self, point):

        solution = math.sqrt(((self.x - point.x)**2)+((self.y - point.y)**2))




