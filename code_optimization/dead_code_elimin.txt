f = open("code.py", "r")
line = f.readlines()

for i in range(len(line)):
    line[i] = line[i][:-1]

print("Code Before Optimization:")
for element in line: 
    print(element)

value = ''
newEq = []
for element in list(line):
    Eq=element.split()
    if 'if' in Eq:
        value = line[line.index(element) - 1].split('=')[1]
        newEq = Eq[1:]
        OtherValue = line[line.index(element)].split('==')[1]
        if value == OtherValue:
            break
        else:
            line.remove(line[line.index(element) + 1])
            line.remove(element)


print("\nCode After Optimization")
for element in line:
    print(element)