import pygame as pg

# pygame setup
pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True

# Colors
background_color = (173, 216, 230)
panel_color = (50, 50, 50)
text_color = (255, 255, 255)

# Font setup
font = pg.font.SysFont(None, 36)  # (Font name, size)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Fill the background
    screen.fill(background_color)

    # Draw the left-side panel
    panel_rect = pg.Rect(0, 0, 300, 720)
    pg.draw.rect(screen, panel_color, panel_rect)

    # Add text to the panel
    name_text = font.render("Name: John Doe", True, text_color)
    details_text = font.render("Profile: Active", True, text_color)
    email_text = font.render("Email: john@example.com", True, text_color)

    # Blit (draw) the text onto the screen at positions inside the panel
    screen.blit(name_text, (20, 50))
    screen.blit(details_text, (20, 100))
    screen.blit(email_text, (20, 150))

    pg.display.flip()
    clock.tick(60)

pg.quit()




import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Font Example")

# Get available fonts and pick one
available_fonts = pygame.font.get_fonts()
print(f"Available fonts: {available_fonts}")

font_name = "bahnschrift"  # Make sure this is in the list
if font_name not in available_fonts:
    font_name = pygame.font.get_default_font()  # fallback if it's not available

font_size = 50
font = pygame.font.SysFont(font_name, font_size)

# Create a text surface
text_surface = font.render("Hello, Pygame!", True, (255, 255, 255))  # white text
text_rect = text_surface.get_rect(center=(320, 240))  # center the text

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # fill the screen with black
    screen.blit(text_surface, text_rect)  # draw the text
    pygame.display.flip()  # update the display

pygame.quit()
