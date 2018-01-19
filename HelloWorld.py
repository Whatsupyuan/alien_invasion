# -*- coding: UTF-8 -*-

# 声明 导入pygame和sys模块，这样我们的程序才可以使用里面的方法
import pygame, sys

# 也是声明导入， 只是形式不同，导入所有 pygame.locals里的变量（比如下面大写的QUIT变量）
from pygame.locals import *
pygame.init()  # 初始化pygame

DISPLAYSURF = pygame.display.set_mode((400, 300))  # 设置窗口的大小单位为像素

pygame.display.set_caption('Hello World!')  # 设置窗口的标题

while True:  # 程序主循环

    for event in pygame.event.get():  # 获取事件

        if event.type == QUIT:  # 判断事件是否为退出事件

            pygame.quit()  # 退出pygame

            sys.exit()  # 退出系统

    pygame.display.update()  # 绘制屏幕内容
