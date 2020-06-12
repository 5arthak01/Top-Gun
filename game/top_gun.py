import pygame
import random


class stobs:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wd = 50
        self.ht = 50
        self.plimg = pygame.image.load('./images/cone.jpeg')
        self.plimg = pygame.transform.scale(
            self.plimg, (self.wd, self.ht))
        self.surf = pygame.Surface((self.wd, self.ht))
        self.rect = self.surf.get_rect()

    def posn(self):
        self.rect = self.rect.move((self.x, self.y))


class mvobs:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # image attributes
        self.vel = 5
        self.imgwd = 70
        self.imght = 70
        self.width = 50
        self.height = 50
        self.plimg = pygame.image.load('./images/cloud.jpg')
        self.plimg = pygame.transform.scale(
            self.plimg, (self.imgwd, self.imght))
        self.surf = pygame.Surface((self.width, self.height))
        self.rect = self.surf.get_rect()
        # now intitial position
        self.rect.move_ip((self.x, self.y))
        self.move()

    def move(self):
        self.rx = self.rect.left
        if self.rx < winx - self.vel:
            self.rx = self.vel
        else:
            self.rx = -1 * (self.rect.width + winx)
        self.rect = self.rect.move((self.rx, 0))


class PlayerDude:

    def __init__(self):
        """characteristics of the player"""
        self.score = 0
        self.lvl = 1
        self.vel = 5
        self.imgwd = 50
        self.imght = 50
        self.width = 50
        self.height = 50
        self.plimg = pygame.image.load('./images/plane.png')
        self.plimg = pygame.transform.scale(
            self.plimg, (self.imgwd, self.imght))
        self.surf = pygame.Surface((self.width, self.height))
        self.rect = self.surf.get_rect()
        """characteristics end"""
        self.anoy = (pheight - self.rect.height)/2
        self.rect = self.rect.move(
            ((winx - self.rect.width)/2, winy - self.anoy - self.rect.height))

    def update(self, keys):
        self.x = 0
        self.y = 0
        self.rx = self.rect.top
        self.ry = self.rect.left
        if keys[pygame.K_LEFT] and self.rect.left > self.vel:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.rect.right < winx - self.vel:
            self.x += self.vel
        if keys[pygame.K_UP] and self.rect.top > self.vel:
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.rect.bottom < winy - self.vel:
            self.y += self.vel
        self.rect = self.rect.move((self.x, self.y))
        pygame.display.update()


class PlayerMood:

    def __init__(self):
        """characteristics of the player"""
        self.score = 0
        self.lvl = 1
        self.vel = 5
        self.imgwd = 50
        self.imght = 50
        self.width = 50
        self.height = 50
        self.plimg = pygame.image.load('./images/plane.png')
        self.plimg = pygame.transform.scale(
            self.plimg, (self.imgwd, self.imght))
        self.surf = pygame.Surface((self.width, self.height))
        self.rect = self.surf.get_rect()
        """characteristics end"""
        self.rect = self.rect.move(
            ((winx - self.rect.width)/2, (pheight - self.rect.height)/2))

    def update(self, keys):
        self.x = 0
        self.y = 0
        self.rx = self.rect.top
        self.ry = self.rect.left
        if keys[pygame.K_a] and self.rect.left > self.vel:
            self.x -= self.vel
        if keys[pygame.K_d] and self.rect.right < winx - self.vel:
            self.x += self.vel
        if keys[pygame.K_w] and self.rect.top > self.vel:
            self.y -= self.vel
        if keys[pygame.K_s] and self.rect.bottom < winy - self.vel:
            self.y += self.vel
        self.rect = self.rect.move((self.x, self.y))


pygame.init()
winx = 1000
winy = 1000
win = pygame.display.set_mode((winx, winy))
pygame.display.set_caption("Top Gun")
clock = pygame.time.Clock()
pwidth = winx
pheight = winy/9
pnum = 5
player = PlayerDude()
player2 = PlayerMood()
mystobs = []
mymvobs = []
flag = 0
somevar = 0
somevar2 = 0
# for i in range(5):
#     temp = stobs()
#     temp.posn()
#     mystobs.append(temp)
#     temp = mvobs()
#     mymvobs.append(temp)
# self.y = self.r1 + self.r2 * self.r3 * 2
# self.x = random.randint(0, winx - self.wd)

r3 = int(pheight)
r1 = random.randint(0, r3 - 50)
r2 = random.randint(1, pnum - 2)
k = (r3 - 50)/2
# 1
t = k + r3*2
temp = stobs(30, t)
temp.posn()
mystobs.append(temp)
# 2
t = k + r3*2
temp = stobs(30 + winx//3, t)
temp.posn()
mystobs.append(temp)
# 3
t = k + r3*2
temp = stobs(30 + 2*(winx//3), t)
temp.posn()
mystobs.append(temp)
# 4
t = k + r3*4
temp = stobs(70, t)
temp.posn()
mystobs.append(temp)
# 5
t = k + r3*4
temp = stobs(70 + (winx//2), t)
temp.posn()
mystobs.append(temp)
# 6
t = k + r3*6
temp = stobs((winx//3) + 20, t)
temp.posn()
mystobs.append(temp)

# 1
t = k + r3
temp = mvobs((2 * (winx//3)) - 10, t)
mymvobs.append(temp)
# 2
t = k + r3
temp = mvobs((winx//3) - 40, t)
mymvobs.append(temp)
# 3
t = k + r3*3
temp = mvobs((winx//3) - 40 + 20, t)
mymvobs.append(temp)
# 4
t = k + r3*3
temp = mvobs(((winx//3) * 2) + 20, t)
mymvobs.append(temp)
# 5
t = k + r3*5
temp = mvobs((winx//2) + 20, t)
mymvobs.append(temp)
# 6
t = k + r3*7
temp = mvobs(((winx//3) * 2) + 20, t)
mymvobs.append(temp)


def mkpartn(q):  # to make partitions

    # partitions dimensions
    px = 0
    py = pheight * q * 2
    pvel = 0
    # end
    pygame.draw.rect(win, (102, 179, 255), (px, py, pwidth, pheight))


def dispwin():
    win.fill((0, 0, 255))
    for i in range(pnum):
        mkpartn(i)
    for ob in mystobs:
        win.blit(ob.plimg, ob.rect)
    for ob1 in mymvobs:
        ob1.move()
        win.blit(ob1.plimg, ob1.rect)
    if(flag == 0):
        text = font.render('Score: ' + str(player.score), 1, (0, 0, 0))
        lvl = font.render('Level: ' + str(levellist[0]), 1, (0, 0, 0))
        win.blit(text, (0, 0))
        win.blit(lvl, (winx-180, 0))
    if(flag == 1):
        text = font.render('Score: ' + str(player2.score), 1, (0, 0, 0))
        lvl = font.render('Level: ' + str(levellist[1]), 1, (0, 0, 0))
        win.blit(text, (winx - 180, 0))
        win.blit(lvl, (0, 0))
    if(flag == 0):
        win.blit(player.plimg, player.rect)
    if(flag == 1):
        win.blit(player2.plimg, player2.rect)
    pygame.display.update()


def playerswitch(i):
    global flag
    if(flag == 0):
        tempx = player.rect.left
        tempy = player.rect.top
        gayx = (winx - player.rect.width)/2
        gayy = winy - player.anoy - player.rect.height
        player.rect = player.rect.move(
            (gayx - tempx, gayy - tempy))
        for i in scorelist[0]:
            i = 0
    if(flag == 1):
        tempx = player2.rect.left
        tempy = player2.rect.top
        gayx = (winx - player2.rect.width)/2
        gayy = (pheight - player2.rect.height)/2
        player2.rect = player2.rect.move(
            (gayx - tempx, gayy - tempy))
        print(flag)
        for i in scorelist[1]:
            i = 0
    i = True
    return i


font = pygame.font.SysFont('comicsans', 30)

scorelist = []
scorelist.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
scorelist.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

levellist = [1, 1]


def scoring():
    if(player.rect.bottom <= r3*7 and scorelist[0][0] == 0):
        player.score += 10
        scorelist[0][0] = 1
    if(player.rect.bottom <= r3*5 and scorelist[0][1] == 0):
        player.score += 10
        scorelist[0][1] = 1
    if(player.rect.bottom <= r3*3 and scorelist[0][2] == 0):
        player.score += 20
        scorelist[0][2] = 1
    if(player.rect.bottom <= r3 and scorelist[0][4] == 0):
        player.score += 20
        scorelist[0][4] = 1
    if(player.rect.bottom <= r3*6 and scorelist[0][5] == 0):
        player.score += 5
        scorelist[0][5] = 1
    if(player.rect.bottom <= r3*4 and scorelist[0][6] == 0):
        player.score += 10
        scorelist[0][6] = 1
    if(player.rect.bottom <= r3*2 and scorelist[0][7] == 0):
        player.score += 15
        scorelist[0][7] = 1
    pygame.display.update()


def scoring2():
    if(player2.rect.bottom >= r3*8 and scorelist[1][0] == 0):
        player2.score += 10
        scorelist[1][0] = 1
    if(player2.rect.bottom >= r3*6 and scorelist[1][1] == 0):
        player2.score += 10
        scorelist[1][1] = 1
    if(player2.rect.bottom >= r3*4 and scorelist[1][2] == 0):
        player2.score += 20
        scorelist[1][2] = 1
    if(player2.rect.bottom >= r3*2 and scorelist[1][4] == 0):
        player2.score += 20
        scorelist[1][4] = 1
    if(player2.rect.bottom >= r3*7 and scorelist[1][5] == 0):
        player2.score += 5
        scorelist[1][5] = 1
    if(player2.rect.bottom >= r3*5 and scorelist[1][6] == 0):
        player2.score += 10
        scorelist[1][6] = 1
    if(player2.rect.bottom >= r3*3 and scorelist[1][7] == 0):
        player2.score += 15
        scorelist[1][7] = 1
    pygame.display.update()


def result():
    pygame.display.quit()
    pygame.time.delay(100)
    winx = 1000
    winy = 1000
    win = pygame.display.set_mode((winx, winy))
    pygame.display.set_caption("Top Gun")
    win.fill((255, 255, 255))
    font1 = pygame.font.SysFont('comicsans', 60)
    text = font1.render('Player1: ' + str(player.score), 1, (0, 0, 0))
    text2 = font1.render('Player2: ' + str(player2.score), 1, (0, 0, 0))
    win.blit(text, (winx//2, winy//3))
    win.blit(text2, (winx//2, (2 * winy//3)))


run = True
while run:
    dispwin()
    clock.tick(30)
    stnum = player.lvl
    keys = pygame.key.get_pressed()
    player.update(keys)
    player2.update(keys)

    for i in mystobs:
        if pygame.sprite.collide_rect(player, i) == True:
            run = playerswitch(run)
            flag = (flag + 1) % 2

    for i in mymvobs:
        if pygame.sprite.collide_rect(player, i) == True:
            run = playerswitch(run)
            flag = (flag + 1) % 2

    scoring()
    if(player.rect.bottom <= r3*7 and somevar == 0):
        blah = pygame.time.get_ticks()
        somevar = 1
    if(player.rect.bottom <= r3):
        player.score -= (pygame.time.get_ticks() - blah)//1000
        run = playerswitch(run)
        flag = (flag + 1) % 2
        levellist[0] = levellist[0] + 1

    for i in mystobs:
        if pygame.sprite.collide_rect(player2, i) == True:
            result()

    for i in mymvobs:
        if pygame.sprite.collide_rect(player2, i) == True:
            result()

    scoring2()

    if(player2.rect.bottom >= r3 and somevar2 == 0):
        blah2 = pygame.time.get_ticks()
        somevar2 = 1
    if(player2.rect.bottom >= r3*8):
        player2.score -= (pygame.time.get_ticks() - blah2)//1000
        run = playerswitch(run)
        flag = (flag + 1) % 2
        levellist[1] = levellist[1] + 1
        for i in mymvobs:
            i.vel += 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
