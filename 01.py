#Functions

def findLongestWord(text):
    data = text.split()
    print (type(data), len(data))
    longest = ""
    cycle = 1
    for i in data:
        print ("Cycle : ", cycle, "Examining ", i)
        print (longest, len(longest))
        if len(i) > len(longest):
            longest = i
            print("Found longer word", longest, len(longest))
        cycle += 1
    return longest

print (findLongestWord("Friday is my favorite day"))

