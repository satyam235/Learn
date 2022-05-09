txt = open('3 Display expanded code (Macroprocessor)\input.txt', 'r')

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

sample_asm = open('3 Display expanded code (Macroprocessor)\input.txt', 'r')
expanded_code, flag = [], 0
for line in sample_asm:
  word = line.split()

  if word[0] == 'ENDM':
    flag = 0
  if word[0] == 'MACRO':
    flag = 1
  else:
    if not flag and word[0]!='ENDM':
      if word[0] not in MNT.keys():
        expanded_code.append(word)
      else:
        curr_param = word[1]
        for instrn in MDT:
          if instrn[1][0] == 'ENDM':
            break
          if 'XX' in instrn[1]:
            index = instrn[1].index('XX')
            expanded_code.append(instrn[1][0:index] + [curr_param] + instrn[1][index+1:])
          else:
            expanded_code.append(instrn[1])

for i in expanded_code:
 print(" ".join(i))