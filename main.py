import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Start pygame
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialise the clock
    clock = pygame.time.Clock()
    
    # Set initial time since last frame.
    dt = 0

    # Create update groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Player is the name of the class, not an instance of it
    # This must be done before any Player objects are created
    Player.containers = (updatable, drawable) 
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Initalise the player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Initialise the asteroid field
    asteroid_field = AsteroidField()

    # Start the game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Black screen    
        screen.fill("black")

        # Calculate time since last frame
        dt = clock.tick(60) / 1000

        # Update
        updatable.update(dt)

        # Draw
        for obj in drawable:
            obj.draw(screen)
        
        # Update screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
