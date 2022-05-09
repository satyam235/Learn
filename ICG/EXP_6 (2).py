import pandas as pd

M_input=("A=B+C*D/E").split("=")
x=M_input[0]
y=M_input[1]
quadraples={"op":[],"arg1":[],"arg2":[],"result":[]}
flag=True
i=0

print("Input : A=B+C*D/E\n\nIntermediate Code Generation :")
def replace(index,symbol):
    global quadraples
    global y
    quadraples["op"].append(symbol)
    if y[index-1].isdigit():
        quadraples["arg1"].append(y[index-2:index])
        if (index+2)!=len(y) and y[index+2].isdigit():
            quadraples["arg2"].append(y[index+1:index+3])
            temp=y[index-2:index+3]
        else:
            temp=y[index-2:index+2]
            quadraples["arg2"].append(y[index+1])
    elif (index+2)!=len(y) and y[index+2].isdigit():
        quadraples["arg1"].append(y[index-1])
        quadraples["arg2"].append(y[index+1:index+3])
        temp=y[index-1:index+3]
    else:
        quadraples["arg1"].append(y[index-1])
        quadraples["arg2"].append(y[index+1])
        temp=y[index-1:index+2]
    print("T{} = {}".format(i,temp))
    y=y.replace(temp,("T"+str(i)))
    quadraples["result"].append("T"+str(i))

while flag==True:
    i+=1
    if "*" in y:
        index=y.index("*")
        replace(index,"*")
    elif "/" in y:
        index=y.index("/")
        replace(index,"/")
    elif "+" in y:
        index=y.index("+")
        replace(index,"+")
    elif "-" in y:
        index=y.index("-")
        replace(index,"-")
    else:
        flag=False

print("{} = T{}".format(x,i-1))
quadraples["op"].append("=")
quadraples["arg1"].append(quadraples["result"][-1])
quadraples["arg2"].append(" ")
quadraples["result"].append(x)


print("\nQuadraples : ")
print(pd.DataFrame(quadraples))