import pygame
pygame.init()
from sprite import Spritesheet






width , height  = 600,  600
canvas  = pygame.Surface((width   , height ))
window  = pygame.display.set_mode((width , height))

my_spritesheet = Spritesheet(r'C:\Users\vinay\Desktop\Tutorials Learning\pygame\cd Codes - learning\texture.png')
# trainer_1 = my_spritesheet.get_sprite(0 , 0,26,48)
trainer_1  = [my_spritesheet.parse_data('trainer1.png')]


running  =  True
while running:


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running  = False
        

    canvas.fill("Red")
    canvas.blit(trainer_1 , (100 , 100))
    window.blit(canvas , (0,0))
    pygame.display.update()

pygame.quit()