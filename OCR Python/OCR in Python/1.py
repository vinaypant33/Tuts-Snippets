''' 
OCR workflow and how does that work : 

PIL (pillow) : open and Image
Open CV ( change an Image )
Tesseract (Pytesseract) :  OCR an Image




'''


from PIL import Image
import cv2
import pytesseract

im_file  = 'OCR in Python\paper.jpg'

im = Image.open(im_file)

print(im)
im.show()

im.rotate(90).show() ## Shows th rotated Image



''' Open the image and do some preprocessing and check the Image and make some simple OCR 

we cna also crp the image and rotate the image 

'''

