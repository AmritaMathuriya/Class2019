from pygame.locals import *
import pygame
import numpy as np
import time
import random 
from random import randint

grid_x = 44
grid_y = 44

class Player:
    dis_x = grid_x 
    dis_y = grid_y
    speed = 44 
 
    def moveRight(self):
        self.dis_x = self.dis_x + self.speed
        return int(self.dis_x/44), int(self.dis_y/44)
 
    def moveLeft(self):
        self.dis_x = self.dis_x - self.speed
        return int(self.dis_x/44), int(self.dis_y/44)

    def moveUp(self):
        self.dis_y = self.dis_y - self.speed
        return int(self.dis_x/44), int(self.dis_y/44)

    def moveDown(self):
        self.dis_y = self.dis_y + self.speed
        return int(self.dis_x/44), int(self.dis_y/44)

class Maze:
    def __init__(self):
       self.M = 20 
       self.N = 20 
       #self.maze = np.zeros(shape=(self.M,self.N))
       self.maze = np.random.randint(2, size=(self.M,self.N))

       for i in range (0, self.M):
        for j in range (0, self.N):
            value = randint(0, 10)
            if value < 0:
                self.maze[i][j] = 0

       for i in range(0, (self.N)//2):
           self.maze[i][1] = 0        

       for i in range(0, (self.M)//2):
           self.maze[self.N//2][i] = 0     
    
       for i in range(0, (self.M)//2):
           self.maze[i][8] = 0     

       for i in range((self.N)//2-1, self.N):
           self.maze[self.M//2][i] = 0      
    
       self.maze[1][2] = 0
       self.maze[:][3] = 0
       for i in range(0,self.N):
            self.maze[i][18] = 0    

       # Set the boundries as 1 to display the bricks on boundaries. 
       self.maze[0][:] = 1
       self.maze[self.M-1][:] = 1

       self.maze[0][:] = 1
       self.maze[self.M-1][:] = 1

       for i in range(self.N):
        self.maze[i][self.N-1]  = 1
        self.maze[i][0]  = 1

       # Set the player's position and start and end bricks to 0  
       self.maze[2][2] = 0
       self.maze[1][0] = 0 
       self.maze[self.M-1][self.N-2] = 0 
       self.maze[1][1] = 0 
    

       # self.maze = [ 1,1,1,1,1,1,1,1,1,1,
       #              1,0,0,0,0,0,0,0,0,1,
       #              1,0,1,1,1,1,1,1,0,1,
       #              1,0,1,1,1,1,1,1,0,1,
       #              1,0,1,0,0,0,0,0,0,1,
       #              1,0,1,0,1,1,1,1,0,1,
       #              1,0,0,0,0,0,0,0,0,1,
       #              1,1,1,1,1,1,1,1,1,1,]

    def draw(self,display_surf,image_surf):
       for i in range(0,self.M):
        for j in range(0, self.N):
           if self.maze[i] [j] == 1:
               display_surf.blit(image_surf,( i * 44 , j * 44))

class App:
 
    windowWidth = 880 
    windowHeight = 880
    player = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.player = Player()
        self.maze = Maze()
        self.grid_xID = int(self.player.dis_x/44)
        self.grid_yID = int(self.player.dis_y/44)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        
        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self._image_surf = pygame.image.load("player.png").convert()
        self._block_surf = pygame.image.load("block.png").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        pass
    
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self._image_surf,(self.player.dis_x,self.player.dis_y))
        self.maze.draw(self._display_surf, self._block_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()


    def blockage(self):
        if ( self.maze.maze[self.grid_xID][self.grid_yID] == 1 ):
            return True 
        return False

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()

            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                    self.grid_xID, self.grid_yID = self.player.moveRight()
                    if (self.blockage()):
                        self.grid_xID, self.grid_yID = self.player.moveLeft()
 
            if (keys[K_LEFT]):
                    self.grid_xID, self.grid_yID =self.player.moveLeft()
                    if (self.blockage()):
                        self.grid_xID, self.grid_yID =self.player.moveRight()
 
            if (keys[K_UP]):
                    self.grid_xID, self.grid_yID =self.player.moveUp()
                    if (self.blockage()):
                        self.grid_xID, self.grid_yID =self.player.moveDown()
 
            if (keys[K_DOWN]):
                    self.grid_xID, self.grid_yID = self.player.moveDown()
                    if (self.blockage()):
                        self.grid_xID, self.grid_yID =self.player.moveUp()
 
            if (keys[K_ESCAPE]):
                self._running = False
            
            self.on_loop()
            self.on_render()
            time.sleep(0.1)
            #print (self.player.dis_x, self.player.dis_y, self.grid_xID, self.grid_yID)
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
