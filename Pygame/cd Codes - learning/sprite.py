import pygame
import json


pygame.init()


class Spritesheet():

    def __init__(self , filename) -> None:
        self.filename = filename
        self.spritesheet =  pygame.image.load(filename).convert()
        self.meta_data  = self.filename.replace('png' , 'json')
        with open(self.meta_data) as f:
            self.data  = json.load(f)
        f.close()

    def get_sprite(self , x,y,w,h):
        sprite = pygame.Surface((w, h ))
        sprite.set_colorkey((0,0,0)) ## This helps to make th etransparent as the surface is the blank slate and can be sued to reduce the  blackness in transparency
        sprite.blit(self.spritesheet , (0,0) , (x,y,w,h))
        return sprite

    ## We can use that using the name and  calling the json file and make use of this 

    def parse_data(self):
        ## the josn is like a dict under the dict and under the dict we just have to parse the data and check the data  
        sprite  = self.data['frames']['name']['frame']
        x,y,w,h = sprite['x'], sprite['y'] , sprite['w'] , sprite['h']
        image   = self.get_sprite(x,y,w,h)
        return image
    