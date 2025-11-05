from tortoise import fields

from .base import BaseModel


class User(BaseModel):
    class Meta:
        table = "users"

    telegram_id = fields.BigIntField(unique=True)

    first_name = fields.CharField(max_length=255, null=True)
    last_name = fields.CharField(max_length=255, null=True)
    username = fields.CharField(max_length=255, null=True)
    phone_number = fields.CharField(max_length=20, null=True)
    language = fields.CharField(max_length=10, default="ua")

    total_debate_games = fields.IntField(default=0)
    average_speaker_points = fields.FloatField(null=True)
