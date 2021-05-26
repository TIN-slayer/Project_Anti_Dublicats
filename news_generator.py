from random import randint, choice, shuffle

f = open('old_news.txt', 'w')
alf = []
alf.extend([chr(i) for i in range(ord('a'), ord('z'))])
alf.extend([chr(i) for i in range(ord('A'), ord('Z'))])
alf.extend([' ', ' ', ' ', ' ', ' ', ' ', ' ', ',', ':', '-'])
ans = []
for _ in range(randint(50, 100)):  # кол-во постов
    row = ''
    for _ in range(randint(5, 10)):
        buf = '\n'
        for _ in range(randint(25, 50)):
            buf += choice(alf)
        row += buf
    row += '\n'
    for qtty in range(randint(1, 3)):  # кол-во дубликатов
        new = list(row.replace('\n', '&'))
        n = len(new) * randint(10, 30) // 100  # процент изменённых символов
        s = 0
        while s != n:
            pos = randint(0, len(new) - 1)
            key = choice(alf)
            if new[pos] not in [key, '&', ' ']:
                new[pos] = key
                s += 1
        post = ''.join(new).replace('&', '\n') + '///'
        ans.append(post)
shuffle(ans)
for i in ans:
    f.write(i)
