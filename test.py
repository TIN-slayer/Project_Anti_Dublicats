import sqlite3
from fuzzywuzzy import fuzz

con = sqlite3.connect('data.db')
cur = con.cursor()
cur.execute("DELETE FROM posts")
con.commit()
f = open('old_news.txt')
file = f.read().split('///')[:-1]
ans = open('new_news.txt', 'w')
dif = []
for i in file:
    flag = True
    for row in cur.execute('SELECT text FROM posts'):
        line = row[0]
        dif.append(fuzz.token_sort_ratio(row[0], i))  # список со процентами схожести
        if fuzz.token_sort_ratio(row[0], i) >= 40:  # процент схожест постов
            print(row[0], i)
            print('ABOBA')
            flag = False
            break
    if flag:
        cur.execute(f"INSERT INTO posts (text) VALUES ('{i}')")
        ans.write(i + '///')
ans.close()
con.commit()
op = open('new_news.txt')
op_ans = op.read().split('///')[:-1]
print()
print(sorted(dif, reverse=True))
print(f'Изначальное кол-во новостей: {len(file)}')
print(f'Конечное кол-во новостей: {len(op_ans)}')
print(f'Удалено дубликатов: {len(file) - len(op_ans)}')
