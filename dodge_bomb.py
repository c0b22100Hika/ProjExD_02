import random
import sys

import pygame as pg


delta = { # keyのイベントを名前にして、辞書のキーにする
        pg.K_UP:(0, -1),
        pg.K_DOWN:(0, 1),
        pg.K_LEFT:(-1, 0),
        pg.K_RIGHT:(1, 0),
        }
timer = 0


def check_bound(scr_rct: pg.Rect, obj_rct: pg.Rect) -> tuple[bool, bool]:
    """
    オブジェクトが画面内or画面外かを判定　真理値タプルを返す関数
    引数１：画面SurfaceのRect
    引数２：こうかとんor爆弾のSurfaceのRect
    """

    yoko, tate = True, True

    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = False
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = False

    return yoko, tate



def main():
    # 以下こうかとんについて
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = (900, 400)
    game_over_img = pg.image.load("ex02/fig/8.png")
    game_over_img = pg.transform.rotozoom(game_over_img, 0, 2.0)
    game_rect = game_over_img.get_rect()
    

    # 以下爆弾について
    bomb_img = pg.Surface((20,20))  # ボムのイメージを作る四角を作る
    pg.draw.circle(bomb_img, (255, 0, 0), (10,10), 10)  # 作った四角の中のどこかに円を作る
    bomb_img.set_colorkey((0, 0, 0))  # 四角の黒い部分を透明化
    b_x = random.randint(0,1600) # ボムのｘ座標
    b_y = random.randint(0,900)  # ボムのｙ座標

    fonto  = pg.font.Font(None, 80)

    game_flag = False # ゲームの処理のためにフラグを作成
    
    
    accs = [a for a in range(1, 11)]

    bomb_imgs = []
    bomb_rcts = []
    for r in range(1, 11):
        bomb_img = pg.Surface((20*r, 20*r))
        pg.draw.circle(bomb_img, (255, 0, 0), (10*r, 10*r), 10*r)
        bomb_imgs.append(bomb_img)
        bomb_rcts.append(bomb_img.get_rect)
    
    vx, vy = 1, 1
    avx, avy = 1, 1
    bomb_rct = bomb_img.get_rect()  # 爆弾の画像をそのまま使うのでなく、新しく四角を作って動かす
    bomb_rct.center = b_x, b_y  # 爆弾の中心の位置  

    tmr = 0

    # イベントの処理
    while True:
        for event in pg.event.get():  # すべてのイベントについて
            if event.type == pg.QUIT:  # もしｘが押されたら
                return 0

        tmr += 1


        # 以下、key入力を確認し、keyに応じて写真を変更する
        key_list = pg.key.get_pressed()
        if key_list[pg.K_UP] == True and key_list[pg.K_DOWN] == False and key_list[pg.K_RIGHT] == False and key_list[pg.K_LEFT] == False :
            kk_img = pg.image.load("ex02/fig/3.png")
            kk_img = pg.transform.flip(kk_img, True, False)
            kk_img = pg.transform.rotozoom(kk_img,90,2.0)
        elif key_list[pg.K_UP] == True and key_list[pg.K_DOWN] == False and key_list[pg.K_RIGHT] == True and key_list[pg.K_LEFT] == False :
            kk_img = pg.image.load("ex02/fig/3.png")
            kk_img = pg.transform.flip(kk_img, True, False)
            kk_img = pg.transform.rotozoom(kk_img,45,2.0)
        elif key_list[pg.K_UP] == False and key_list[pg.K_DOWN] == False and key_list[pg.K_RIGHT] == True and key_list[pg.K_LEFT] == False :
            kk_img = pg.image.load("ex02/fig/3.png")
            kk_img = pg.transform.flip(kk_img, True, False)
            kk_img = pg.transform.rotozoom(kk_img,0,2.0)
        elif key_list[pg.K_UP] == False and key_list[pg.K_DOWN] == True and key_list[pg.K_RIGHT] == True and key_list[pg.K_LEFT] == False :
            kk_img = pg.image.load("ex02/fig/3.png")
            kk_img = pg.transform.flip(kk_img, True, False)
            kk_img = pg.transform.rotozoom(kk_img,-45,2.0)
        elif key_list[pg.K_UP] == False and key_list[pg.K_DOWN] == True and key_list[pg.K_RIGHT] == False and key_list[pg.K_LEFT] == False :
            kk_img = pg.image.load("ex02/fig/3.png")
            kk_img = pg.transform.flip(kk_img, True, False)
            kk_img = pg.transform.rotozoom(kk_img,-90,2.0)
        elif key_list[pg.K_UP] == False and key_list[pg.K_DOWN] == True and key_list[pg.K_RIGHT] == False and key_list[pg.K_LEFT] == True :
            kk_img = pg.image.load("ex02/fig/3.png")
            kk_img = pg.transform.rotozoom(kk_img,45,2.0)
        elif key_list[pg.K_UP] == False and key_list[pg.K_DOWN] == False and key_list[pg.K_RIGHT] == False and key_list[pg.K_LEFT] == True :
            kk_img = pg.image.load("ex02/fig/3.png")
            kk_img = pg.transform.rotozoom(kk_img,0,2.0)
        elif key_list[pg.K_UP] == True and key_list[pg.K_DOWN] == False and key_list[pg.K_RIGHT] == True and key_list[pg.K_LEFT] == False :
            kk_img = pg.image.load("ex02/fig/3.png")
            kk_img = pg.transform.flip(kk_img, True, False)
            kk_img = pg.transform.rotozoom(kk_img,-45,2.0)
            

        for k, mv in delta.items():
            if key_list[k]:
                kk_rct.move_ip(mv)  #こうかとんの場所を変化させる
        if check_bound(screen.get_rect(), kk_rct) != (True,True):
            for k, mv in delta.items():
                if key_list[k]:
                    kk_rct.move_ip(-mv[0], -mv[1])  #こうかとんの場所を変化させる
        
        
        

        screen.blit(bg_img, [0, 0])  # 背景描画
        screen.blit(kk_img, kk_rct)  # こうかとんの描画
        
        yoko, tate = check_bound(screen.get_rect(), bomb_rct)

        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1

        
        avx, avy = vx*accs[min(tmr//1000, 9)], vy*accs[min(tmr//1000, 9)]
        bomb_img = bomb_imgs[min(tmr//1000, 9)]
        
        bomb_rct.move_ip(avx, avy)  # 爆弾の場所を変化させる
        screen.blit(bomb_img, bomb_rct)  # 爆弾の描画
        bomb_img.set_colorkey((0, 0, 0))

        
        
        if kk_rct.colliderect(bomb_rct):  # オブジェクトの重なりを確認
            print()
            kk_img = game_over_img
            bomb_rct.center = 10,10
            
            vx, vy = 0,0
            game_flag = True
            
            
            #return 0
        if game_flag == False:
            timer = tmr
            txt = fonto.render(str(tmr/1000), True, (255, 0, 0))  # 時間を表示させる
            screen.blit(txt, [10, 10])
        
        txt = fonto.render(str(timer/1000), True, (255, 0, 0))
        screen.blit(txt, [10, 10])  # 最終時間を表示させる
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()