import os
from PIL import Image, ImageFilter, ImageDraw

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

                f,e = os.path.splitext(file)
                file = f + "_blur" + e
                outFileName = os.path.join(outfolder, file)

                '''
                outfolder = outfolder + "blur\\"
                '''

                print ("%2d %s size:%s (%s)" \
                       % (c, fullname, im.size, im.mode))

                out = im.filter(ImageFilter.BLUR)
                #im.show()
                #out.show()

                #In case the out folder doesnt exist
                if (os.path.exists(outfolder) == False):
                    os.mkdir(outfolder)

                mark = Image.open(".\\Day2Resource\\watermark.png")
                mark = mark.resize((100, 100))
                out = watermark(im, mark, (0, 50))

                d = ImageDraw.Draw(out)
                d.text((700, 500), "Hello World", fill=(155, 155, 155))

                out.save(outFileName)
                c += 1
                if (onlyFirst):
                    return


def cleanOutput():
    print ("Removing old out files")
    for root, dirs, files in os.walk(outfolder):
        for file in files:
            fullName = os.path.join(root, file)
            os.remove(fullName)
            print (".")
    print ("Done")


def watermark(im, mark, position):
    layer = Image.new('RGBA', im.size, (0,0,0,0))
    layer.paste(mark, position)
    return Image.composite(layer, im, layer)

cleanOutput()
processAllImages(False)

