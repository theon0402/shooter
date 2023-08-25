# -*- coding: utf-8 -*-
import pygame

class Shooter:
    def __init__(self, screen_size):
        self.image = pygame.image.load("shooter.png")
        self.rect = self.image.get_rect()
        self.rect.center = (screen_size[0]/2, 60)
    
    def is_died(self):
        return False
    
    def update(self, player):
        lasers = player.get_lasers()
        for laser_rect in lasers:
            if laser_rect.colliderect(self.rect):
                self.image.set_alpha(64)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)