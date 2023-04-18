import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg") #Surface生成
    bg_img2 = pg.transform.flip(pg.image.load("ex01/fig/pg_bg.jpg"), True, False) #背景反転
    kk_img = pg.transform.flip(pg.image.load("ex01/fig/3.png"), True, False) #こうかとん生成
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 5, 1.0), pg.transform.rotozoom(kk_img, 10, 1.0), pg.transform.rotozoom(kk_img, 15, 1.0), pg.transform.rotozoom(kk_img, 10, 1.0), pg.transform.rotozoom(kk_img, 5, 1.0)] #こうかとんリスト


    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        x = tmr % 3200
        screen.blit(bg_img, [-x,0]) #背景1枚目
        screen.blit(bg_img2, [1600-x,0]) #背景2枚目
        screen.blit(bg_img, [3200-x,0]) #背景3枚目
        screen.blit(kk_imgs[int(tmr/10)%6], [300,200]) #こうかとん

        pg.display.update()
        clock.tick(100)
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()