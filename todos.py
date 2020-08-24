# All todo logic
from peewee import *


# todo: setup ability to read (get all) items from db
# todo: setup ability to update items in db
# todo: setup ability to delete items in db

DATABASE = SqliteDatabase('todos.db')

class Todos(Model):
    title = CharField()
    location = CharField()

    class Meta:
        database = DATABASE

    @classmethod
    def create_todo(cls, title, location):
        cls.create(
            title=title,
            location=location
        )


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Todos], safe=True)
    DATABASE.close()


if __name__ == '__main__':
    initialize()
    Todos.create_todo('Walk the dog', 'Outside')