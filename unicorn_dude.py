import pygame

class UnicornDude():

    def __init__(self, screen):
        """Initialize the unicorn dude and set his starting position."""
        self.screen = screen

        # Load the unicorn dude and get his rect.
        self.image = pygame.image.load('images/unicorn_dude_front_standing.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start the unicorn dude in the center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """Draw the unicorn dude at his current location."""
        self.screen.blit(self.image, self.rect)