from django.db import models
from datetime import datetime

# Create your models here.
class Memo(models.Model):
    idx = models.AutoField(primary_key=True)    #AutoField: 자동증가 메서드
    writer = models.CharField(null=False, max_length=50)
    memo = models.TextField(null=False)
    post_date = models.DateTimeField(default=datetime.now, blank=True)