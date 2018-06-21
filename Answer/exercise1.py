def findLongestWord(text):
    data = text.split()
    longest = ""
    for i in data:
        if len(i) > len(longest):
            longest = i
    return longest

print (findLongestWord("Friday is my favorite day"))