import math
import pygame
import random

screen_width = 800
screen_height = 900
player_startx = 370
player_starty = 380
enemy_starty_min = 50
enemy_starty_max = 150
enemy_speedx = 4
enemy_speedy = 40
bullet_speedy = 10
collision_distance = 27

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("background.png")

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# player
playerimg = pygame.image.load("player.png")
playerX = player_startx
playerY = player_starty
playerX_change = 0

# enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemynum = 6

for i in range(enemynum):
    enemyimg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, screen_width - 64)) # 64 is the size of the enemy
    enemyY.append(random.randint(enemy_starty_min, enemy_starty_max))
    enemyX_change.append(enemy_speedx)
    enemyY_change.append(enemy_speedy)

# bullet
bulletimg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = player_starty
bulletX_change = 0
bulletY_change = bullet_speedy
bulletstate = "ready"

# score
scorevalue = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

# Game Over text
over_font = pygame.font.Font("freesansbold.ttf", 64)

# player 2
player2img = pygame.image.load("player2.png") 
player2X = 200
player2Y = player_starty
player2X_change = 0

# Collision
def isCollision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt((math.pow(enemyX - playerX, 2)) + (math.pow(enemyY - playerY, 2)))
    return distance < collision_distance

# Score Display
def show_score(x, y):
    score = font.render("Score: " + str(scorevalue), True, (255, 255, 255))
    screen.blit(score, (x, y))

# Draw Players
def player1(x, y):
    screen.blit(playerimg, (x, y))

def player2(x, y):
    screen.blit(player2img, (x, y))

# Draw Enemy
def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))

# Main Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keydown events
        if event.type == pygame.KEYDOWN:
            # Player 1 (Arrow keys)
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            # Player 2 (WASD)
            if event.key == pygame.K_a:
                player2X_change = -5
            if event.key == pygame.K_d:
                player2X_change = 5

        # Keyup events
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                playerX_change = 0
            if event.key in (pygame.K_a, pygame.K_d):
                player2X_change = 0

    # Player movements
    playerX += playerX_change
    player2X += player2X_change

    # Boundary checks
    playerX = max(0, min(playerX, screen_width - 64))
    player2X = max(0, min(player2X, screen_width - 64))

    # Enemy Movement
    for i in range(enemynum):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = enemy_speedx
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= screen_width - 64:
            enemyX_change[i] = -enemy_speedx
            enemyY[i] += enemyY_change[i]

        # Collision with Player 1
        if isCollision(enemyX[i], enemyY[i], playerX, playerY):
            scorevalue += 1
            enemyX[i] = random.randint(0, screen_width - 64)
            enemyY[i] = random.randint(enemy_starty_min, enemy_starty_max)

        # Collision with Player 2
        if isCollision(enemyX[i], enemyY[i], player2X, player2Y):
            scorevalue += 1
            enemyX[i] = random.randint(0, screen_width - 64)
            enemyY[i] = random.randint(enemy_starty_min, enemy_starty_max)

        enemy(enemyX[i], enemyY[i], i)

    # Draw Players
    player1(playerX, playerY)
    player2(player2X, player2Y)

    show_score(textX, textY)
    pygame.display.update()

def show_score(x,y): #display current score onscreen
    score = font.render("Score:"+str(scorevalue), True, (255, 255, 255))
    screen.blit(score(x,y))
def gameover_text(): #display game over text
    over_text = over_font.render("GAME OVER.", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
def player(x,y): # draw player onscreen
    screen.blit(playerimg, (x,y))
def enemy(x,y,i): # draw enemy onscreen
    screen.blit(enemyimg[i], (x,y))
def firebullet(x,y): # fire a bullet from player's position
    global bulletstate
    bulletstate = "fire"
    screen.blit(bulletimg, (x+16, y+10))
def isCollision(enemyX, enemyY, bulletX, bulletY): # check if there was a collision btwn enemy and bullet
    distance = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
    return distance < collision_distance

# game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                playerX_change = -5
            if event.type == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bulletstate == "ready":
                bulletX = playerX
                firebullet(bulletX, bulletY)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0
        
        # player movement
        playerX += playerX_change
        playerX = max(0, min(playerX, screen_width - 64)) # 64 is the player size

        # enemy movement
        for i in range(enemynum):
            if enemyY[i] > 340: # game over condition
                for j in range(enemynum):
                    enemyY[j] = 2000
                gameover_text()
                break
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0 or enemyX[i] >= screen_width - 64:
                enemyX_change[i] *= -1
                enemyY[i] += enemyY_change[i]
            
            # collision check
            if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
                bulletY = player_starty
                bulletstate = "ready"
                scorevalue += 1
                enemyX[i] = random.randint(0, screen_width - 64)
                enemyY[i] = random.randint(enemy_starty_min, enemy_starty_max)
            enemy(enemyX[i], enemyY[i], i)
        
        # bullet movement
        if bulletY <= 0:
            bulletY = player_starty
            bulletstate = "ready"
        elif bulletstate == "fire":
            firebullet(bulletX, bulletY)
            bulletY -= bulletY_change
        player(playerX, playerY)
        show_score(textX, textY)
        pygame.display.update()

pygame.mixer.music
pygame.init()
pygame.mixer.music.load("bgm.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)