from collections import Counter 

s1='below'
s2='elbow'

print('anagram') if Counter(s1)==Counter(s2) else print("not an anagram")