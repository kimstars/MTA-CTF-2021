x = [234, 12, 165, 19, 230, 126, 254, 9, 174, 46, 148, 7,
     184, 188, 16, 306, 183, 363, 372, 217, 150, 204, 148, 337]
v4 = [283, 171, 159, 78, 112, 299, 76, 166, 257, 145, 124, 72,
      170, 300, 149, 132, 86, 231, 219, 96, 239, 224, 190, 197]
flag = []
d = {}
for t in v4:
    a = t
    temp = 66
    if t % 2 == 0:
        t = t * (temp * 2 + t % 10)
    else:
        t = t * (temp) + temp/12
    t = t
    flag.append(t)
    d[a] = t
flag.sort()
print(flag)
ff = []
for i in range(len(flag)):
    for j in d:
        if d[j] == flag[i]:
            ff.append(chr(j ^ x[i]))
print("".join(ff))
