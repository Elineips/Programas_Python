#cap3_graf1v2.py
'''Exemplo de grafico simples com legenda
usando o modulo matplotlib
Programador: Elinei Santos
Data da ultima revisao: 26/12/2016'''

from matplotlib.pylab import *
from math import *
t = linspace(0,30,200)
y1 = zeros(len(t))
y2 = zeros(len(t))
for i in arange(len(t)):
    f1 = 8*exp(-0.2*t[i])*cos(2.*t[i])
    f2 = 10*exp(-0.15*t[i])*cos(2.5*t[i])
    y1[i] = f1
    y2[i] = f2
plot(t,y1,'b-',linewidth = 2)
#hold('on') #utilizado em versoes mais antigas
plot(t,y2,'r-.', linewidth = 3)
title('Oscilador harmonico amortecido')
xlabel('tempo(s)', fontsize = 15)
ylabel('y(m)', fontsize = 15)
legend(['f1-oscil1', 'f2-oscila2'])
axis([0,30, -8,8])
show()
