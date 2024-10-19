import database

app_prompt = """


1) Add User.
2) View All Users.
3) Find User by name.
4) Add Run Session
5) View Run Session
6) View All Run Sessions by User
7) Remove Run Session
8) Exit.

"""

def users():
	connection = database.connect()
	database.create_tables(connection)

users()
