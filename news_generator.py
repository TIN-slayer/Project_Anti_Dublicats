from random import randint, choice, shuffle

f = open('old_news.txt', 'w')
alf = []
alf.extend([chr(i) for i in range(ord('a'), ord('z'))])
alf.extend([chr(i) for i in range(ord('A'), ord('Z'))])
alf.extend([' ', ',', ':', '-'])
ans = []
for _ in range(randint(10, 20)):
    row = ''
    for _ in range(randint(5, 10)):
        buf = '\n'
        for _ in range(randint(25, 50)):
            buf += choice(alf)
        row += buf
    row += '\n///'
    for _ in range(randint(1, 3)):
        ans.append(row)
shuffle(ans)
for i in ans:
    f.write(i)
