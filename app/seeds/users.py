from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():
    users = [
        {
            'first_name': 'Demo',
            'last_name': 'User',
            'email': 'demo@magicbnb.io',
            'username': 'demo',
            'password': 'alohamora',
            'house_allegiance': 1,
            'is_admin': False,
            'profile_image': 'https://i.imgur.com/XyqQZ9x.jpg',
            'created_at': new Date(),
            'updated_at': new Date()
        },
        {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 
        }
    ]
    for user in users:
        user = User(**user)
        db.session.add(user)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
