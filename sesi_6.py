import pygame as pg
import random as ran

pg.init()

width, height = 800, 450
screen = pg.display.set_mode((width, height))  # Perbaikan di sini
pg.display.set_caption("Dodge")

image = pg.image.load("/Users/aainayyahm/Documents/Kelas Game Development/image1.jpg")
image = pg.transform.scale(image, (800, 450))

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

fps = 60
clock = pg.time.Clock()


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height - 50)
        self.speed = 5

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT] and self.rect.right < width:  # Perbaikan di sini
            self.rect.x += self.speed
        if keys[pg.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN] and self.rect.bottom < height:  # Perbaikan di sini
            self.rect.y += self.speed

class Enemies(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50,50))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = ran.randint(0, width - 5)
        self.rect.y = ran.randint(-10, -5)
        self.speed = ran.randint(5,10)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > height:
            self.rect.x = ran.randint(0, width - 50)
            self.rect.y = ran.randint(-100, -50)
            self.speed = ran.randint(5, 10)

all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(5):
    enemy = Enemies()
    all_sprites.add(enemy)
    enemies.add(enemy)

score = 0
start = pg.time.get_ticks()

running = True
game_over = False
while running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    if not game_over:
        all_sprites.update()

        hits = pg.sprite.spritecollide(player, enemies, False)
        if hits:
            game_over = True
            game_over_time = (pg.time.get_ticks() - start) // 1000

        score = (pg.time.get_ticks() - start) // 1000

    screen.blit(image, (0, 0))

    all_sprites.draw(screen)

    font = pg.font.SysFont(None,30)
    text = font.render(f"Score: {score}", True, white)
    screen.blit(text,(10,10))

    if game_over:
        over_text = font.render(f"Game Over! Final Score: {game_over_time}", True, white)
        screen.blit(over_text, (width // 2 - 150, height // 2))
    

    pg.display.flip()
    clock.tick(fps)  # Tambahkan batasan fps
pg.quit()
