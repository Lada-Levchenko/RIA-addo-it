# Sample code to dynamically create peewee models

from peewee import *
db = SqliteDatabase('testdb')
dict = {'a': '1', 'b': '2',  'c': '3'}
attrs = {field: CharField() for field in dict}
Dict2db = type('Dict2db', (Model,), attrs)
db.connect()
db.create_table(Dict2db)
