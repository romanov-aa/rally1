import pygame as pg
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

SIZE = WIDTH, HEIGT = 800, 600
GRAY = (128, 128, 128)
GREEN = (0, 128, 0)
WHITE = (200, 200, 200)

bg_image = pg.image.load('Image/road.jpg')
bg_image_rect = bg_image.get_rect(topleft=(0, 0))
bg_image_2_rect = bg_image.get_rect(topleft=(0, 600 - HEIGT))
car1_image = pg.image.load('Image/car1.png')


pg.init()
pg.display.set_caption('Rally ')
screen = pg.display.set_mode(SIZE)

FPS = 144
clock = pg.time.Clock()


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('Image/car4.png')


class Car(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, s, img):
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.image = pg.transform.flip(car1_image, False, True)
        self.image = pg.image.load('Image/car1.png')
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.speed = s
        self.rect = self.image.get_rect(center=(self.x, self.y))


play = Player()
play_image = play.image
play_w, play_h = play.image.get_width(), play.image.get_height()
play.x, play.y = (WIDTH - play_w) // 2, (HEIGT - play_h) // 2


car1 = Car(WIDTH // 2 + 80, (HEIGT - car1_image.get_height()) // 2, car1_image.get_width(), car1_image.get_height(), 1, car1_image)
car1_image = car1.image
car1_w, car1_h = car1.image.get_width(), car1.image.get_height()
car1.x, car1.y = (WIDTH - car1_w) // 2 + 80, (HEIGT - car1_h) // 2


def bg():
    pg.draw.line(screen, GREEN, (20, 0), (20, 600), 40)
    pg.draw.line(screen, GREEN, (780, 0), (780, 600), 40)
    for xx in range(10):
        for yy in range(10):
            pg.draw.line(
                screen, WHITE, 
                (40 + xx * 80, 0 if xx == 0 or xx == 9 else 10 + yy * 60),
                (40 + xx * 80, 600 if xx == 0 or xx == 9 else 50 + yy * 60), 5
            )


game = True

while game:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False
        

    bg_image_rect.y += 1
    if bg_image_rect.y > HEIGT:
        bg_image_rect.y = 0
    bg_image_2_rect.y += 1
    if bg_image_2_rect.y > 0:
        bg_image_2_rect.y = -HEIGT
    
    screen.fill(GRAY)
    #bg()
    for i in range(2):
        screen.blit(bg_image, bg_image_rect if i == 0 else bg_image_2_rect)
    #screen.blit(bg_image, bg_image_2_rect)
    screen.blit(car1_image, car1.rect)
    screen.blit(play_image, (play.x, play.y))
    pg.display.update()
    clock.tick(FPS)
    pg.display.set_caption(f'Rally   FPS: {int(clock.get_fps())}')

#pg.image.save(screen, 'road.jpg')
