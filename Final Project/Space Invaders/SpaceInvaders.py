# Enoch Wang
# 4/30/2020
# Final Project: Space Invaders
# CSCI 6651
# Professor Gulnora Nurmatova 

import pygame, sys, random, os
from pygame.locals import *

level = 1
lives = 3
score = 0
bombs = 2

def wmd():
    global bombs
    bombs = bombs - 1
    
def coldwar():
    global bombs
    bombs = bombs + 1

def point():
    global score
    score = score + 1

def lose():
    global lives
    lives = lives - 1

def add():
    global level
    level = level + 1
    
class Game:
    screen = None
    aliens = []
    rockets = []
    obsticle = []
    beams = []
    lost = False

    def __init__(self, width, height):
        
        pygame.init()
        
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        done = False

        hero = Hero(self, width / 2, height - 20)
        generator = Generator(self)
        rocket = None
        beam = None
        
        while not done:
            if len(self.aliens) == 0:
                if self.lost == True:
                    lose()
                    self.lost = False
                    self.rockets.clear()
                    self.beams.clear()
                    self.obsticle.clear()
                    generator = Generator(self)
                    hero = Hero(self, width / 2, height - 20)
                    rocket = None
                    beam = None
                    obsticle = None
                elif self.lost == False:
                    stringLevel = str(level)
                    self.displayText("Level " + stringLevel + " Win! Continue? y/n")
                    pressed = pygame.key.get_pressed()
                    if pressed[pygame.K_y]:
                        add()
                        self.rockets.clear()
                        self.obsticle.clear()
                        self.beams.clear()
                        generator = Generator(self)
                        hero = Hero(self, width / 2, height - 20)
                        rocket = None
                        beam = None
                        obsticle = None
                    elif pressed[pygame.K_n]:
                        pygame.quit()
                        sys.exit()
                
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:  # sipka doleva
                hero.x -= 2 if hero.x > 20 else 0  # leva hranice plochy
            elif pressed[pygame.K_RIGHT]:  # sipka doprava
                hero.x += 2 if hero.x < width - 20 else 0  # prava hranice

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost and len(self.aliens)!=0:
                    self.rockets.append(Rocket(self, hero.x, hero.y))
                if event.type == pygame.KEYDOWN and event.key == pygame.K_z and not self.lost and len(self.aliens) !=0 and bombs > 0:
                    wmd()
                    self.beams.append(Beam(self, hero.x, hero.y))

            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))
            self.hud()
            
            for alien in self.aliens:
                alien.draw()
                alien.checkCollision(self)

                if (alien.y > height):
                    if (lives == 0):
                        self.displayRedText("GAME OVER! any key to exit")
                        pressed = pygame.key.get_pressed()
                        if event.type == pygame.KEYDOWN:
                            pygame.quit()
                            sys.exit()
                    else:
                        self.lost = True
                        self.displayRedText("YOU DIED level " + str(level) + " Continue? y/n")
                        pressed = pygame.key.get_pressed()
                        if pressed[pygame.K_y]:
                             self.obsticle.clear()
                             self.aliens.clear()
                        elif pressed[pygame.K_n]:
                            pygame.quit()
                            sys.exit()
                
            for obsticle in self.obsticle:
                obsticle.draw()
                obsticle.checkCollision(self)

            for rocket in self.rockets:
                rocket.draw()
                
            for beam in self.beams:
                beam.draw()

            if not self.lost: 
                hero.draw()
                
    def displayText(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('arial', 50)
        textsurface = font.render(text, True, (0,128,128))
        self.screen.blit(textsurface, (160, 100))
        
    def displayRedText(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('agencyfb', 50)
        textsurface = font.render(text, True, (128,0,0))
        self.screen.blit(textsurface, (160, 100))
        
    def hud(self):
        pygame.font.init()
        font = pygame.font.SysFont('arial', 20)
        hudstring = "Score: " + str(score)
        textsurface = font.render(hudstring, True, (0,128,0))
        self.screen.blit(textsurface, (10, 5))
        hudstring = "Bombs: " + str(bombs)
        textsurface = font.render(hudstring, True, (0,128,0))
        self.screen.blit(textsurface, (100, 5))
        hudstring = "Level: " + str(level) 
        textsurface = font.render(hudstring, True, (0,128,0))
        self.screen.blit(textsurface, (650, 5))
        hudstring = "Lives: " + str(lives) 
        textsurface = font.render(hudstring, True, (0,128, 0))
        self.screen.blit(textsurface, (730, 5))
        
    
        
class Alien:
    z = 0
    def __init__(self, game, image, x, y):
        self.x = x
        self.game = game
        self.y = y
        self.size = 30
        self.image = image

    def draw(self):
        super().__init__()
        if level <= 3:
            self.y = self.y + 0.1 + (0.05*(score/100))  
            if ((self.x + 1) % 30) != 0 and Alien.z == 0:
                self.x += 0.5
            elif((self.x + 1) % 30) == 0 and Alien.z == 0:
                Alien.z = 1
            elif((self.x - 1) % 30) != 0 and Alien.z == 1:
                self.x -= 0.5
            elif((self.x - 1) % 30) == 0 and Alien.z == 1:
                Alien.z = 0   
        elif level > 3:
            self.y = self.y + ((level-3)*0.05) + 0.1 + (0.05*(score/100))  
            if ((self.x + 1) % 30) != 0 and Alien.z == 0:
                self.x += 0.5
            elif((self.x + 1) % 30) == 0 and Alien.z == 0:
                Alien.z = 1
            elif((self.x - 1) % 30) != 0 and Alien.z == 1:
                self.x -= 0.5
            elif((self.x - 1) % 30) == 0 and Alien.z == 1:
                Alien.z = 0
            
        self.surf = self.image
        self.rect = self.surf.get_rect(center = (self.x,self.y))    
        self.game.screen.blit(self.surf, self.rect)

    def checkCollision(self, game):
        for rocket in game.rockets:
            if (rocket.x < self.x + self.size and
                    rocket.x > self.x - self.size and
                    rocket.y < self.y + self.size and
                    rocket.y > self.y - self.size):
                game.rockets.remove(rocket)
                game.aliens.remove(self)
                point()
                if (score % 100 == 0) and score != 0:
                    coldwar()
        for beam in game.beams:
            if (beam.x < self.x + self.size and
                    beam.x > self.x - self.size and
                    beam.y < self.y + self.size and
                    beam.y > self.y - self.size):
                game.beams.remove(beam)
                game.aliens.clear() 
                
class Obsticle:
    def  __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
        self.size = 10
    
    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (235, 52, 195),pygame.Rect(self.x, self.y, self.size, self.size))
        
    def checkCollision(self, game):
        for rocket in game.rockets:
            if (rocket.x < self.x + self.size and
                    rocket.x > self.x - self.size and
                    rocket.y < self.y + self.size and
                    rocket.y > self.y - self.size):
                game.rockets.remove(rocket)             

        for beam in game.beams:
            if (beam.x < self.x + self.size and
                    beam.x > self.x - self.size and
                    beam.y < self.y + self.size and
                    beam.y > self.y - self.size):
                game.beams.remove(beam)

class Hero:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (210, 250, 251),
                         pygame.Rect(self.x, self.y, 8, 5))



class Generator:
    def __init__(self, game):
        margin = 40  # mezera od okraju obrazovky
        width = 60  # mezera mezi alieny
        img = pygame.image.load("./alien1.png").convert_alpha()
        scaled_img1 = pygame.transform.scale(img, (30,30))
        img = pygame.image.load("./alien2.png").convert_alpha()
        scaled_img2 = pygame.transform.scale(img, (30,30))
        img = pygame.image.load("./alien3.png").convert_alpha()
        scaled_img3 = pygame.transform.scale(img, (30,30))
        
        if level == 1:
            for x in range(5+level):
                game.obsticle.append(Obsticle(game, random.randint(0,795), random.randint(180,500)))
            for x in range(margin, game.width - margin, width):
                game.aliens.append(Alien(game, scaled_img1, x, 50))
        elif level == 2:
            for x in range(5+level):
                game.obsticle.append(Obsticle(game, random.randint(0,795), random.randint(180,500)))
            for x in range(margin, game.width - margin, width):
                game.aliens.append(Alien(game, scaled_img1, x, 50))
            for x in range(margin, game.width - margin, width):
                game.aliens.append(Alien(game, scaled_img2, (x+15), 100))
        elif level == 3:
            for x in range(5+level):
                game.obsticle.append(Obsticle(game, random.randint(0,795), random.randint(180,500)))
            for x in range(margin, game.width - margin, width):
                game.aliens.append(Alien(game, scaled_img1, x, 50))
            for x in range(margin, game.width - margin, width):
                game.aliens.append(Alien(game, scaled_img2, (x-15), 100))
            for x in range(margin, game.width - margin, width):
                game.aliens.append(Alien(game, scaled_img3, (x+15), 150))    
            
        elif level > 3: 
            for x in range(5+level):
                game.obsticle.append(Obsticle(game, random.randint(0,795), random.randint(180,500)))
            for x in range(margin, game.width - margin, width):
                game.aliens.append(Alien(game, scaled_img1, x, 50))
            for x in range(margin, game.width - margin, width):
                game.aliens.append(Alien(game, scaled_img2, (x-15), 100))
            for x in range(margin, game.width - margin, width):
                game.aliens.append(Alien(game, scaled_img3, (x+15), 150))



class Rocket:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game

    def draw(self):
        pygame.draw.rect(self.game.screen,  # renderovací plocha
                         (254, 52, 110),  # barva objektu
                         pygame.Rect(self.x, self.y, 2, 4))
        self.y -= 2  # poletí po herní ploše nahoru 2px/snímek
        
class Beam:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game

    def draw(self):
        pygame.draw.circle(self.game.screen, (0, 208, 255), (self.x, self.y), 10)    
        self.y -= 1




if __name__ == '__main__':
    game = Game(800, 600)
    
    