# -*- coding: utf-8 -*-
import pygame

class Player:
    def __init__(self, screen_size):
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (screen_size[0]/2, screen_size[1]-40)
        self.lasers = []
    
    def get_lasers(self):
        return self.lasers
    
    def update(self, shooters, controller):
        if controller.is_left_pressed():
            self.rect.move_ip(-5, 0)
            
        if controller.is_right_pressed():
            self.rect.move_ip(5, 0)
            
        if controller.is_space_pressed():
            left = self.rect.centerx-1
            top = self.rect.centery-60
            width = 2
            height = 40
            self.lasers.append(pygame.Rect(left, top, width, height))
    
    def draw(self, screen):
        for laser in self.lasers:
            # update laser here
            laser.move_ip(0, -4)
            pygame.draw.rect(screen, (255,0,0), laser)
            
        screen.blit(self.image, self.rect)