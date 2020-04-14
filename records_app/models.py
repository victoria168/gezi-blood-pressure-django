from django.db import models

# Create your models here.


class Record(models.Model):
    class Meta:
        db_table = 'record'
        indexes = [
            models.Index(fields=['user_id'], ),
            models.Index(fields=['date', ])
        ]
    user_id = models.IntegerField(null=True)
    date = models.DateTimeField()
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    pulse = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
