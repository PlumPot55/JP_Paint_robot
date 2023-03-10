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
    
    def determine_next_move(self, grid, enemies, game_info):
       
       #Will try just do a snake movement, cover all the blocks YOLO.
       
          
       x = self.position[0] 
       y = self.position[1] 
       print(self.Down) 
       if x > 0 and self.AllLeft == 0: #We always start moving left
       
        
         return Move.LEFT
       
       if x == 0 and y > 0 and self.AllLeft == 0 and self.Down == 0: #When we get left but not 0 on Y axis we go one down
         self.AllLeft = 1
         self.AllRight = 0
         return Move.DOWN
       
       if x == 0 and y > 0 and self.AllLeft == 0 and self.Down == 1: #When we get left but not 0 on Y axis we go one down
         self.AllLeft = 1
         self.AllRight = 0
         return Move.UP
       
       if self.AllLeft == 1 and x < (grid.shape[0]-1): #We start moving right untill the end
          
          return Move.RIGHT
       
       if x == (grid.shape[0]-1) and self.Down == 0 : #Then we go down by one and then we go left again
          self.AllRight = 1
          self.AllLeft = 0
          
          return Move.DOWN
       
       if x == (grid.shape[0]-1) and y < (grid.shape[1]-1) and  self.Down == 1 : #Then we go down by one and then we go left again
          self.AllRight = 1
          self.AllLeft = 0
          
          return Move.UP
      
       
       if x == 0 and y == 0: #Now we at the bottom left we have to reverse the directions
          
          self.AllLeft = 1
          self.Down = 1
          self.AllRight = 0
          
          return Move.RIGHT  
       
       if x == (grid.shape[0]-1) and y == (grid.shape[1]-1): #Now we at the bottom left we have to reverse the directions
          print('Im here')
          self.AllLeft = 0
          self.Down = 0
          self.AllRight = 1
          
          return Move.LEFT
       
       if self.AllRight == 1:

          return Move.LEFT

        
       
       return Move.DOWN
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # Chooses a random target location, and moves there.
        # Once it's there, choose a new location.
        
        # Create a target in storage if doesn't exist
        #if  self.target is None:
        #    self.target = np.zeros_like(self.position)

        # If reached the target find a new target
        #if np.array_equal(self.position, self.target):
        #    self.target[0] = random.randint(0, grid.shape[0] - 1)
        #    self.target[1] = random.randint(0, grid.shape[1] - 1)
        
        # Move in direction of target
        #if self.target[0] > self.position[0]:
        #    return Move.RIGHT
        #elif self.target[0] < self.position[0]:
        #    return Move.LEFT
        #elif self.target[1] > self.position[1]:
        #    return Move.UP
        #else:  