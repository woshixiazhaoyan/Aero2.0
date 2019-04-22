from plane_sprites import *
import plane_enemy
import plane_hero


class PlaneGame(object):

    #主程序
    def __init__(self):
        print("游戏初始化")

        #创建游戏窗口
        self.screen = pygame.display.set_mode((SCREEN_RECT.size))
        #游戏时钟
        self.clock = pygame.time.Clock()
        #创建精灵组
        self.__create_sprites()
        #设置定时器时间——创建敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(CREATE_PROPS_ENEMY_EVENT,5000)
        pygame.time.set_timer(CREATE_MEDIUM_ENEMY_EVENT,8000)
        pygame.time.set_timer(CREATE_HERO_COOL, 100)


    def __create_sprites(self):
        #背景精灵
        self.bg1 = Backgroud("./image/078.jpg")
        self.bg2 = Backgroud("./image/078.jpg")
        self.bg2.rect.y = -SCREEN_RECT.height

        #创建精灵组
        self.back_goup = pygame.sprite.Group(self.bg1, self.bg2)

        #敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        #英雄
        self.hero = plane_hero.Hero()
        self.hero_group = pygame.sprite.Group(self.hero)


    def start_game(self):
        print("游戏开始")

        while True:

            self.clock.tick(FRAME_PER_SEC)
            #监听
            self.__event_handler()
            #碰撞检测
            self.__check_collide()
            #更新，绘制精灵组
            self.__update_sprites()
            #绘制得分
            score_text = score_font.render("Score: %s" %str(score),True,[65,105,255])
            self.screen.blit(score_text,(10,5))
            #更新显示
            pygame.display.update()


    def __event_handler(self):
        #监听类
        global FIRECOOL
        for event in pygame.event.get():
            #判断退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                #创建敌机精灵
                enemy1 = plane_enemy.Enemy("./image/enemy1.png")
                #添加到精灵组
                self.enemy_group.add(enemy1)
            elif event.type == CREATE_PROPS_ENEMY_EVENT:
                enemy2 = plane_enemy.Props_Enemy("./image/enemy2.png", 2, 10)
                self.enemy_group.add(enemy2)
            elif event.type == CREATE_MEDIUM_ENEMY_EVENT:
                enemy3 = plane_enemy.MEDIUM_Enemy("./image/enemy3.png", 2, 50)
                self.enemy_group.add(enemy3)
            elif event.type == CREATE_HERO_COOL:
                FIRECOOL = True

        #英雄精灵组控制
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            if keys_pressed[pygame.K_a]:
                self.hero_group.update(-HERO_SPEED, -HERO_SPEED)
            elif keys_pressed[pygame.K_d]:
                self.hero_group.update(HERO_SPEED, -HERO_SPEED)
            else:
                self.hero_group.update(0,-HERO_SPEED)
        elif keys_pressed[pygame.K_s]:
            if keys_pressed[pygame.K_a]:
                self.hero_group.update(-HERO_SPEED, HERO_SPEED)
            elif keys_pressed[pygame.K_d]:
                self.hero_group.update(HERO_SPEED, HERO_SPEED)
            else:
                self.hero_group.update(0,HERO_SPEED)
        elif keys_pressed[pygame.K_a]:
            if keys_pressed[pygame.K_w]:
                self.hero_group.update(-HERO_SPEED, -HERO_SPEED)
            elif keys_pressed[pygame.K_s]:
                self.hero_group.update(-HERO_SPEED, HERO_SPEED)
            else:
                self.hero_group.update(-HERO_SPEED,0)
        elif keys_pressed[pygame.K_d]:
            if keys_pressed[pygame.K_w]:
                self.hero_group.update(HERO_SPEED, -HERO_SPEED)
            elif keys_pressed[pygame.K_s]:
                self.hero_group.update(HERO_SPEED, HERO_SPEED)
            else:
                self.hero_group.update(HERO_SPEED,0)

        #英雄子弹控制
        if keys_pressed[pygame.K_j]:
            if FIRECOOL == True:
                self.hero.fire(self.hero.fire_level)
                hero_fire_sound.play()
                FIRECOOL = False
            else:
                pass


    def __check_collide(self):
        global score
        #判断敌机是否撞毁英雄
        hero_die = pygame.sprite.spritecollide(self.hero,self.enemy_group,True,pygame.sprite.collide_mask)
        if hero_die :
            self.hero.kill()
            self.__game_over()
        #判断子弹击毁敌机,函数返回第一个精灵组中发生碰撞的精灵
        enemy_hit = pygame.sprite.groupcollide(self.enemy_group,hero_bullte_group,False,True,pygame.sprite.collide_mask)
        if len(enemy_hit) :
            for each in enemy_hit:
                if each in self.enemy_group:
                    each.hp -= 1
                    if each.hp <= 0:
                        score += 200
                        each.kill()
        #判断英雄是否吃到道具
        props_eat = pygame.sprite.groupcollide(self.hero_group,props_group,False,True,pygame.sprite.collide_mask)
        if len(props_eat):
            for each in props_eat:
                if each in self.hero_group:
                    if each.fire_level == 4:
                        score += 500
                    else:
                        each.fire_level += 1


    def __update_sprites(self):
        ticks = pygame.time.get_ticks()
        self.back_goup.update()
        self.back_goup.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        hero_bullte_group.update()
        hero_bullte_group.draw(self.screen)
        boom_group.update(ticks)
        boom_group.draw(self.screen)
        props_group.update()
        props_group.draw(self.screen)


    #声明静态方法
    @staticmethod
    def __game_over():
        print("你死了,游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
