from PIL import Image, ImageFilter
import os
import sys


nameOfContainerImages, newImagesDirectory = sys.argv[1], sys.argv[2]

if newImagesDirectory:
    os.mkdir(f"./{newImagesDirectory}")
    os.chdir('./images')
    print(os.getcwd())
    for img in os.listdir():
        with Image.open(img) as imgfile:
            imgfile.thumbnail((400,400))
            imgfile.save(f"../new_images/{img}-converted.png" , "png")
    
    print("converted successful")
    
print("the program has finished")