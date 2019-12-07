#This Game Was Make By me..

import pygame
import sys
import random
import time
 
pygame.init()

 #Make Class For Game
  
class Snake():
    def __init__(self):
        self.position = [100,50]
        self.body = [[100,50],[90,50],[80,50]]
        self.direction = "RIGHT"
        
#Direction Change Function
 
    def changeDirTo(self,dir):
        if dir=="RIGHT" and not self.direction=="LEFT":
            self.direction = "RIGHT"
        elif dir=="LEFT" and not self.direction=="RIGHT":
            self.direction = "LEFT"
        elif dir=="UP" and not self.direction=="DOWN":
            self.direction = "UP"
        elif dir=="DOWN" and not self.direction=="UP":
            self.direction = "DOWN"

         
    def move(self,foodPos):
        if self.direction == "RIGHT":
            self.position[0] = self.position[0] + 10
        elif self.direction == "LEFT":
            self.position[0] = self.position[0] - 10
        elif self.direction == "UP":
            self.position[1] = self.position[1] - 10
        elif self.direction == "DOWN":
            self.position[1] = self.position[1] + 10
        self.body.insert(0,list(self.position))
         
        if self.position == foodPos:
            return 1
        else:
            self.body.pop()
            return 0
 
    def move_Right(self):
        self.position[0] = self.position[0] + 10
    def move_Left(self):
        self.position[0] = self.position[0] - 10
    def move_Up(self):
        self.position[0] = self.position[1] - 10
    def move_Down(self):
        self.position[0] = self.position[1] + 10
     
    def checkCollision(self):
        if self.position[0] > 490 or self.position[0] < 10:
            return 1 
        elif self.position[1] > 500 or self.position[1] < 10:
            return 1
        for bodyPart in self.body[1:]:
            if self.position == bodyPart:
                return 1
        return 0
 
    def getHeadPosition(self):
        return self.position
     
    def getBody(self):
        return self.body
 
#Make food
 
class FoodSpawn():
    def __init__(self):
        self.position = [random.randint(4,46)*10,random.randint(4,46)*10]
        self.isFoodOnScreen = True
 
    def spawnFood(self):
        if self.isFoodOnScreen == False:
            self.position = [random.randrange(4,46)*10,random.randrange(4,46)*10]
            self.isFoodOnScreen = True
        return self.position
     
    def setFoodOnScreen(self,b):
        self.isFoodOnScreen = b
 
#Make Display For Game
 
window = pygame.display.set_mode((500 + 20,500 + 20))
pygame.display.set_caption("Snake Game")
fps = pygame.time.Clock()
 
score = 0
 
snake = Snake()
foodSpawner = FoodSpawn()

 #Game Over Function
  
def gameOver():
    font = pygame.font.SysFont('Candara', 30)
    score_text = font.render("Congrats you got " + str(score) + " points!",4,(255,0,0))
    window.blit(score_text,(100,250))
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver()
         
        pressed = pygame.key.get_pressed()

 #This Is Game Event Hendling(Direction change key)
  
        if pressed[pygame.K_RIGHT]:
            snake.changeDirTo('RIGHT')
        elif pressed[pygame.K_LEFT]:
            snake.changeDirTo('LEFT')
        elif pressed[pygame.K_UP]:
            snake.changeDirTo('UP')
        elif pressed[pygame.K_DOWN]:
            snake.changeDirTo('DOWN')
        elif pressed[pygame.K_ESCAPE]:
            gameOver()
 
 #Score Make With Loop
    foodPos = foodSpawner.spawnFood()
    if(snake.move(foodPos)==1):
        score+=1
        foodSpawner.setFoodOnScreen(False)
 
 #Color and Snack making
    window.fill(pygame.Color(225,225,225))
    for x in range(0, 520, 10):
        pygame.draw.rect(window, (0,0,225), [x, 0, 10, 10])
        pygame.draw.rect(window, (0,0,225), [x, 510, 10, 10])
 
    for x in range(0, 510, 10):
        pygame.draw.rect(window, (0,0,225), [0, x, 10, 10])
        pygame.draw.rect(window, (0,0,225), [510, x, 10, 10])
 
    for pos in snake.getBody():
        pygame.draw.rect(window,pygame.Color(0,225,0),pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(window,pygame.Color(225,0,0),pygame.Rect(foodPos[0],foodPos[1],10,10))
     
    if(snake.checkCollision()==1):
        gameOver()
     
    pygame.display.set_caption("Snake | Score: " + str(score))
    pygame.display.flip()
    fps.tick(20)
 
pygame.quit()

#THANKES FOR PLAY MY GAME
