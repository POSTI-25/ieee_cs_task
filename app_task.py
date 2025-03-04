# Example file showing a basic pygame "game loop"
import pygame as pg

# pygame setup
pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True

# colors
background_color = (57 , 54 , 70)
panel_color = (79, 69, 87)
button_color = (109, 93, 110)
text_color = (244, 238, 224)
line_color = (255, 255, 255)

#fonts
fonts = pg.font.get_fonts()
base_font = pg.font.SysFont("aptosdisplay" , 30)

# icons
profile_icon = pg.image.load("profile.png").convert_alpha()
group_icon = pg.image.load("group.png").convert_alpha()
qr_icon = pg.image.load("qr.png").convert_alpha()
feedback_icon = pg.image.load("feedback.png").convert_alpha()
settings_icon = pg.image.load("settings.png").convert_alpha()
about_icon = pg.image.load("about.png").convert_alpha()
logout_icon = pg.image.load("logout.png").convert_alpha()

# Resize icons (optional)
profile_icon = pg.transform.scale(profile_icon, (20, 20))
group_icon = pg.transform.scale(group_icon, (20, 20))
qr_icon = pg.transform.scale(qr_icon, (20,20))
feedback_icon = pg.transform.scale(feedback_icon, (20,20))
settings_icon = pg.transform.scale(settings_icon, (20,20))
about_icon = pg.transform.scale(about_icon, (20,20))
logout_icon = pg.transform.scale(logout_icon, (20,20))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(background_color)

    # Drawing the left-side panel 
    panel_rect = pg.Rect(0, 0, screen.get_width()/4 , screen.get_height())  # (x, y, width, height)
    panel_line = pg.Rect(0 , screen.get_height()/2 , screen.get_width()/4 , 3)
    pg.draw.rect(screen, panel_color, panel_rect)
    pg.draw.rect(screen, line_color, panel_line)
    # RENDER YOUR GAME HERE

    # writing on panel
    profile = base_font.render("My Profile", True, text_color)
    groups = base_font.render("My Groups", True, text_color)
    join = base_font.render("Join group via QR code", True, text_color)
    feedback = base_font.render("Send Feedback", True, text_color)
    settings = base_font.render("Settings", True, text_color)
    about = base_font.render("About Us", True, text_color)
    logout = base_font.render("Logout", True, text_color)

    # Blit (draw) the text onto the screen at positions inside the panel
    screen.blit(profile, (screen.get_width()/16, screen.get_height()/4 + screen.get_height()/16))
    screen.blit(groups, (screen.get_width()/16, screen.get_height()/4 + screen.get_height()*2/16))
    screen.blit(join, (screen.get_width()/16, screen.get_height()/4 + screen.get_height()*3/16))
    screen.blit(feedback, (screen.get_width()/16, screen.get_height()/2 + screen.get_height()/16))
    screen.blit(settings, (screen.get_width()/16, screen.get_height()/2 + screen.get_height()*2/16))
    screen.blit(about, (screen.get_width()/16, screen.get_height()/2 + screen.get_height()*3/16))
    screen.blit(logout, (screen.get_width()/16, screen.get_height()/2 + screen.get_height()*4/16))

    # icons
    screen.blit(profile_icon, (20, screen.get_height()/4 + screen.get_height()/16))
    screen.blit(group_icon, (20, screen.get_height()/4 + screen.get_height()*2/16))
    screen.blit(qr_icon , (20, screen.get_height()/4 + screen.get_height()*3/16))
    screen.blit(feedback_icon , (20, screen.get_height()/2 + screen.get_height()/16))
    screen.blit(settings_icon , (20, screen.get_height()/2 + screen.get_height()*2/16))
    screen.blit(about_icon , (20, screen.get_height()/2 + screen.get_height()*3/16))
    screen.blit(logout_icon , (20, screen.get_height()/2 + screen.get_height()*4/16))

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()