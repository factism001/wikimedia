from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bug(models.Model):
    BUG_TYPES = (
        ('error', 'Error'),
        ('new_feature', 'New Feature'),
        ('enhancement', 'Enhancement'),
        ('other', 'Other'),
    )

    STATUS_CHOICES = (
        ('todo', 'To Do'),
        ('inprogress', 'In Progress'),
        ('done', 'Done'),
    )

    description = models.TextField()
    bug_type = models.CharField(max_length=20, choices=BUG_TYPES)
    report_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.description

