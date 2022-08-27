from collections import Counter
def counterTrick():
    s="aaabcddefa"
    c = Counter(s)
    print(c)



    s="11133223552"
    d = map(str,s)
    d = map(int,s) # maps it to array of integers
    print(d)
    c = Counter(map(int,s)) # make both sides integers

    print(c)



counterTrick()