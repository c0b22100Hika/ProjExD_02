import pygame as pg
import sys

def main():
    level: int = 51
    print(level)

    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    tmr = 0

    
    bb_img = pg.Surface((500,500))
    pg.draw.circle(bb_img,(255,0,0),(250,250),250)
    bb_img.set_colorkey((0, 0, 0))


    print(main.__doc__)

    #イベントの処理
    while True:
        for event in pg.event.get():    #すべてのイベントについて
            if event.type == pg.QUIT:   #もしｘが押されたら
                return 0

        """
        tmr += 1
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        """
        

        screen.blit(bb_img, (1000,500))





        pg.display.update()
        clock.tick(1000)




if __name__ == "__main__":
    
    pg.init()
    main()
    pg.quit()
    sys.exit()