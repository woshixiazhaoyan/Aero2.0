import random
import pygame
from pygame.locals import *


#屏幕大小
SCREEN_RECT = pygame.Rect(0,0,512,768)
#屏幕刷新率
FRAME_PER_SEC = 120
#创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
CREATE_PROPS_ENEMY_EVENT = pygame.USEREVENT + 2
CREATE_MEDIUM_ENEMY_EVENT = pygame.USEREVENT + 3
#英雄子弹间隔
CREATE_HERO_COOL = pygame.USEREVENT + 1
#英雄移动速度
HERO_SPEED = 3
#英雄子弹精灵组
hero_bullte_group = pygame.sprite.Group()
#爆炸精灵组
boom_group = pygame.sprite.Group()
#道具精灵组
props_group = pygame.sprite.Group()

pygame.init()
pygame.mixer.init()
#得分
score = 0
score_font = pygame.font.Font("./font/font.TTF",30)

pygame.mixer_music.load("./sound/background.flac")
pygame.mixer_music.set_volume(0.3)
pygame.mixer_music.play(-1)

hero_fire_sound = pygame.mixer.Sound('./sound/hero_fire.wav')
hero_fire_sound.set_volume(0.1)





class GameSprite(pygame.sprite.Sprite):

    def __init__(self,image_name,speed=1):

        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.mask = pygame.mask.from_surface(self.image)


    def update(self):
        self.rect.y += self.speed


class Backgroud(GameSprite):
    #游戏背景精灵
    def update(self):

        #调用父类方法实现
        super().update()

        #判断是否出屏幕
        if self.rect.y>=SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Boom(pygame.sprite.Sprite):

    def __init__(self,image_name,width,height,last,space = 0,y_deviation = 0):
        super().__init__()
        self.image = None
        self.master_image = pygame.image.load(image_name).convert_alpha()
        self.rect = pygame.Rect(0,0,0,0)
        self.max = self.master_image.get_rect()
        self.max_x = self.max.width
        self.max_y = self.max.height
        self.frame_last = last
        self.frame = 0
        self.frame_first = 0
        self.width = width
        self.height = height
        self.last_time = 0
        self.frame_x = 0
        self.old_ticks = 0
        self.old_frame = None
        self.y_deviation = y_deviation
        self.space = space

    def update(self,ticks):

        if ticks > self.old_ticks + self.space:
            self.frame += 1
            if self.frame == self.frame_last:
                self.frame = 0
                self.old_frame = self.frame
                self.kill()
            self.old_ticks = ticks


        if self.frame != self.old_frame:
            rect = (self.frame_x,0,self.width ,self.height)
            self.image = self.master_image.subsurface(rect)
            self.rect.y -= self.y_deviation
            self.frame_x += self.width
            self.old_frame = self.frame

    def __del__(self):
        pass




'''def get_screen_rect():
    global SCREEN_RECT
    return SCREEN_RECT'''


'''class Enemy(GameSprite):
    #敌机精灵类

    def __init__(self,image_name,speed=0,hp=1):

        #创建敌机精灵，指定图片
        super().__init__(image_name)
        #指定敌机初始速度
        if speed == 0:
            self.speed = random.randint(2,3)
        else:
            self.speed = speed
        if hp == 1:
            self.hp = 1
        else:
            self.hp = hp
        #随机敌机初始位置
        self.rect.bottom = 0


        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

    def update(self):
        #调用父类方法 保持垂直方向飞行
        super().update()
        #判断是否出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        print("敌机挂了 %s" % self.rect)'''


'''class Hero(GameSprite):
    #英雄精灵
    def __init__(self):
        super().__init__("./image/hero0.png",0)

        #设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120



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

    def fire(self):
        #创建英雄子弹精灵
        hero_bullte = Bullte("./image/hero_bullet.png",-7)

        #设定位置
        hero_bullte.rect.bottom = self.rect.y - 5
        hero_bullte.rect.centerx  = self.rect.centerx

        hero_bullte.add(hero_bullte_group)

    def __del__(self):
        pass'''