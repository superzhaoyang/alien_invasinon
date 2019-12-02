import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
import game_functions as gf
from game_stats import GameStats
from button import Button
def run_game():
    #初始化游戏兵并建立一个屏幕对象
    #初始化pygame，设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建play按钮
    play_button = Button(ai_settings,screen,"play")


    #创建一艘飞船,创建一个用于存储子弹的编组和外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #设置背景色
    bg_color = (230,230,230)
    #创建一个外星人
    alien = Alien(ai_settings,screen)
    #创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    file = r'music\1.mp3'
    # 初始化
    pygame.mixer.init()
    # 加载音乐文件
    track = pygame.mixer.music.load(file)
    # 开始播放音乐流
    pygame.mixer.music.play()

    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets)

        if stats.game_active:

            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)

        gf.update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button)

run_game()




