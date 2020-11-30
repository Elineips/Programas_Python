#circulosrosetacor.py
'''Desenha uma roseta composta por 4 circulos coloridos
Programador: Elinei Santos
Data da ultima revisao: 25/04/2017'''
import turtle #importa o modulo turtle
caneta = turtle.Pen() #cria um objeto caneta
turtle.bgcolor("white")
cores = ["red", "black", "blue", "green"]
for x in range(4):
    caneta.pencolor(cores[x%4])
    caneta.circle(60) #segue para frente em pixels = lado
    caneta.left(90)    #gira 90 graus a para esquerda a caneta

