import csv, sqlite3
conn = sqlite3.connect("C:\\CET\\demo.sqlite")
curs = conn.cursor()
curs.execute("DROP TABLE IF EXISTS Employees;")
curs.execute(''' CREATE TABLE Employees (
                  id        INTEGER PRIMARY KEY AUTOINCREMENT,
                  name      TEXT, email     TEXT,
                  country   TEXT, salary    INTEGER,
                  company   TEXT, dob       DATETIME); ''')

fin = open("C:\\CET\\dataJun-21-2018.csv")
reader = csv.reader(fin)
next(reader, None)  #skip the header
for row in reader:
    to_db = []
    for i in range(len(row)):
        to_db.append(row[i])
    curs.execute('''
    INSERT INTO EMployees (name, email, country, salary, company, dob) 
    VALUES (?, ?, ?, ?, ?, ?);''', to_db)
conn.commit()
conn.close()
fin.close()



