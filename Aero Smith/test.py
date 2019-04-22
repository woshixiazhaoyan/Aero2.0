import sys,pygame
import random
from pygame.locals import *
import plane_enemy

clock = pygame.time.Clock()
screen = pygame.display.set_mode((512,768))
paodan = pygame.image.load("./image/Gun2.png")
rect = (0,0,118,77)
rect1 = Rect(100,100,200,100)
test = paodan.get_rect()

paodan1 = paodan.subsurface(rect)
#paodan2 = paodan.subsurface(rect1)


while True:
    for event in pygame.event.get():
        # 判断退出游戏
        speed = random.randint(-5, 5)
        print(speed)
        if event.type == pygame.QUIT:
            sys.exit()

    ticks = pygame.time.get_ticks()
    clock.tick(60)
    print(ticks)
    sss = plane_enemy.Level()
    aaa = plane_enemy.Enemy("./image/enemy1.png")
    sss_gourp = enemy_group = pygame.sprite.Group()
    sss.add(sss_gourp)
    sss_gourp.update()
    sss_gourp.draw(screen)
    abc = 0
    abc += 3

    screen.blit(paodan1, (abc, 200))
    pygame.display.update()