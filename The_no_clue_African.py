import random
import numpy as np
from ..bot_control import Move
  
class TheCluelessAfrican:

    
    def __init__(self):
        
        self.AllLeft = 0
        self.AllRight = 0
        self.Up = 0
        self.Down = 0
        
    def get_name(self):
        return "The Clueless African"

    def get_contributor(self):
        return "JP Potgieter"
    
    def should_I_Move(self, id, tile):
        if tile == 0: return True
        return (id - tile) % 3 == 2  or self.id == tile
    
    def determine_next_move(self, grid, enemies, game_info):
       
       #Will try just do a snake movement, cover all the blocks YOLO.
       
       
       x = self.position[0] 
       y = self.position[1] 
      
       if x > 0 and self.AllLeft == 0: #We always start moving left
           
         
         if self.should_I_Move(self.id,grid[y][x-1]) == False and self.Down == 1:
           self.AllRight = 0
           self.AllLeft = 1
           if y == grid.shape[0]-1:
              self.Down = 0
              return Move.DOWN
            
           return Move.UP
                  
         
         if self.should_I_Move(self.id,grid[y][x-1]) == False and self.Down == 0:
            self.AllRight = 0
            self.AllLeft = 1
            if y == 0:
              self.Down = 1
              return Move.UP
            
            return Move.DOWN
         
         if self.should_I_Move(self.id,grid[y][x-1]) == False and self.Down == 0:
            return Move.DOWN
        

         return Move.LEFT
       
       
       if x == 0 and y > 0 and self.AllLeft == 0 and self.Down == 0: 
         self.AllLeft = 1
         self.AllRight = 0
        
                 
         return Move.DOWN
       
       if x == 0 and y > 0 and self.AllLeft == 0 and self.Down == 1: 
         
         
         self.AllLeft = 1
         self.AllRight = 0
        
         
         return Move.UP
       
       if self.AllLeft == 1 and x < (grid.shape[1]-1): 
          
         if self.should_I_Move(self.id,grid[y][x+1]) == False and self.Down == 1:
            if y == grid.shape[0]-1:
              self.Down = 0
              return Move.DOWN
         
            return Move.UP
         
         
         
         if self.should_I_Move(self.id,grid[y][x+1]) == False and self.Down == 0:
            self.AllRight = 0
            self.AllLeft = 1
            
            if y == 0:
              self.Down = 1
              return Move.UP
            
            
            return Move.DOWN
          
          
         return Move.RIGHT
       
       if x == (grid.shape[1]-1) and self.Down == 0 : 
          self.AllRight = 1
          self.AllLeft = 0
          
          return Move.DOWN
       
       if x == (grid.shape[1]-1) and y < (grid.shape[0]-1) and  self.Down == 1 : 
          self.AllRight = 1
          self.AllLeft = 0
          
          return Move.UP
      
       
       if y == 0: 
          
          self.AllLeft = 1
          self.Down = 1
          self.AllRight = 0
          
          return Move.UP  
       
       if  y == (grid.shape[1]-1): 
         
          self.AllLeft = 0
          self.Down = 0
          self.AllRight = 1
          
          return Move.DOWN
       
      # if self.AllRight == 1:

      #    return Move.LEFT

        
       
       return Move.DOWN
       
       
              
       
       
       
       
       
       
       
       
       
       
       
       
     