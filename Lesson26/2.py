import sqlite3
from random import choice

con = sqlite3.connect("game.sqlite")
cur = con.cursor()
# que_insert = '''
# INSERT INTO class (name,surname,mark) VALUES
#     ('Даниил', 'Мун',1),
#     ('Денис','Синицын',4),
#     ('Василий','Пупкин',4),
#     ('Саша','Петров',2)




que_create = '''
CREATE TABLE IF NOT EXISTS score (
    id INTEGER PRIMARY KEY,
    name TEXT,
    score_points INTEGER
    '''
