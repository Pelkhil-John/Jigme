import pygame
import random
import math

pygame.init()
WIDTH, HEIGHT = 1200,800
PLAYER_WIDTH, PLAYER_HEIGHT = 35, 55
MAX_VEL = 5
win = False
score = 0
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("run nigga run")
player = pygame.Rect(WIDTH/2 - PLAYER_WIDTH/2, HEIGHT/2 - PLAYER_HEIGHT/2, PLAYER_WIDTH, PLAYER_HEIGHT)
entities = []
lanes = []
wall_1 = pygame.rect.Rect(-1000, 0, WIDTH/4 + 1000, HEIGHT)
wall_2 = pygame.rect.Rect(4*WIDTH/5, 0, 10000, HEIGHT)
finish = pygame.rect.Rect(0, -10000, WIDTH, HEIGHT)

class Entity:

    x, y = 0, 0
    on_screen = True
    rect = pygame.Rect(x,y,x,y)
    color = 0

    def __init__(self, x=random.random()*WIDTH, y=random.random()*HEIGHT, width=PLAYER_WIDTH, height=PLAYER_HEIGHT):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, width, height)
        self.color = pygame.color.Color(int(random.random()*255),int(random.random()*255),int(random.random()*255))
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y



def collision_car():
    global player
    for ent in entities:
        if player.colliderect(ent):
            # exit(0)
            pass
def collision_finish():
        global MAX_VEL, player
        if player.colliderect(finish):
            MAX_VEL += 2
            finish.y = -10000    
            pygame.mixer.music.play(0)

def draw(player):
    # WIN.blit()
    WIN.fill("black")
    for ent in lanes:
        pygame.draw.rect(WIN, ent.color, ent.rect)
    pygame.draw.rect(WIN, "red", player)
    for ent in entities:
        pygame.draw.rect(WIN, ent.color, ent.rect)
    
    pygame.draw.rect(WIN, "blue", wall_1)
    pygame.draw.rect(WIN, "blue", wall_2)
    pygame.draw.rect(WIN, "white", finish)
    pygame.display.update()


def is_on_screen(ent):
    if ent.rect.right < 0 or ent.rect.left > WIDTH or ent.rect.bottom < 0 or ent.rect.top > HEIGHT:
        ent.on_screen = False
    return ent.on_screen


def rolling_add(ent):
    if not is_on_screen(ent):
        if ent.rect.right < 0:
            entities.append(Entity(WIDTH, random.random()*HEIGHT))
        elif ent.rect.left > WIDTH:
            entities.append(Entity(0-PLAYER_WIDTH, random.random()*HEIGHT))
        elif ent.rect.bottom < 0:
            entities.append(Entity(random.random()*WIDTH, HEIGHT))
        elif ent.rect.top > HEIGHT:
            entities.append(Entity(random.random()*WIDTH, 0-PLAYER_HEIGHT))




def update_position(vel_x, vel_y):
    finish.y -= vel_y
 
    wall_1.x -= vel_x
    wall_2.x -= vel_x
    for ent in lanes:
        ent.x -= vel_x
        ent.y += MAX_VEL*7//5
        
        if ent.y > HEIGHT:
            ent.y = 0 - ent.rect.h 
        ent.update()
    if player.colliderect(wall_1) or player.colliderect(wall_2):
        for ent in lanes:
            ent.x += vel_x
        wall_1.x += vel_x
        wall_2.x += vel_x
        vel_x = 0

    
    for ent in entities:
        ent.x -= vel_x
        ent.y -= vel_y
        ent.update()
        if ent.on_screen:
            rolling_add(ent)


def check_win():
    if player.colliderect(finish):
        win = True
        score += 1

def main():
   
    for x in range(10):
        entities.append(Entity(random.random()*WIDTH, random.random()*HEIGHT))
    
    for x in range(10):
        lanes.append(Entity(WIDTH/2, x*HEIGHT/10, 10, 50))

    clock = pygame.time.Clock()
    while True:
        clock.tick(100)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                break

        keys = pygame.key.get_pressed()
        vel_x, vel_y = 0, 0
        if keys[pygame.K_a]:
            vel_x -= MAX_VEL
        if keys[pygame.K_d]:
            vel_x += MAX_VEL
        #if keys[pygame.K_s]:
        #    vel_y += MAX_VEL
        #dif keys[pygame.K_w]:
        vel_y -= MAX_VEL
        if math.sqrt(math.pow(vel_x, 2) + math.pow(vel_y, 2)) > MAX_VEL:
            vel_x, vel_y = vel_x/math.sqrt(2), vel_y/math.sqrt(2)
        check_win()
        if not win:
            update_position(vel_x, vel_y)
        collision_car()
        collision_finish()
        draw(player)


if __name__ == "__main__":
    main