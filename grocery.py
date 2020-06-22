# All grocery list logic
from peewee import *


# todo: setup ability to read (get all) items from db
# todo: setup ability to update items in db
# todo: setup ability to delete items in db

DATABASE = SqliteDatabase('glist.db')

class Glist(Model):
    title = CharField()
    description = TextField()

    class Meta:
        database = DATABASE

    @classmethod
    def create_item(cls, title, description):
        cls.create(
            title=title,
            description=description
        )


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Glist], safe=True)
    DATABASE.close()


if __name__ == '__main__':
    initialize()
    Glist.create_item('Peanut butter', "Large one for Jethro's treats.")