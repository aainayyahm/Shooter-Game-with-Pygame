#pygame
import pygame as pg

# print(pygame.__version__)
pg.init()

screen = pg.display.set_mode((1600,900))
pg.display.set_caption("My First Game")

#Tambahkan image
image = pg.image.load("/Users/aainayyahm/Documents/Kelas Game Development/image1.jpg")
image = pg.transform.scale(image, (1600, 900))

#Loop game
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    #Buat white background
    screen.fill((255,255,255))

    #Menampilkan gambar
    screen.blit(image, (0,0))

    #Update image
    pg.display.flip()

pg.quit()



