# Pygame Mandelbrot fractal generator

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
size = (700, 700)
zoomfactor = (4,4) # value 5,5 good for start
MAXITER = 200

movex = 0
movey = 0


screen = pygame.display.set_mode(size)

xzoom = 1.0 * zoomfactor[0] / size[0]
yzoom = 1.0 * zoomfactor[1] / size[1]

done = False

# starting point
spos = [0,0]


def drawpixel(color, pos):
    screen.set_at(pos,color)


while(spos[0] < size[0]):
    spos[1] = 0
    x = (spos[0] - size[0]/2) + movex
    while(spos[1] < size[1]):
        y = spos[1] - size[1]/2 + movey

        curcolor = BLACK
        iters = 0
        sx = 1.0 * x * xzoom
        sy = 1.0 * y * yzoom

        z = complex(0,0)
        c = complex(sx,sy)

        while (z.real ) < 4 and iters < MAXITER:

            z = z*z +c
            iters+= 1

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
