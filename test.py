from database import Database

db = Database('smdb', load=True,user="Admin",password="password")


db.show_table("meta_users")

db.create_user("nikolakhs","kwdikos","rw","classroom")

db.show_table("meta_users")

db._update()
