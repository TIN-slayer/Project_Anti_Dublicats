import sqlite3

con = sqlite3.connect('data.db')
cur = con.cursor()
cur.execute("DELETE FROM posts")
con.commit()
f = open('old_news.txt')
file = f.read().split('///')[:-1]
print(file)
ans = open('new_news.txt', 'w')
for i in file:
    flag = True
    for row in cur.execute('SELECT text FROM posts'):
        if row[0] == i:
            flag = False
            break
    if flag:
        cur.execute(f"INSERT INTO posts (text) VALUES ('{i}')")
        ans.write(i + '///')
con.commit()
