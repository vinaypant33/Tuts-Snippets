'''
OCR in python : Optical Character Recognition

General Workflow for working : 

Open an Image  :  Pillow 
change and Image : Open CV  
OCR the Image : Tessract 




'''

## Installation of the libararies : 


'''

Pillow :  pip install pillow 
open CV  : pip install opencv-python  
tessract  : pip install     we have to isntall tessrat also to make it working https://digi.bib.uni-mannheim.de/tesseract/ downloading link for current workflow 
version 64 bit an 4.01 2019 is used


to check for tessract we have to sue the cmd as  :  tesseract --version 

pip install pytesseract 

'''


import cv2 
from PIL import Image
import pytesseract

