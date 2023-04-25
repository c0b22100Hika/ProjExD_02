import random
import sys

import pygame as pg

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    tmr = 0

    bomb_img = pg.Surface((20,20))  # ボムのイメージを作る四角を作る
    pg.draw.circle(bomb_img, (255, 0, 0), (10,10), 10)  # 作った四角の中のどこかに円を作る
    bomb_img.set_colorkey((0, 0, 0))  # 四角の黒い部分を透明化

    b_x = random.randint(0,1600) # ボムのｘ座標
    b_y = random.randint(0,900)  # ボムのｙ座標


    # イベントの処理
    while True:
        for event in pg.event.get():  # すべてのイベントについて
            if event.type == pg.QUIT:  # もしｘが押されたら
                return 0

        tmr += 1
        screen.blit(bg_img, [0, 0])  # 背景描画
        screen.blit(kk_img, [900, 400])  # こうかとんの描画

        
        screen.blit(bomb_img, [b_x, b_y])  # 爆弾の描画



        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()