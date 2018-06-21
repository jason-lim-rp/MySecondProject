#File reading
fin = open("Day2Resource\\file.txt")
for i in fin:
    print (i)


#File writing
fout = open("newfile.txt", "w")
fout.write("this line has no newline")
fout.write("this line has a trailing newline\n")
fout.write("Adding a number " + str(5))
fout.close()