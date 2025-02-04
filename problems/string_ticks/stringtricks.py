shift=-2
sb = 97 + (ord('a')+shift-97)%26 # For python -2%26 = 24
# sb = 97 + (ord('a')+shift-97+26)%26 # For other languages -2%26 = -2, so we need to add 26

print(sb)