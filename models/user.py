from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    user_id = fields.BigIntField(unique=True)
    fullname = fields.CharField(max_length=100)
    username = fields.CharField(max_length=50, unique=True)
    phone_number = fields.CharField(max_length=13, unique=True)
    verification_code = fields.CharField(max_length=6, null=True)
    expires_date = fields.DatetimeField(null=True)
    is_verified = fields.BooleanField(default=False)

    class Meta:
        table = "users"