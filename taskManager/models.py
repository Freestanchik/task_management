from mongoengine import StringField, IntField, BooleanField, Document, ReferenceField


class Employee(Document):
    name = StringField()
    surname = StringField()
    role = StringField()


# Create your models here.
class Task(Document):
    name = StringField()
    additional_info = StringField()
    priority = IntField(min_value=1, max_value=5)
    role = StringField()
    complete = BooleanField(default=False)
    employee = ReferenceField(Employee)
