import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_hanten =pg.transform.flip(bg_img,True,False)
    bg_img_3 = pg.image.load("fig/pg_bg.jpg")
    koukaton_3 = pg.image.load("fig/3.png")
    koukaton_3=pg.transform.flip(koukaton_3,True,False)
    kou_3_rect = koukaton_3.get_rect()#こうかとんレクとの取得
    kou_3_rect.center = 300,200#中心座標を設定
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_list = pg.key.get_pressed()
        if key_list[pg.K_UP]:#上矢印キーを取得
            kou_3_rect.move_ip((0,-1))#上に移動
        if key_list[pg.K_DOWN]:#下矢印キーを取得
            kou_3_rect.move_ip((0,+1))#下に移動
        if key_list[pg.K_RIGHT]:#右矢印キーを取得
            kou_3_rect.move_ip((+1,0))#右に移動
        if key_list[pg.K_LEFT]:#左矢印キーを取得
            kou_3_rect.move_ip((-1,0)) # 左に移動
        x= tmr%3200 #練習９余りが3199より上にはならない
        #画面surfaceに張り付けている
        screen.blit(bg_img, [-x,0])#練習5背景画像が動く
        screen.blit(bg_img_hanten,[-x+1600,0])#練習７、８背景に背景をついかする,不自然に追加されないようにする
        screen.blit(bg_img_3,[-x+3200,0])
        screen.blit(koukaton_3,kou_3_rect)#練習4こうかとんを描画
        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習6fps200


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()