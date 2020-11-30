#obliquo.py
'''Calculo do alcance maximo de um projetil
lancado no campo gravitacional da Terra
Programador: Elinei Santos
Data da ultima revisao: 18/12/2016
A = (Vo*Vo*sen(2*te))/g'''
from math import sin,pi
Vo =15.0
g = 9.8
te = eval(input("Entre com o angulo\
de lancamento em graus "))
ter = (te/180.)*pi # transforma para radianos
A=Vo*Vo*sin(2.*ter)/g
print("Para um angulo de lancamento = \
%6.2f graus o alcance e de %6.4f m" %(te,A))

