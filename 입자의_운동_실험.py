import pygame, sys  # 파이썬 게임 묘듈 import 
from pygame.locals import *

pygame.init() # 파이 게임 초기화 
screen = pygame.display.set_mode((480, 320)) #화면 크기 설정
pygame.display.set_caption('입자의 운동') # 타이틀 제목


# 색깔 변수 
BLACK 	= (	0, 	0,	0)
WHITE 	= (255,255,255)
RED	   	= (255, 0,	0)
GREEN 	= (	0,255,	0)
BLUE	= (	0, 	0,255)

# 공 변수
x = 480 / 2
y = 320 - 30
dx = 0.1
dy = -0.1

# draw 함수 정의
def drawBall():
	pygame.draw.circle(screen,BLUE,(int(x),int(y)),7)

def draw():
	screen.fill(WHITE)
	drawBall()

while True:
	# 이벤트 처리
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	# 그리기 함수 호출
	draw()

	# 공과 벽돌 충돌 검사
	if x + dx > 480-7 or x + dx < 7:
		dx = -dx
	if y + dy > 320-7 or y + dy < 7:
		dy = -dy

	# 공 이동
	x += dx
	y += dy
	
	# 모듈 갱신
	pygame.display.update()