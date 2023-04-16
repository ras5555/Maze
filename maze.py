from pygame import *

win_w = 700
win_h = 500
window = display.set_mode((win_w,win_h))
display.set_caption('Maze')
background = transform.scale(image.load('background.jpg'), (win_w,win_h))
clock = time.Clock()
FPS = 90

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')
def hiihl():
    pass
font.init()
font1 = font.SysFont("Algerian", 50)
win = font1.render('You Win', True, (0,255,0))
lose = font1.render('You Lose', True, (255,0,0))

class Gamesprite(sprite.Sprite):
    def __init__(self,player_image,x,y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 'left'

    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(Gamesprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 600:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

class Enemy(Gamesprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= 615:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self,color1, color2, color3, wall_x, wall_y, wall_w, wall_h):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_w
        self.heght = wall_h
        self.image = Surface((self.width,self.heght))
        self.image.fill((self.color1,self.color2,self.color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

wall1 = Wall(255, 255, 0, 100, 10, 400, 20)
wall2 = Wall(255, 255, 0, 100, 10, 20, 300)
wall3 = Wall(255, 255, 0, 300, 120, 20, 400)
player = Player('hero.png', 5, 400, 5)
enemy = Enemy('cyborg.png', 600, 300, 3)
treasure = Gamesprite('treasure.png', 600, 400, 0)

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        player.update()
        player.reset()
        enemy.reset()
        enemy.update()
        treasure.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()

        if sprite.collide_rect(player, treasure):
            finish = True
            money.play()
            window.blit(win, (200, 200))
        

        if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3):
            finish = True
            kick.play()
            window.blit(lose, (200,200))

    clock.tick(FPS)
    display.update()
