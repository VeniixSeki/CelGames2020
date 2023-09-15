import mouse

print ("Inicio")

#Variables
NB = 450
CB = 20
T = 95

count = 0
rep = NB//CB
mouse.move(x = 0, y = 0, absolute=False, duration=5)

print(rep)

while count < rep:
    count = count +1
    print(count)
    
    mouse.move(x = 250, y = -500, absolute=False, duration=1)
    mouse.click('left')
    mouse.move(x = 0, y = 0, absolute=False, duration=.5)
    mouse.click('left')
    mouse.move(x = 0, y = 0, absolute=False, duration=.5)
    mouse.click('left')
    mouse.move(x = -250, y = 500, absolute=False, duration=1)

    mouse.click('left')
    mouse.move(x = 380, y = -165, absolute=False, duration=0.5)
    mouse.click('left')
    mouse.move(x = -380, y = +165, absolute=False, duration=0.1)
    mouse.move(x = 0, y = 0, absolute=False, duration=T)

print ("Final")