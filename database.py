from peewee import *
DATABASE = SqliteDatabase('flick.db')

class Databasee(Model):
	class Meta:
		database = DATABASE