import os
from PIL import Image, ImageFilter

where = ".\\Day2Resource\\img\\"
outfolder = ".\\Day2Resource\\imgout\\"

def processAllImages(onlyFirst):
    c = 1
    for root, dirs, files in os.walk(where):
        for file in files:
            fullname = os.path.join(root, file)
            if file.lower().endswith("jpg") or \
                    file.lower().endswith("bmp") or \
                    file.lower().endswith("png"):
                im = Image.open(fullname)
                outFileName = os.path.join(outfolder, file)
                print ("%2d %s size:%s (%s)" \
                       % (c, fullname, im.size, im.mode))

                mark = Image.open(".\\Day2Resource\\watermark.png")
                mark = mark.resize((100, 100))

                out = watermark(im, mark, (0, 50))
                #im.show()
                #out.show()
                out.save(outFileName)
                c += 1
                if (onlyFirst):
                    return

def watermark(im, mark, position):
    layer = Image.new('RGBA', im.size, (0,0,0,0))
    layer.paste(mark, position)
    return Image.composite(layer, im, layer)


processAllImages(True)

