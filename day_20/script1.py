from collections import Counter

mynums=[1,9,4,6,6,5,7,4,7,2,6,4,2,3,4,6,9]
counts=Counter(mynums)
print(counts)
for i in counts.most_common():
    if i[1]>3:
        print(i[0])
# enumerate()