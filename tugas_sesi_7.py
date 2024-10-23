import pygame as pg
import random as ran

pg.init()
pg.mixer.init()

width, height = 800, 450
screen = pg.display.set_mode((width, height)) 
pg.display.set_caption("Dodge")

background = pg.image.load("image1.jpg")
background = pg.transform.scale(background, (800, 450))

sound_effect = pg.mixer.Sound("Warsong.mp3")
sound_effect.set_volume(0.5)
sound_effect.play(-1)

sound_hit = pg.mixer.Sound("alarmSound.wav")
sound_hit.set_volume(0.1)

sound_shot = pg.mixer.Sound("collected.wav")
sound_shot.set_volume(0.1)


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

fps = 60
clock = pg.time.Clock()

highest_score = 0

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("character.png")
        self.image = pg.transform.smoothscale(self.image, (60, 80))
        # self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height - 50)
        self.speed = 5

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT] and self.rect.right < width:  
            self.rect.x += self.speed
        # if keys[pg.K_UP] and self.rect.top > 0:
        #     self.rect.y -= self.speed
        # if keys[pg.K_DOWN] and self.rect.bottom < height: 
        #     self.rect.y += self.speed

class Senjata(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("senjata.png")
        self.image = pg.transform.smoothscale(self.image, (50, 50))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 10  
        if self.rect.bottom < 0:
            self.kill()  

class Enemies(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("pesawat.png")
        self.image = pg.transform.smoothscale(self.image, (50, 50))
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


def draw_text(text, font, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, (x,y))

def draw_button(text, x, y, w, h, inactive_color, active_color, action=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pg.draw.rect(screen, active_color, (x,y,w,h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pg.draw.rect(screen, inactive_color, (x,y,w,h))
    
    font = pg.font.SysFont(None, 40)
    text_surf = font.render(text, True, white)
    screen.blit(text_surf, (x+25,y+13))

def start_game():
    all_sprites = pg.sprite.Group()
    enemies = pg.sprite.Group()
    senjata_group = pg.sprite.Group()

    player = Player()
    all_sprites.add(player)

    for i in range(10):
        enemy = Enemies()
        all_sprites.add(enemy)
        enemies.add(enemy)

    global highest_score
    score = 0
    level = 1

    running = True
    game_over = False
    while running:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            # Button UP untuk menembakkan senjata
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    senjata = Senjata()
                    senjata.rect.centerx = player.rect.centerx  
                    senjata.rect.top = player.rect.top  
                    all_sprites.add(senjata)
                    senjata_group.add(senjata)

        if score >= 10 * level:
            level += 1
            for i in range(10):
                enemy = Enemies()
                enemy.speed = ran.randint(2 + level, 6 + level)
                all_sprites.add(enemy)
                enemies.add(enemy)

        if not game_over:
            all_sprites.update()

            for senjata in senjata_group:
                hits = pg.sprite.spritecollide(senjata, enemies, True)  
                if hits:
                    sound_shot.play()
                    score += 1  
                    senjata.kill() 

            hits = pg.sprite.spritecollide(player, enemies, False)
            if hits:
                sound_hit.play()
                game_over = True 

                if score > highest_score:
                    highest_score = score  


        screen.blit(background, (0, 0))

        all_sprites.draw(screen)

        font = pg.font.SysFont(None, 30)
        text = font.render(f"Score: {score}", True, black)
        screen.blit(text, (10, 10))

        font = pg.font.SysFont(None, 30)
        text = font.render(f"Level: {level}", True, black)
        screen.blit(text, (10, 35))

        if game_over:
            over_text = font.render(f"Game Over! Your Best Score: {highest_score}", True, black)
            screen.blit(over_text, (width // 2 - 165, height // 3))

            draw_button("Restart Game", width // 3, height // 2, 250, 50, blue, red, start_game)

            sound_effect.stop()
            sound_shot.stop()

        pg.display.flip()
        clock.tick(fps)

    pg.quit()


def main_menu():
    menu = True
    while menu:
        screen.blit(background, (0,0))

        font = pg.font.SysFont(None, 70)
        draw_text("Dodge the Enemies", font, black, width//4, height//8)

        draw_button("Start Game", width//2.4, height//4, 200, 50, blue, red, start_game)
    
        for event in pg.event.get():
            if event.type == pg.QUIT:
                menu = False
        
        pg.display.update()
        clock.tick(15)

if __name__ == "__main__":
    main_menu()