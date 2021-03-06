import pygame

class Ship():
    '''A model of a ship for sideway shooter'''
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        #Load ship image and get rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Load ship to screen
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        #store a decimal value for ship's center
        self.center = float(self.rect.centery)

        #Movement flag
        self.moving_up = False
        self.moving_down = False

    def update_position(self):
        '''Updates ship's position based on movement flag'''
        if self.moving_up and self.rect.top > 0:
            self.center -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.settings.ship_speed

        self.rect.centery = self.center

    def blitme(self):
        '''Draw the ship at current location'''
        self.screen.blit(self.image, self.rect)