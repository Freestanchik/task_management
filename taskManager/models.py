from mongoengine import StringField, IntField, BooleanField, Document


# Create your models here.
class Task(Document):
    name = StringField()
    additional_info = StringField()
    priority = IntField(min_value=1, max_value=5)
    complete = BooleanField(default=False)


class Worker(Document):
    name = StringField()
    surname = StringField()
    role = StringField()
