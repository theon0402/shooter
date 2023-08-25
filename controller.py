# -*- coding: utf-8 -*-
import pygame

class Controller:
    def update(self):
        self.keys = pygame.key.get_pressed()
    
    def draw(self, screen):
        pass       
    
    def is_left_pressed(self):
        return self.keys[pygame.K_LEFT]
    
    def is_right_pressed(self):
        return self.keys[pygame.K_RIGHT]
    
    def is_space_pressed(self):
        return self.keys[pygame.K_SPACE]