from plane_sprites import *

HERO_BULLTE_SPEED = -10

class Hero(pygame.sprite.Sprite):
    #英雄精灵
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./image/hero0.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        #设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.fire_level = 1



    def update(self,xspeed=0,yspeed=0):

        self.rect.x += xspeed
        self.rect.y += yspeed

        if self.rect.x < 0 :
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y >= SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height

    def fire(self,fire_level):
        if fire_level == 1:
            #创建英雄子弹精灵
            hero_bullte = Bullte("./image/hero_bullet.png",HERO_BULLTE_SPEED)
            #设定位置
            hero_bullte.rect.bottom = self.rect.y + 5
            hero_bullte.rect.centerx  = self.rect.centerx
            hero_bullte.add(hero_bullte_group)
        elif fire_level == 2:
            hero_bullte = Bullte("./image/hero_bullet.png", HERO_BULLTE_SPEED)
            hero_bullte1 = Bullte("./image/hero_bullet.png",HERO_BULLTE_SPEED)
            # 设定位置
            hero_bullte.rect.bottom = self.rect.y + 5
            hero_bullte.rect.centerx = self.rect.centerx - 10
            hero_bullte1.rect.bottom = self.rect.y + 5
            hero_bullte1.rect.centerx = self.rect.centerx + 10
            hero_bullte.add(hero_bullte_group)
            hero_bullte1.add(hero_bullte_group)
        elif fire_level == 3:
            hero_bullte = Bullte("./image/hero_bullet.png", HERO_BULLTE_SPEED)
            hero_bullte1 = Bullte("./image/hero_bullet.png",HERO_BULLTE_SPEED)
            hero_bullte2 = Bullte("./image/hero_bullet.png", HERO_BULLTE_SPEED)
            # 设定位置
            hero_bullte.rect.bottom = self.rect.y - 5
            hero_bullte.rect.centerx = self.rect.centerx
            hero_bullte1.rect.bottom = self.rect.y + 5
            hero_bullte1.rect.centerx = self.rect.centerx - 15
            hero_bullte2.rect.bottom = self.rect.y + 5
            hero_bullte2.rect.centerx = self.rect.centerx + 15

            hero_bullte.add(hero_bullte_group)
            hero_bullte1.add(hero_bullte_group)
            hero_bullte2.add(hero_bullte_group)
        elif fire_level == 4:
            hero_bullte = Bullte("./image/hero_bullet.png", HERO_BULLTE_SPEED)
            hero_bullte1 = Bullte("./image/hero_bullet.png",HERO_BULLTE_SPEED)
            hero_bullte2 = Bullte("./image/hero_bullet.png", HERO_BULLTE_SPEED)
            hero_bullte3 = Bullte("./image/hero_bullet.png", HERO_BULLTE_SPEED)
            # 设定位置
            hero_bullte.rect.bottom = self.rect.y - 5
            hero_bullte.rect.centerx = self.rect.centerx - 8
            hero_bullte1.rect.bottom = self.rect.y - 5
            hero_bullte1.rect.centerx = self.rect.centerx + 8
            hero_bullte2.rect.bottom = self.rect.y + 5
            hero_bullte2.rect.centerx = self.rect.centerx - 25
            hero_bullte3.rect.bottom = self.rect.y + 5
            hero_bullte3.rect.centerx = self.rect.centerx + 25

            hero_bullte.add(hero_bullte_group)
            hero_bullte1.add(hero_bullte_group)
            hero_bullte2.add(hero_bullte_group)
            hero_bullte3.add(hero_bullte_group)

    def __del__(self):
        pass

class Bullte(GameSprite):

    def update(self):
        super().update()

        if self.rect.bottom < 0:
            self.kill()


    def __del__(self):

        Bullte_die = Boom("./image/bullet_hit.png",45,45,2,65)
        Bullte_die.rect.x = self.rect.x - 5
        Bullte_die.rect.y = self.rect.y
        Bullte_die.add(boom_group)