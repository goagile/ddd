import sqlite3


conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()

CREATE = 'CREATE TABLE Ideas (IdeaId str, Title str, Description str, Rating str, Votes str, Email str)'

INSERT = "INSERT INTO Ideas VALUES ('{}', '{}', '{}', '{}', '{}', '{}')"


if __name__ == '__main__':
    # c.execute(CREATE)
    # c.execute(INSERT.format(1, 'Make figure', 'Making figures by paper', '3.0', '1', 'xxx@gmail.com'))
    # conn.commit()

    ideas = c.execute('SELECT * FROM Ideas').fetchall()
    print(ideas)
