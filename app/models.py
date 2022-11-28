from django.db import models
import datetime
from django.core.exceptions import ValidationError
# Create your models here.
def validate_due_date(value):
    if value<datetime.date.today():
        raise ValidationError("due date must be greater than or equal to current date")

class Tags(models.Model):
    tag_name=models.CharField(max_length=10)
    def __str__(self):
        return self.tag_name

class ToDo(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
    due_date=models.DateField(blank=True,validators=[validate_due_date])
    tags=models.ManyToManyField(to=Tags)
    status=models.CharField(max_length=10,choices=(('1','OPEN'),('2','WORKING'),('3','DONE'),('4','OVERDUE')),default="1")
    timestamp=models.DateTimeField(auto_now_add=True)


