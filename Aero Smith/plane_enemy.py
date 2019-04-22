from plane_sprites import *
import plane_sprites



class Enemy(pygame.sprite.Sprite):
    #敌机精灵类

    def __init__(self,image_name,speed=0,hp=1):

        super().__init__()
        self.score = 200
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.mask = pygame.mask.from_surface(self.image)
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
        self.rect.y += self.speed
        #判断是否出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        if self.hp == 0:
            boom = Boom("./image/Gun2.png",96,96,6,65,12)
            boom.rect.y = self.rect.y
            boom.rect.x = self.rect.x
            boom.add(boom_group)

class Props_Enemy(Enemy):

    def __del__(self):
        if self.hp == 0:
            level_up = Level()
            level_up.rect.x = self.rect.x
            level_up.rect.y = self.rect.y
            boom = Boom("./image/Gun2.png",96,96,6,65,12)
            boom.rect.y = self.rect.y
            boom.rect.x = self.rect.x
            boom.add(boom_group)
            level_up.add(props_group)

class MEDIUM_Enemy(Enemy):

    def __del__(self):
        if self.hp == 0:
            level_up = Level()
            level_up.rect.x = self.rect.x
            level_up.rect.y = self.rect.y
            boom = Boom("./image/Gun2.png", 96, 96, 6, 65, 12)
            boom.rect.y = self.rect.y
            boom.rect.x = self.rect.x
            boom.add(boom_group)
            level_up.add(props_group)

class Level(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./image/props_levelup.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.respeed_x = random.randint(-3,3)
        self.respeed_y = random.randint(-3,3)
        while self.respeed_x == 0 or self.respeed_y ==0:
            self.respeed_x = random.randint(-3, 3)
            self.respeed_y = random.randint(-3, 3)
        self.temp = 0
        self.rect.x = 200
        self.rect.y = 200


    def update(self):
        if self.rect.x < 0 :
            self.rect.x = 0
            self.temp = self.respeed_x
            self.respeed_x = -self.temp
        elif self.rect.y < 0:
            self.rect.y = 0
            self.temp = self.respeed_y
            self.respeed_y = -self.temp
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
            self.temp = self.respeed_x
            self.respeed_x = -self.temp
        elif self.rect.y > SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height
            self.temp = self.respeed_y
            self.respeed_y = -self.temp
        else:
            self.rect.y += self.respeed_y
            self.rect.x += self.respeed_x

    def __del__(self):
        level_up = Boom("./image/levelup.png",130,32,3,150)
        level_up.rect.x = self.rect.x
        level_up.rect.y = self.rect.y
        level_up.add(boom_group)