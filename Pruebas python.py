import time
#E Energia // C Costo // T Tiempo // RPI Repeticiones iniciales // SE Sobrante de energia // ST Sobrante de tiempo
#ET Energia nueva por tiempo // RF Repeticiones finales // NE Nueva energia // NI Nuevo intento 

T = 42
E = 415
C = 5
NI = 5
T2 = 0
RPI = E//C
RF = RPI

while NI > C-1: 
    T2 = T2 + ST  
    TC = ((4.5+T)*RPI)+T2
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