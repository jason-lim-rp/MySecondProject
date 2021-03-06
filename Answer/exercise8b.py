import os
from PIL import Image, ImageFilter

where = ".\\Day2Resource\\img\\"

def processAllImages(onlyFirst):
    c = 1
    for root, dirs, files in os.walk(where):
        for file in files:
            fullname = os.path.join(root, file)
            if file.lower().endswith("jpg") or \
                    file.lower().endswith("bmp") or \
                    file.lower().endswith("png"):
                im = Image.open(fullname)
                print ("%2d %s size:%s (%s)" \
                       % (c, fullname, im.size, im.mode))

                out = im.filter(ImageFilter.BLUR)
                im.show()
                out.show()
                c += 1
                if (onlyFirst):
                    return

processAllImages(True)

