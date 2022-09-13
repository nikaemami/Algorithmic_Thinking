import math
n = int(input())
plan=[]
for i in range(n):
    plan.append(list(map(int,input().split())))

choice_dict={}
for i in range(n):
    for j in range(1,len(plan[i])):
        if plan[i][j] in choice_dict:
            choice_dict[plan[i][j]]+=1
        else:
            choice_dict[plan[i][j]]=1


possible_plan = [None]*n
length=[]
count_dict={}
for i in choice_dict:
    count_dict[i]=0

for i in range(n):
    length.append(len(plan[i]))
max_length = max(length)

condition=0
for i in range (2,max_length+1):
    for j in range(n):
        choose_cond=0
        element=1
        if(len(plan[j]) == i):
             while (choose_cond == 0 and element < i ):
                if(count_dict[plan[j][element]]+1 <= math.floor(n/2)):
                  count=choice_dict[plan[j][element]]
                  possible_plan[j]=plan[j][element]
                  choice_dict[plan[j][element]]-=1
                  count_dict[plan[j][element]]+=1
                  choose_cond=1
                else:
                    element+=1
             if (element >= i):
                 condition=1
                 break
    

             for k in range(1,len(plan[j])):
                 if (choice_dict[plan[j][k]] > count and (count_dict[plan[j][k]]+1) <= math.floor(n/2)):
                     possible_plan[j]=plan[j][k]
                     choice_dict[plan[j][element]]+=1
                     choice_dict[plan[j][k]]-=1
                     count_dict[plan[j][element]]-=1
                     count_dict[plan[j][k]]+=1

    if(condition==1):
        break


if condition == 0:
    print("YES")
    print(*possible_plan)
else:
    print("NO")