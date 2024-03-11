import sqlite3
from random import choice

con = sqlite3.connect("school.sqlite")
cur = con.cursor()

que_insert = '''
SELECT surname
FROM class
GROUP BY surname
HAVING COUNT(surname) > 1
'''

result = cur.execute(que_insert)
data =result.fetchall()
for line in data:
    print(line)


# que_create = '''
# CREATE TABLE IF NOT EXISTS class (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     surname TEXT,
#     mark INTEGER
# )
# '''

# que_insert = '''
# INSERT INTO class (name,surname,mark) VALUES
#     ('Даниил', 'Мун',1),
#     ('Денис','Синицын',4),
#     ('Василий','Пупкин',4),
#     ('Саша','Петров',2)

# que_insert = '''
# INSERT INTO class (name,surname,mark) VALUES
#     ('{}','{}','{}')
# '''
# pool_name = ('Василий','Денис','Костя','Саша')
# pool_surname = ('Синицин','Соколов','Петров','Крылов')
# pool_nums = tuple(range(2,6))

# for i in range(5):
#     name_insert = choice(pool_name)
#     surname_insert = choice(pool_surname)
#     mark_insert = choice(pool_nums)
#     cur.execute(que_insert.format(name_insert,surname_insert,mark_insert))


con.close()