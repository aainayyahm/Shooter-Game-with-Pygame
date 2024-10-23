#pygame
import pygame as pg

# print(pygame.__version__)
pg.init()

screen = pg.display.set_mode((800, 450))
pg.display.set_caption("My First Game")

# Tambahkan image
image = pg.image.load("/Users/aainayyahm/Documents/Kelas Game Development/image1.jpg")
image = pg.transform.scale(image, (800, 450))

# Menginisiasi ukuran rectangle
rect_x, rect_y = 400, 200
rect_height, rect_weight = 25, 15
rect_color = (255, 194, 111)
alt_color = (255, 0, 0)
current_color = rect_color
speed = 1  # kecepatan pergerakan dari objek
rectangle_draw = False  # untuk menandakan bahwa setelah running objek belum ada atau masih kosong

# Loop game
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Menerima input dari mouse
    mouse_x, mouse_y = pg.mouse.get_pos()  # Untuk mendapatkan posisi kursor mouse
    mouse_buttons = pg.mouse.get_pressed()  # Untuk mendeteksi klik dari mouse

    # Membuat kondisi jika tombol kiri ditekan maka akan muncul objek
    if mouse_buttons[0]:  # 0 itu left klik
        if not rectangle_draw:
            rect_x, rect_y = mouse_x - rect_weight // 2, mouse_y - rect_height // 2
            rectangle_draw = True
        else:
            # Untuk cek apakah posisi kursor kita berada dalam objek/rectangle
            if rect_x <= mouse_x <= rect_x + rect_weight and rect_y <= mouse_y <= rect_y + rect_height:
                current_color = alt_color if current_color == rect_color else rect_color

    # Membuat kondisi jika tombol keyboard atas dan bawah ditekan
    keys = pg.key.get_pressed()
    if rectangle_draw:  # Kondisi untuk cek apakah objek sudah tergambar
        if keys[pg.K_UP]:
            rect_y -= speed
        if keys[pg.K_DOWN]:
            rect_y += speed
        if keys[pg.K_LEFT]:
            rect_x -= speed
        if keys[pg.K_RIGHT]:
            rect_x += speed

    # Menampilkan background
    screen.blit(image, (0, 0))

    # Menampilkan objek
    if rectangle_draw:
        pg.draw.rect(screen, current_color, (rect_x, rect_y, rect_weight, rect_height))

    # Update image
    pg.display.flip()

pg.quit()


