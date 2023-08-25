import pygame
import math

pygame.init()

BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

screen = pygame.display.set_mode([600,600])
pygame.display.set_caption("자유낙하 시뮬레이션")

FPS = pygame.time.Clock()

Circle1_x = 200
Circle1_y = 75 # 만약 Circle2의 면적이 더 크다면 50+(Circle2의 반지름 - Circle1의 반지름)의 값 입력 아니면 50
Circle1_speed_y = 0
gravity = 0.98
A = Circle1_m = 5   #질량kg

Circle2_x = 400
Circle2_y = 50 # 만약 Circle1의 면적이 더 크다면 50+(Circle1의 반지름 - Circle2의 반지름)의 값 입력 아니면 50
Circle2_speed_y = 0
gravity = 0.98
B = Circle2_m = 10  #질량kg

P1 = Circle1_P = A*9.8*5 #위치에너지
P2 = Circle2_p = B*9.8*5

K1 = Circle1_K = A*9.8*9.8*0.5  #떨어지는 시간이 1초라 가정 운동에너지
K2 = Circle2_K = B*9.8*9.8*0.5

h1 = (P1-K1) / 9.8*A
h2 = (P2-K2) / 9.8*B



running = True

while running :
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    Circle1_speed_y += gravity
    Circle1_y += Circle1_speed_y

    Circle2_speed_y += gravity
    Circle2_y += Circle2_speed_y
    
    if Circle1_y + 25 > 550 :
        Circle1_y = 525     #550 - 5n의 값 입력 n = 질량(kg)
        Circle1_speed_y = -Circle1_speed_y* 1/h2

    if Circle2_y + 50 > 550 :
        Circle2_y = 500   #550 - 5n 의 값 입력 n = 질량(kg)
        Circle2_speed_y = -Circle2_speed_y* 1/h1

    screen.fill(BLACK)

    pygame.draw.rect(screen,GREEN,[0,550,600,50])
    
    Circle1 = pygame.draw.circle(screen,BLUE,(int(Circle1_x),int(Circle1_y)),25)#1kg-->5cm  5kg-->25cm 반지름이 25cm  nkg-->5ncm값을 반지름으로 입력

    Circle2 = pygame.draw.circle(screen,BLUE,(int(Circle2_x),int(Circle2_y)),50)#10kg--> 50cm 반지름이 50cm  nkg-->5ncm값을 반지름으로 입력

    FPS.tick(60)

    pygame.display.flip()

pygame.quit()
