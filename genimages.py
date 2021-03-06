"""A small script for generating a markdown page from images.
Run from inside root folder of repo"""
import os
with open('images.md', 'w') as f:
    print("Generating markdown")
    for image in sorted(os.listdir("Images/Thumbnails")):
        f.write("[{0}](Schematics/{0})\n\n".format(image.replace("png","schematic")))
        f.write("![{0}](Images/Thumbnails/{0})\n\n".format(image))
