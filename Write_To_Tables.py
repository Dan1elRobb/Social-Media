import sqlite3

param_user_insert = '''
INSERT INTO
    users (named, age, gender, nationality),
VALUES
    (?,?,?,?);
'''
conn = sqlite3.connect("sm_app.sqlite")
cursor = conn.cursor()
conn.execute((param_user_insert))