import pygame
pygame.init()





## making the cameras group  
camera_group = pygame.sprite.Group() # This is basically the sprite group which can be used later 
## Then add the plaerr insude the group 
player((300,300) , camera_group) # Player is the player class 

## we can add other trees in the same group 



## example for the plater or the class 

class Player(pygame.sprite.Sprite):
    def __init__(self, pos,group) -> None:
        super().__init__(group)
        ## then the image rect direc and  the speed can be defined in the group 
    
## Y sort camera make the plaer in front the trees and make it behind the trees and we dont have the z coordinate 
## Make the y position and for the higher values it will be drawn on the top  
""" Make the class for the cameras group and 
    make the custom draw method for that 
    The camera cannot be changed for that we have to make anothther method for it

    Make the surface somewhere else and  make the surface moving to the visible rectangle 
    make x and y location as the offset and then at the time of rendering make the offset with the draw fuction blit 
    blit.(sprite.image,offsetpos)
    
    self.offset  = pygame.math.vector2(300 , 100)
    ground_offset = self.ground.rect.topleft  +self.offset

    
    """

## Example code  :





"""
    for the camera box we check the player position wrt to the rectangle and if the player is near the rectangle then the rectangle should move
    


"""

