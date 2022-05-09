import re

f=open("grammer.txt","r")

Non_terminal=[]
grammer=[]
first_set={}
follow_set={}
visited=[]

print("Grammer : ")
for x in f:
    x=(re.sub(" +"," ",x.strip()))
    y=x.split("->")
    Non_terminal.append(y[0].strip())
    grammer.append(y[1].lstrip())
    first_set[y[0].strip()]=[]
    follow_set[y[0].strip()]=[]
    print(x)
visited=[0]*len(Non_terminal)
print("\n--------------------------------------------\n")

def cal_first(f_grammer,m):
    if visited[m]==1:
        return
    temp=[f_grammer]
    if "/" in f_grammer :
        temp=f_grammer.split("/")
    for char in temp:
        if not char[0].isupper():
            if char[:2]=="id":
                first_set[Non_terminal[m]].append(char[:2])
                visited[m]=1
            else:
                first_set[Non_terminal[m]].append(char[0])
                visited[m]=1
        else:
            char1=char[0] if char[1]!="'" else char[0]+char[1]
            cal_first(grammer[Non_terminal.index(char1)],Non_terminal.index(char1))
            first_set[Non_terminal[m]].extend(first_set[char1])
            visited[m]=1
    return

for i in range(0,len(Non_terminal)):
    if visited[i]==1:
        continue
    cal_first(grammer[i],i)

def cal_follow(n_terminal,m):
    if m==0:
        follow_set[n_terminal].append("$")
    for f_grammer in grammer:
        temp=[f_grammer]
        if "/" in f_grammer :
            temp=f_grammer.split("/")
        for char in temp:
            index=check_grammer(char,n_terminal)
            if index!=-1:
                if index!=len(char)-1:
                    if char[index+1]!="@":
                        if char[index+1].isupper():
                            if index+1!=len(char)-1 and char[index+2]=="'":
                                follow_set[n_terminal].extend(first_set[char[index+1:index+3]])
                                if "@" in first_set[char[index+1:index+3]]:
                                    follow_set[n_terminal].extend(follow_set[Non_terminal[grammer.index(f_grammer)]])
                                if "@" in follow_set[n_terminal]:
                                    follow_set[n_terminal].remove("@")
                            else:
                                follow_set[n_terminal].extend(first_set[char[index+1]])
                                if "@" in follow_set[n_terminal]:
                                    follow_set[n_terminal].remove("@")
                                if "@" in first_set[char[index+1:index+3]]:
                                    follow_set[n_terminal].extend(follow_set[Non_terminal[grammer.index(f_grammer)]])
                        else:
                            follow_set[n_terminal].append(char[index+1])
                elif index==len(char)-1:
                    if char[index]=="'":
                        temp=char[-2:]
                    else:
                        temp=char
                    if visited[grammer.index(f_grammer)]==1:
                        follow_set[n_terminal].extend(follow_set[Non_terminal[grammer.index(f_grammer)]])
    visited[m]=1
    return

def check_grammer(char,n_terminal):
    for i in range(len(char)):
        if n_terminal[-1]=="'":
            if char[i]==n_terminal[0] and char[i+1]=="'":
                return i+1
        else:
            if char[i]==n_terminal and char[i+1]!="'":
                return i
    return -1
visited=[0]*len(Non_terminal)
for i in range(0,len(Non_terminal)):
    if visited[i]==1:
        continue
    cal_follow(Non_terminal[i],i)

print("First_Set : ")
for char in Non_terminal:
    first_set[char]=", ".join(first_set[char])
    print("{} : {}".format(char,first_set[char]))

print("\n--------------------------------------------\n")

print("Follow_Set : ")
for char in Non_terminal:
    follow_set[char]=", ".join(sorted(set(follow_set[char]),key=follow_set[char].index))
    print("{} : {}".format(char,follow_set[char]))

print("\n--------------------------------------------\n")