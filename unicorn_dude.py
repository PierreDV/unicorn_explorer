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

        # Movement flags
        self.moving_right = False 
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.centerx += 1
        
        if self.moving_left:
            self.rect.centerx -= 1
        
        if self.moving_up:
            self.rect.centery -= 1

        if self.moving_down:
            self.rect.centery += 1

    def blitme(self):
        """Draw the unicorn dude at his current location."""
        self.screen.blit(self.image, self.rect)