#cap3_graf4.py
'''Exemplo de grafico simples com matplotlib
importando todos os metodos
Programador: Elinei Santos
Data da ultima revisao: 26/12/2016'''

from matplotlib.pylab import *
from math import *
t = linspace(0,50,200)
y1 = zeros(len(t))
y2 = zeros(len(t))
y3 = zeros(len(t))
for i in arange(len(t)):
    f1 = 4*exp(-0.1*t[i])*cos(1.2*t[i]+pi/6)
    f2 = 4*exp(-0.2*t[i])+2*exp(-0.2*t[i])
    f3 = (2.+3*t[i])*exp(-0.3*t[i])
    y1[i] = f1
    y2[i] = f2
    y3[i] = f3
plot(t,y1,'bo')
plot(t,y2,'r^')
plot(t,y3,'ms')
xlabel('tempo(s)', fontsize = 15)
ylabel('y(m)', fontsize = 15)
legend(['f1', 'f2', 'f3'],loc=1)
axis([0,50, -6,6])
show()
