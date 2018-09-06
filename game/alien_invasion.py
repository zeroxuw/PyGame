#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zerowin
# @Time    : 2018/9/5

import sys
import pygame
from game.settings import Settings
from game.ship import Ship
import game.game_functions as gf
from pygame.sprite import Group
from game.button import Button
from game.alien import Alien


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    # screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alian Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 设置背景颜色
    bg_color = (85, 204, 220)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    aliens = Group()


    # 创建一个外星人
    alien = Alien(ai_settings, screen)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, play_button, ship, bullets)
        ship.update()
        # bullets.update()

        # 删除已消失的子弹
        # for bullet in bullets.copy():
        #     if bullet.rect.bottom <= 0:
        #         bullet.remove(bullet)
        print(len(bullets))
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets, play_button)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        # 创建外星人群
        gf.create_fleet(ai_settings, screen, ship, aliens)

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exeit()

        # 每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        # screen.fill(bg_color)
        ship.blitme()
        # 让最终绘制的屏幕可见
        pygame.display.flip()


run_game()
