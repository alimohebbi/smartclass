from django.db import models

# Create your models here.


class Issue (models.Model):
    description = models.CharField
    date = models.DateField
    status = models.BooleanField
    category = models.CharField
    user = None


class IssuePosts (models.Model):
    issue = models.ForeignKey(Issue)
    assignBy = None
    assignTo = None
    date = models.DateField
    details = models.CharField
    file = models.FileField
