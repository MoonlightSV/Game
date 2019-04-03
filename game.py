import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("VVV")

clock = pygame.time.Clock()

x = 50
y = 475
width = 10
height = 20
speed = 5

isJump = False
jumpCount = 10

demXD = True
demYL = False
demXU = False
demYR = False


def drawWindow():
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
    pygame.display.update()


run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and pygame.key.get_mods() & pygame.KMOD_CTRL:
                demXD = False
                demYL = False
                demXU = False
                demYR = True

                if width < height:
                    width, height = height, width

                while x < 500 - width - 5:
                    # clock.tick(60)
                    x += 1

                isJump = False
                jumpCount = 10

            if event.key == pygame.K_DOWN and pygame.key.get_mods() & pygame.KMOD_CTRL:
                demXD = True
                demYL = False
                demXU = False
                demYR = False

                if width > height:
                    width, height = height, width

                while y < 500 - height - 5:
                    # clock.tick(60)
                    y += 1

                isJump = False
                jumpCount = 10

            if event.key == pygame.K_UP and pygame.key.get_mods() & pygame.KMOD_CTRL:
                demXD = False
                demYL = False
                demXU = True
                demYR = False

                if width > height:
                    width, height = height, width

                while y > 5:
                    # clock.tick(60)
                    y -= 1

                isJump = False
                jumpCount = 10

            if event.key == pygame.K_LEFT and pygame.key.get_mods() & pygame.KMOD_CTRL:
                demXD = False
                demYL = True
                demXU = False
                demYR = False

                if width < height:
                    width, height = height, width

                while x > 5:
                    # clock.tick(60)
                    x -= 1

                isJump = False
                jumpCount = 10

    keys = pygame.key.get_pressed()
    if demXD or demXU:
        if keys[pygame.K_LEFT] and x > 5:
            x -= speed
            # left = True
            # right = False
        elif keys[pygame.K_RIGHT] and x < 500 - width - 5:
            x += speed
            # left = False
            # right = True
    elif demYL or demYR:
        if keys[pygame.K_UP] and y > 5:
            y -= speed
        elif keys[pygame.K_DOWN] and y < 500 - height - 5:
            y += speed


    # else:
        # left = False
        # right = False
        # animCount = 0

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if demXD:
                if jumpCount < 0:
                    y += (jumpCount ** 2) / 4  # теряем высоту
                else:
                    y -= (jumpCount ** 2) / 4  # набираем высоту
                jumpCount -= 1
            elif demYR:
                if jumpCount < 0:
                    x += (jumpCount ** 2) / 4  # теряем высоту
                else:
                    x -= (jumpCount ** 2) / 4  # набираем высоту
                jumpCount -= 1
            elif demXU:
                if jumpCount < 0:
                    y -= (jumpCount ** 2) / 4  # теряем высоту
                else:
                    y += (jumpCount ** 2) / 4  # набираем высоту
                jumpCount -= 1
            elif demYL:
                if jumpCount < 0:
                    x -= (jumpCount ** 2) / 4  # теряем высоту
                else:
                    x += (jumpCount ** 2) / 4  # набираем высоту
                jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    drawWindow()

pygame.quit()
