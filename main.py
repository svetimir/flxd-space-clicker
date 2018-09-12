# -*- coding: utf-8 -*-

# AUTHOR: fluxoid, ifi@yandex.ru
# VERSION: 0.0.2
# STARTED: 12.09.2018
# LATEST FILE REVISION: 12.09.2018
# PURPOSE: Project "space clicker" main file
# DESCRIPTION: Space clicker project main file

# by clicking the star
# you get star beams :)

import pygame
from pygame.locals import *

appversion="v0.0.2"

class Game(object):
    def __init__(self):
        self._running=True
        self.screen=None
        self.size=self.weight,self.height=640,480
        self.points=0

    def on_init(self):
        pygame.init()
        self.screen=pygame.display.set_mode(self.size)
        pygame.display.set_caption("SPACE CLICKER "+appversion)
        pygame.draw.circle(self.screen,pygame.color.THECOLORS["yellow"],(320,240),200)
        pygame.display.update()
        self._running=True

    def on_event(self,event):
        if event.type==pygame.QUIT:
            self._running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            self.points+=1
        pygame.display.update()

    def on_loop(self):
        pass

    def on_render(self):
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init()==False:
            self._running=False
        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

def main():
    g=Game()
    g.on_execute()

if __name__=="__main__":
    main()
