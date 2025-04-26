from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    user_id = fields.BigIntField()
    fullname = fields.CharField(max_length=100)
    username = fields.CharField(max_length=50)
    phone_number = fields.CharField(max_length=13)
    is_verified = fields.BooleanField(default=False)

    class Meta:
        table = "users"