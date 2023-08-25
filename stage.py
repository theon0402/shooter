# -*- coding: utf-8 -*-
import pygame

import controller
import player
import shooter

class Stage:
    def __init__(self):
        pygame.init()

        # title
        pygame.display.set_caption('Shooting Game')

        # clock
        self.clock = pygame.time.Clock()

        # screen
        self.screen_size = (800, 600)
        self.screen = pygame.display.set_mode(self.screen_size)
        
        # main objects
        self.controller = controller.Controller()
        self.player = player.Player(self.screen_size)
        self.shooters = []
        
    def run(self):
        # checking quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
        # reset screen
        self.screen.fill((0, 0, 0))
        
        # main objects update
        self.controller.update()        
        if len(self.shooters) == 0:
            self.shooters.append(shooter.Shooter(self.screen_size))
        updated_shooters = []
        for candidate_shooter in self.shooters:
            if not candidate_shooter.is_died():
                candidate_shooter.update(self.player)
                updated_shooters.append(candidate_shooter)
        self.shooters = updated_shooters
        self.player.update(self.shooters, self.controller)
        
        # main object draw
        for candidate_shooter in self.shooters:
            candidate_shooter.draw(self.screen)
        self.player.draw(self.screen)
        self.controller.draw(self.screen)
        
        
        # flip
        pygame.display.flip()
        return True
    
    def tick(self):
        self.clock.tick(60)
    
    def halt(self):
        pygame.quit()