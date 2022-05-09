pseudo_opcode = ['START', 'USING', 'DC', 'DS', 'END']
MOT, POT, ST, LT, LC = [], [], [], [], []
location_counter = 0
text = [["JOHN", "START", ""], ["", "USING", "*,15"], ['', "LOAD", "1,FIVE"], ['', "ADD",
"1,FOUR"], ['', "STORE", "1,TEMP"],["FIVE", "DC", "F'5'"],["FOUR", "DC", "F'4'"],['TEMP', 'DS', "1'F'"],['', 'END', '']]

for i in text:
  if i[1] not in ['START', 'USING']:
    i.append(location_counter)
    LC.append(i)
    location_counter += 4
  else:
    i.append(location_counter)
    LC.append(i)

  if i[1] not in pseudo_opcode:
    MOT.append([i[1], '10', '001'])
  else:
    POT.append([i[1], ''])
    
  if i[0] != '':
    ST.append([i[0], i[3], 1 if i[2]=='' else 4, 'R'])
  if i[2].startswith("F'"):
    LT.append([i[2], i[3], 4, 'R'])

BT = []
for i in range(16):
 BT.append([i, 'Y' if i==15 else 'N', '' if i!=15 else 0])

print("\nLocation Counter Table", *LC, sep='\n')
print("\nMnemonic Opcode Table", *MOT, sep='\n')
print("\nPsedo Opcode Table", *POT, sep='\n')
print("\nSymbol Table", *ST, sep='\n')
print("\nLiteral Table", *LT, sep='\n')
print("\nBase Table", *BT, sep='\n')