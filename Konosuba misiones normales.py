import mouse

print ("Enchilada")

#E Energia // C Costo // T Tiempo // RPI Repeticiones iniciales // SE Sobrante de energia // ST Sobrante de tiempo
#ET Energia nueva por tiempo // 
T = 45
E = 147
C = 5
NI = 5
T2 = 0
ST = 0
RPI = E//C
RF = RPI

while NI > C-1: 
    T2 = T2 + ST  
    TC = ((7.5+T)*RPI)+T2
    SE = E % C
    ET = TC//180
    ST = TC % 180
    NI = ET + SE
    NE = NI//5
    RF = RF + NE
    E = SE + NE
    RPI = E//C
    T2=0

print("Energia final =",RF)


mouse.move(x = 0, y = 0, absolute=False, duration=5)

count = 0
while count < RF:
    mouse.move(x = 250, y = -500, absolute=False, duration=1)
    mouse.click('left')
    mouse.move(x = 0, y = 0, absolute=False, duration=.5)
    mouse.click('left')
    mouse.move(x = 0, y = 0, absolute=False, duration=.5)
    mouse.click('left')
    mouse.move(x = -250, y = 500, absolute=False, duration=1)

    mouse.click('left')
    mouse.move(x = 0, y = 0, absolute=False, duration=3)
    mouse.click('left')
    mouse.move(x = 100, y = -150, absolute=False, duration=0.5)
    mouse.click('left')
    mouse.move(x = -100, y = +150, absolute=False, duration=0.1)
    count = count + 1
    mouse.move(x = 0, y = 0, absolute=False, duration=T)

print ("Finalizo")
