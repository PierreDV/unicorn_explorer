import pygame

class UnicornDude():

    def __init__(self, screen):
        """Initialize the unicorn dude and set his starting position."""
        self.screen = screen

        # Load the unicorn dude and get his rect.
        # self.image = pygame.image.load('images/front_standing.bmp')
    

        self.front_walking_images = []

        self.front_walking_images.append(pygame.image.load('images/front_walking_1.bmp'))
        self.front_walking_images.append(pygame.image.load('images/front_walking_2.bmp'))
        self.front_walking_images.append(pygame.image.load('images/front_walking_3.bmp'))
        self.front_walking_images.append(pygame.image.load('images/front_walking_4.bmp'))
        self.front_walking_images.append(pygame.image.load('images/front_walking_5.bmp'))
        self.front_walking_images.append(pygame.image.load('images/front_walking_6.bmp'))
        
        self.counter = 0
        self.index = 0
        self.image = self.front_walking_images[self.index]
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
            self.counter += 1

            if self.counter == 60:
                self.counter = 0
                self.index += 1
   
            if self.index >= len(self.front_walking_images):
                self.index = 0
            self.image = self.front_walking_images[self.index]
            self.rect.centery += 1

    def blitme(self):
        """Draw the unicorn dude at his current location."""
        self.screen.blit(self.image, self.rect)