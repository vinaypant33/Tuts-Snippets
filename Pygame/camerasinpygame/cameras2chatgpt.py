mport pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Camera Follows Player")

# Set up the clock
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN  ="Green"

# Define the player sprite
player_size = 50
player_x = screen_width / 2 - player_size / 2
player_y = screen_height / 2 - player_size / 2
player_speed = 5
player = pygame.Rect(player_x, player_y, player_size, player_size)
player2 = pygame.Rect(player_x, player_y, player_size, player_size)

# Define the camera
camera_x = 0
camera_y = 0

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed
    
    # Update the camera position to follow the player
    camera_x = -player.x + screen_width / 2 - player_size / 2
    camera_y = -player.y + screen_height / 2 - player_size / 2
    
    # Draw the background
    screen.fill(BLACK)
    
    # Draw the player and all other sprites with the camera offset
    pygame.draw.rect(screen, WHITE, player.move(camera_x, camera_y))
    pygame.draw.rect(screen, GREEN, player2.move(0, 0))

    
    # Update the screen
    pygame.display.update()
    
    # Tick the clock
    clock.tick(60)
