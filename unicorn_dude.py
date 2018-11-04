import pygame

class UnicornDude():

    def __init__(self, ai_settings, screen):
        """Initialize the unicorn dude and set his starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the unicorn dude and get his rect.
        # self.image = pygame.image.load('images/front_standing.bmp')
    
        self.down_walking_images = []

        for x in range(1, 7):
            self.down_walking_images.append(
                pygame.image.load('images/unicorn_dude/down_walking/' + str(x) + '.bmp'))
                
        self.counter = 0
        self.index = 0
        self.image = self.down_walking_images[self.index]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start the unicorn dude in the center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flags
        self.moving_right = False 
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def animate_movement(self):
        self.counter += 1

        if self.counter == 60:
            self.counter = 0
            self.index += 1

        if self.index >= len(self.down_walking_images):
            self.index = 0
        self.image = self.down_walking_images[self.index]

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the unicorn dude's center value, not the rect.
        if self.moving_right:
            self.centerx += self.ai_settings.unicorn_dude_speed_factor
        
        if self.moving_left:
            self.centerx -= self.ai_settings.unicorn_dude_speed_factor
        
        if self.moving_up:
            self.centery -= self.ai_settings.unicorn_dude_speed_factor

        if self.moving_down:
            self.animate_movement()
            self.centery += self.ai_settings.unicorn_dude_speed_factor
        # Update rect object from self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

 

    def blitme(self):
        """Draw the unicorn dude at his current location."""
        self.screen.blit(self.image, self.rect)