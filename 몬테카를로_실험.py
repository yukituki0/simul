import pygame as pg
import random

screen = pg.display.set_mode([200,200])

def main():
    screen.fill((255,255,255))

    A = 0
    B = 0
    A1 = []
    B1 = []
    running=True
    while running:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                running = False

        x=random.randint(0,200)
        y=random.randint(0,200)

        if x*x+y*y<=40000:
            A1.append([x,y])
            A += 1
        else:
            B1.append([x,y])
            B += 1

        screen.fill((255,255,255))

        for i in A1:
                pg.draw.circle(screen, (255,0,0),i,1)
        
        for i in B1:
                pg.draw.circle(screen, (0,0,255),i,1)
        
        font=pg.font.SysFont("arial",20,True,False)

        text = font.render(f"{4*A/(A+B)}",True,(0,0,0))

        screen.blit(text,(10,150))


        pg.display.flip()
    


if __name__=="__main__":
    pg.init()
    main()
    pg.quit()




    