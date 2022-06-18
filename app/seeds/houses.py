from app.models import db, House

def seed_houses():
    houses = [
      {'name': 'Gryffindor'},
      {'name': 'Slytherin'},
      {'name': 'Hufflepuff'},
      {'name': 'Ravenclaw'}

    ]
    for house in houses:
        house = House(**house)
        db.session.add(house)
    db.session.commit()


def undo_houses():
    db.session.execute('TRUNCATE houses RESTART IDENTITY CASCADE;')
    db.session.commit()


    