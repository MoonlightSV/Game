import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("VVV")

'''walkRight = [pygame.image.load('right_1.png'),
             pygame.image.load('right_2.png'),
             pygame.image.load('right_3.png'),
             pygame.image.load('right_4.png')]

walkLeft = [pygame.image.load('left_1.png'),
            pygame.image.load('left_2.png'),
            pygame.image.load('left_3.png'),
            pygame.image.load('left_4.png')]'''

# bg = pygame.image.load('bg.jpg')
# playerStand = pygame.image.load('idle.png')

clock = pygame.time.Clock()

x = 50
y = 435
width = 40
height = 60
speed = 5

isJump = False
jumpCount = 10

demX = True
demY = False

# left = False
# right = False
# animCount = 0


'''def animMove(i):
    global width
    global height
    global x
    global y
    if i == 0:
        height = 40
        y = 445
    elif i == 1:
        height = 60
        y = 435'''


def drawWindow():
    global animCount

    # win.blit(bg, (0, 0))
    win.fill((0, 0, 0))

    '''if animCount + 1 >= 30:
        animCount = 0

    if left:
        # win.blit(walkLeft[animCount // 8], (x, y))
        animMove(animCount // 15)
        animCount += 1
    elif right:
        # win.blit(walkRight[animCount // 8], (x, y))
        animMove(animCount // 15)
        animCount += 1'''
    # else:
        # win.blit(playerStand, (x, y))

    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))

    pygame.display.update()


run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if demX:
        if keys[pygame.K_LEFT] and x > 5:
            x -= speed
            # left = True
            # right = False
        elif keys[pygame.K_RIGHT] and x < 500 - width - 5:
            x += speed
            # left = False
            # right = True
    elif demY:
        if keys[pygame.K_UP] and y > 5:
            y -= speed
        elif keys[pygame.K_DOWN] and y < 500 - height - 5:
            y += speed

    if keys[pygame.K_PAGEUP]:
        if demX:
            demX = False
            demY = True
        else:
            demX = True
            demY = False
    # else:
        # left = False
        # right = False
        # animCount = 0

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 4
            else:
                y -= (jumpCount ** 2) / 4
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    drawWindow()

pygame.quit()
