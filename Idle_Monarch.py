myinput = list(map(int,input().split()))
n = myinput[0]
q = myinput[1]
num_list = list(map(int,input().split()))
repeat_list=[]
index_list=[]
for i in range(q):
    c_d = list(map(int,input().split()))
    repeat_list.append(c_d[0])
    index_list.append(c_d[1])

def counted_array (num_list,n):
    cond=0
    i=0
    new_list={}
    while(cond == 0):
        condition=0
        i+=1
        new_list[i] = None
        count_list=[]
        for j in range(n):
            count_list.append(num_list.count(num_list[j]))
        num_list=count_list
        new_list[i]=num_list
        for j in range(n):
            if (num_list[j] != num_list.count(num_list[j])):
                condition = 1
        if (condition == 0):
             cond=1
    return new_list

new_array = counted_array(num_list,n)
array=[] 
for i in range(q):
    if(repeat_list[i] in new_array):
        array=new_array[repeat_list[i]]
    else:
        array=new_array[len(new_array)]
    new_index=index_list[i]
    print(array[new_index-1])