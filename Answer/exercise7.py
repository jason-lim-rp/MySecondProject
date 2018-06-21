import csv

#writing
fout = open("csvfile.txt", "w", newline="")
writer = csv.writer(fout)
writer.writerow(["Item1", "Item2", "Item3"])
writer.writerow(["123", "321", "222"])
fout.close()

#reading
fin = open("csvfile.txt")
reader = csv.reader(fin)
for row in reader:
    print (row)
fin.close()

