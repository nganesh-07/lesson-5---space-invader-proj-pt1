import math
import pygame
import random

screen_width = 600
screen_height = 700
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
    enemyY.append(random.randint(0, enemy_starty_min, enemy_starty_max))
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
