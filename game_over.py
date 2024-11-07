import pygame
import math

# Initialize Pygame
pygame.init()

def game_over_window(screen):
    # Set up the screen
    screen_width, screen_height = 1100, 650
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("game_over")

       # Create an instance of the Game class
    game = Game()


    # Load the button image
    game_over_image = pygame.image.load('C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/gameover.jpg')
    replay_button_image = pygame.image.load('C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/restart.png')
    exit_button_image = pygame.image.load('C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/exit_button.png')



    button_width, button_height = 150, 75
    replay_button_image = pygame.transform.scale(replay_button_image, (145, 65))
    exit_button_image = pygame.transform.scale(exit_button_image, (150, 75))

    # Get the rectangle of each button image
    replay_button_rect = replay_button_image.get_rect()
    exit_button_rect = exit_button_image.get_rect()


    # Set the positions of the buttons
    replay_button_rect.bottomleft = (screen_width // 3, screen_height - 50)
    exit_button_rect.bottomright = (2 * screen_width // 3, screen_height - 50)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click is within the replay button
                if replay_button_rect.collidepoint(event.pos):
                    print("Replay button clicked")
                    game.start()
                    running = False
                    
                # Check if the mouse click is within the exit button
                elif exit_button_rect.collidepoint(event.pos):
                    print("Exit button clicked")
                    running = False  # Close the game over window


        # Clear the screen
        screen.fill((0, 0, 0))

        # Blit the "Game Over" image
        screen.blit(game_over_image, (0, 0))

         # Blit the buttons
        screen.blit(replay_button_image, replay_button_rect)
        screen.blit(exit_button_image, exit_button_rect)


        pygame.display.flip()

pygame.quit()
