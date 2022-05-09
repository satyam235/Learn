txt = open('input.txt', 'r')

MDT, MNT, ALA = [], {}, {}
i1, i2, i3, flag = 0, 0, 0, 0
# Pass 1
for line in txt:
  word = line.split()
  if word[0] == 'MACRO':
    MNT[word[1]] = i2
    i2 += 1
    ALA[word[2]] = i3
    i3 += 1
    flag = 1

  if word[0] == 'ENDM':
    MDT.append([str(i1), word])
    i1 += 1
    flag = 0

  if flag:
    if word[0] != 'MACRO':
      MDT.append([str(i1), word])
      i1 += 1

print("MNT Table : ")
for i in MNT:
 print(MNT[i], i)
print("\nMDT Table")
print(*MDT, sep='\n')
print('\nALA Table')
for i in ALA:
 print(ALA[i], i)