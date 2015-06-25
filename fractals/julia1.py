# Pygame Julia fractal generator

import pygame

pygame.init()

BLACK = (0, 0, 0)

icol =(
    (204,0,102),
    (204,0,204),
    (102,0,204),
    (0,0,204),
    (0,102,204),
    (0,204,204),
    (0,204,102),
    (0,204,0),
    (102,204,0),
    (172,119,20),
    (20,213,60),
    (0,250,192)
)

# variables
size = (1000, 800)
zoomfactor = (3,3)
MAXITER = 200

# see Julia set wiki for example values for c
c_real = -0.123 # real
c_img = 0.746 # imag

movex = 0
movey = 0


screen = pygame.display.set_mode(size)

xzoom = 1.0 * zoomfactor[0] / size[0]
yzoom = 1.0 * zoomfactor[1] / size[1]

done = False

# starting point
spos = [0,0]
c = complex(c_real,c_img)

def drawpixel(color, pos):
    screen.set_at(pos,color)


while(spos[0] < size[0]):
    spos[1] = 0
    x = (spos[0] - size[0]/2) + movex
    while(spos[1] < size[1]):
        y = spos[1] - size[1]/2 + movey

        curcolor = BLACK

        zre = 1.0 * x * xzoom
        zim = 1.0 * y * yzoom

        z = complex(zre,zim)
        z = z * z + c

        iters = 0

        while iters < MAXITER:
            if z.real >4 or z.imag > 4: break
            z = z * z + c
            iters += 1

        if iters >= MAXITER:
            curcolor = BLACK
        else:
            curcolor = icol[iters % 12] #

        drawpixel(curcolor,spos)

        #pygame.display.flip()

        spos[1] += 1
    pygame.display.update()
    spos[0] += 1


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
ygame.quit()
