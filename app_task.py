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

#panel top profile
bg_grad = pg.image.load("images_and_icons/profile_grad.jpg").convert_alpha()
bg_grad = pg.transform.scale(bg_grad, (screen.get_width()/4, screen.get_height()/4))
profile_img = pg.image.load("images_and_icons/j_profile.png").convert_alpha()  
profile_img = pg.transform.scale(profile_img, (64, 64))

#fonts
fonts = pg.font.get_fonts()
title_font = pg.font.SysFont("arial" , 27, bold=True)
base_font = pg.font.SysFont("aptosdisplay" , 30)
small_font = pg.font.SysFont("aptosdisplay" , 25)

# icons
profile_icon = pg.image.load("images_and_icons/profile.png").convert_alpha()
group_icon = pg.image.load("images_and_icons/group.png").convert_alpha()
qr_icon = pg.image.load("images_and_icons/qr.png").convert_alpha()
feedback_icon = pg.image.load("images_and_icons/feedback.png").convert_alpha()
settings_icon = pg.image.load("images_and_icons/settings.png").convert_alpha()
about_icon = pg.image.load("images_and_icons/about.png").convert_alpha()
logout_icon = pg.image.load("images_and_icons/logout.png").convert_alpha()

# Resize icons (optional)
profile_icon = pg.transform.scale(profile_icon, (20, 20))
group_icon = pg.transform.scale(group_icon, (20, 20))
qr_icon = pg.transform.scale(qr_icon, (20,20))
feedback_icon = pg.transform.scale(feedback_icon, (20,20))
settings_icon = pg.transform.scale(settings_icon, (20,20))
about_icon = pg.transform.scale(about_icon, (20,20))
logout_icon = pg.transform.scale(logout_icon, (20,20))

# THE 4 SCREENS
expenses_illu = pg.image.load("images_and_icons/expense.png")
expenses_illu = pg.transform.scale(expenses_illu, (200 , 200))

balance_illu = pg.image.load("images_and_icons/balance.png")
balance_illu = pg.transform.scale(balance_illu, (200 , 200))

payment_illu = pg.image.load("images_and_icons/pay.png")
payment_illu = pg.transform.scale(payment_illu, (200 , 200))

new_grp = pg.image.load("images_and_icons/new_grp.png")
new_grp = pg.transform.scale(new_grp, (200 , 200))

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
    div_horizontal = pg.Rect(screen.get_width()/4 + screen.get_width()/64 ,  screen.get_height()/2 , screen.get_width()*3/4 - screen.get_width()/32, 3)
    div_vertical = pg.Rect(screen.get_width()/4 + screen.get_width()*3/8 ,  screen.get_height()/32 , 3, screen.get_height() - screen.get_height()/16)
    pg.draw.rect(screen, panel_color, panel_rect)
    pg.draw.rect(screen, line_color, panel_line)
    pg.draw.rect(screen, button_color, div_horizontal)
    pg.draw.rect(screen, button_color, div_vertical)

    # RENDER YOUR GAME HERE

    # writing on panel
    profile = base_font.render("My Profile", True, text_color)
    groups = base_font.render("My Groups", True, text_color)
    join = base_font.render("Join group via QR code", True, text_color)
    feedback = base_font.render("Send Feedback", True, text_color)
    settings = base_font.render("Settings", True, text_color)
    about = base_font.render("About Us", True, text_color)
    logout = base_font.render("Logout", True, text_color)
    username = title_font.render("User Name", True, text_color)
    email = small_font.render("user@example.com", True, text_color)

    # WRITING ON SCREENS
    add_expenses = title_font.render("ADD EXPENSES", True, text_color)
    view_balance = title_font.render("VIEW BALANCE", True, text_color)
    settle_payment = title_font.render("SETTLE PAYMENTS", True, text_color)
    create_grp = title_font.render("CREATE GROUP", True, text_color)

    # Blit (draw) the text onto the screen at positions inside the panel
    screen.blit(profile, (screen.get_width()/16, screen.get_height()/4 + screen.get_height()/16))
    screen.blit(groups, (screen.get_width()/16, screen.get_height()/4 + screen.get_height()*2/16))
    screen.blit(join, (screen.get_width()/16, screen.get_height()/4 + screen.get_height()*3/16))
    screen.blit(feedback, (screen.get_width()/16, screen.get_height()/2 + screen.get_height()/16))
    screen.blit(settings, (screen.get_width()/16, screen.get_height()/2 + screen.get_height()*2/16))
    screen.blit(about, (screen.get_width()/16, screen.get_height()/2 + screen.get_height()*3/16))
    screen.blit(logout, (screen.get_width()/16, screen.get_height()/2 + screen.get_height()*4/16))

    # Blit text for the 4 screens
    screen.blit(add_expenses, (screen.get_width()/4 + screen.get_width()*13/64, screen.get_height()/4))
    screen.blit(settle_payment, (screen.get_width()/4 + screen.get_width()*13/64, screen.get_height()*3/4))
    screen.blit(view_balance, (screen.get_width()/4 + screen.get_width()*37/64, screen.get_height()/4))
    screen.blit(create_grp, (screen.get_width()/4 + screen.get_width()*37/64, screen.get_height()*3/4))

    # icons
    screen.blit(profile_icon, (20, screen.get_height()/4 + screen.get_height()/16))
    screen.blit(group_icon, (20, screen.get_height()/4 + screen.get_height()*2/16))
    screen.blit(qr_icon , (20, screen.get_height()/4 + screen.get_height()*3/16))
    screen.blit(feedback_icon , (20, screen.get_height()/2 + screen.get_height()/16))
    screen.blit(settings_icon , (20, screen.get_height()/2 + screen.get_height()*2/16))
    screen.blit(about_icon , (20, screen.get_height()/2 + screen.get_height()*3/16))
    screen.blit(logout_icon , (20, screen.get_height()/2 + screen.get_height()*4/16))

    #panel top profile
    screen.blit(bg_grad , (0 , 0))
    screen.blit(profile_img, (screen.get_width()/64, screen.get_height()/32))

    screen.blit(username, (screen.get_width()/64 , screen.get_height()/8))
    screen.blit(email, (screen.get_width()/64, screen.get_height()/8 + screen.get_height()/16))

    # EXPENSES SCREEN
    screen.blit(expenses_illu, (screen.get_width()/4 + screen.get_width()/32, screen.get_height()/8))
    screen.blit(balance_illu, (screen.get_width()/4 + screen.get_width()*3/8 + screen.get_width()/32, screen.get_height()/8))
    screen.blit(payment_illu, (screen.get_width()/4 + screen.get_width()/32, screen.get_height()/2 + screen.get_height()/8))
    screen.blit(new_grp, (screen.get_width()/4 + screen.get_width()*3/8 + screen.get_width()/32, screen.get_height()/2 + screen.get_height()/8))
    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()