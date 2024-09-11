import sqlite3

con = sqlite3.connect("main.db")
cur = con.cursor()

def create_users_database():
    try:
        cur.execute(f"""CREATE TABLE Users(ID INTEGER UNIQUE, Chat INTEGER)""")
        con.commit()
    except:
        pass


def create_chat_database(id):
    try:
        cur.execute(f"""CREATE TABLE Chat{id}(UserID INTEGER, MessageID INTEGER, Time TIME, Comment TEXT, Link TEXT)""")
        con.commit()
    except:
        pass


def insert_new_user(user_id):
    try:
        cur.execute(f"""INSERT INTO Users (ID, Chat) VALUES ({user_id}, NULL)""")
        con.commit()
    except:
        pass


def connect_user_group(user_id, chat_id):
    cur.execute(f"""UPDATE Users SET Chat = {chat_id} WHERE ID = {user_id}""")
    con.commit()


def insert_group_message(chat_id, user_id, message_id, time, comment, link):
    cur.execute(f"""INSERT INTO Chat{chat_id} VALUES ({user_id}, {message_id}, {time}, "{comment}", "{link}")""")
    con.commit()