import os

where = ".\\Day2Resource\\img\\"

def processAllImages(onlyFirst):
    c = 1
    for root, dirs, files in os.walk(where):
        for file in files:
            fullname = os.path.join(root, file)
            if file.lower().endswith("jpg") or \
                    file.lower().endswith("bmp") or \
                    file.lower().endswith("png"):
                print ("%2d %s" % (c, fullname))
                c += 1
                if (onlyFirst):
                    return

processAllImages(True)

