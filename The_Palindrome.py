import math
word = input()
count=0
count_2=1
for i in range(math.floor(len(word)/2)):
    if word[i] != word[len(word)-i-1]:
        count+=1
        count_2=2*count_2
        count_2=count_2%(10**9+7)
if (count==0):
    print(0,1)
else:
    print(count,count_2)