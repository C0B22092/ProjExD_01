import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg") #Surface生成
    kk_img = pg.image.load("ex01/fig/3.png") #こうかとん生成
    kk_img = pg.transform.flip(kk_img, True, False) #左右反転
    kk_img = pg.transform.rotozoom(kk_img, 10, 1.0) #10度反時計回りに回転



    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        screen.blit(bg_img, [0, 0])

        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()