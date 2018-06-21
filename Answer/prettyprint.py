import pprint

pp = pprint.PrettyPrinter(depth = 3, width = 20, indent = 4)

#Example 1
a = ["Jack", "Mary", "Jackson", ["KL", "SIN", "BKK", ["Phuket", "Krabi"]]]
print (a)
print ()
pp.pprint(a)

#Example 2
a = {"names": ["Jack", "Mary", "Peter"],
     "cities": ["BKK", "TPE", "KUL"],
     "airlines" : { "SG": ["SIA", "MI"],
                    "MY": ["MH", "AK"]
                    }
     }
print (a)
print ()
pp.pprint(a)
