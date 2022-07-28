v4 = [283, 171, 159, 78, 112, 299, 76, 166, 257, 145, 124, 72, 170, 300, 149, 132, 86, 231, 219, 96, 239, 224, 190, 197]

def sleep(t):
    if( t % 2 == 0):
        t = t * (66 * 2 + t % 10)
    else:
        t = t * 66 + 5
    return t

v2 =  [0x0EA,0x0C, 0x0A5,0x13, 0x0E6,0x7E, 0x0FE, 9, 0x0AE,0x2E,0x94, 7, 0x0B8, 0x0BC,0x10, 0x132, 0x0B7, 0x16B, 0x174, 0x0D9,0x96, 0x0CC,0x94,0x151]


aSleep = []
dici = {}
for i in range(len(v4)):
    temp = sleep(v4[i])
    aSleep.append(temp)
    dici[v4[i]] = temp
    
aSleep.sort()

flag = ""
for i in range(len(aSleep)):
    for j in dici:
        if(dici[j] == aSleep[i]):
            flag += chr(j ^ v2[i])
            
print(flag)
    
