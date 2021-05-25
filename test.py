import sqlite3
from fuzzywuzzy import fuzz

con = sqlite3.connect('data.db')
cur = con.cursor()
cur.execute("DELETE FROM posts")
con.commit()
f = open('old_news.txt')
file = f.read().split('///')[:-1]
ans = open('new_news.txt', 'w')
for i in file:
    flag = True
    for row in cur.execute('SELECT text FROM posts'):
        line = row[0]
        # print(fuzz.token_sort_ratio(row[0], i))
        if fuzz.token_sort_ratio(row[0], i) >= 80:
            flag = False
            break
    if flag:
        cur.execute(f"INSERT INTO posts (text) VALUES ('{i}')")
        ans.write(i + '///')
ans.close()
con.commit()
op = open('new_news.txt')
op_ans = op.read().split('///')[:-1]
print(f'Удалено дубликатов: {len(file) - len(op_ans)}')
