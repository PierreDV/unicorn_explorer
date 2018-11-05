import pygame

class UnicornDude():

    # Upload all sprite animations into seperate groups of images based on direction.
    # Animate movement based on direction.
    # Fix animation speed of diagonal motion.

    def __init__(self, ai_settings, screen):
        """Initialize the unicorn dude and set his starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
 
        # Create image groups for animation sprites and upload images.
        self.down_walking_images = []
        self.load_images(self.down_walking_images, 'down')

        self.up_walking_images = []
        self.load_images(self.up_walking_images, 'up')

        self.left_walking_images = []
        self.load_images(self.left_walking_images, 'left')

        self.right_walking_images = []
        self.load_images(self.right_walking_images, 'right')

        self.up_right_walking_images = []
        self.load_images(self.up_right_walking_images, 'up_right')

        self.up_left_walking_images = []
        self.load_images(self.up_left_walking_images, 'up_left')

        self.down_right_walking_images = []
        self.load_images(self.down_right_walking_images, 'down_right')

        self.down_left_walking_images = []
        self.load_images(self.down_left_walking_images, 'down_left')

        # Load the unicorn dude and get his rect.
        self.image = pygame.image.load('images/unicorn_dude/standing/down.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Set counter for changing animation frame and index for animations within group.
        self.counter = 0
        self.index = 0

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

    def load_images(self, image_group, direction):
        for x in range(1, 7):
            image_group.append(
                pygame.image.load('images/unicorn_dude/' + direction + '_walking/' + str(x) + '.bmp'))

    def animate_movement(self, direction):
        if direction == 'down':
            self.image = self.down_walking_images[self.index]
        elif direction == 'up':
            self.image = self.up_walking_images[self.index]
        elif direction == 'left':
            self.image = self.left_walking_images[self.index]
        elif direction == 'right':
            self.image = self.right_walking_images[self.index]
        elif direction == 'down_right':
            self.image = self.down_right_walking_images[self.index]
        elif direction == 'down_left':
            self.image = self.down_left_walking_images[self.index]
        elif direction == 'up_right':
            self.image = self.up_right_walking_images[self.index]
        else:
            self.image = self.up_left_walking_images[self.index]

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the unicorn dude's center value, not the rect.
        if self.moving_down or self.moving_left or self.moving_right or self.moving_up:
            self.counter += 1
            if self.counter == 60:
                self.counter = 0
                self.index += 1

            if self.index >= len(self.down_walking_images):
                self.index = 0

        if self.moving_right:
            if self.moving_down:
                self.animate_movement('down_right')
            elif self.moving_up:
                self.animate_movement('up_right')
            else:
                self.animate_movement('right')

            self.centerx += self.ai_settings.unicorn_dude_speed_factor
        
        if self.moving_left:
            if self.moving_down:
                self.animate_movement('down_left')
            elif self.moving_up:
                self.animate_movement('up_left')
            else:
                self.animate_movement('left')

            self.centerx -= self.ai_settings.unicorn_dude_speed_factor
        
        if self.moving_up:
            if self.moving_left:
                self.animate_movement('up_left')
            elif self.moving_right:
                self.animate_movement('up_right')
            else:
                self.animate_movement('up')

            self.centery -= self.ai_settings.unicorn_dude_speed_factor

        if self.moving_down:
            if self.moving_left:
                self.animate_movement('down_left')
            elif self.moving_right:
                self.animate_movement('down_right')
            else:
                self.animate_movement('down')
                
            self.centery += self.ai_settings.unicorn_dude_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Draw the unicorn dude at his current location."""
        self.screen.blit(self.image, self.rect)