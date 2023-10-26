# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, 'BLUE', (250, 250), 75)

    line_color = (0, 0, 0)
    start_point = (500, 0)
    end_point = (0, 500)
    line_width = 5

    # Draw a line
    pygame.draw.line(screen, line_color, start_point, end_point, line_width)

    #challenge question
    pygame.draw.line(screen, line_color, (500, 500), (0, 0), line_width)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
