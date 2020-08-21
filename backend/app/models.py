from django.db import models

class Student(models.Model):
    fname = models.CharField(max_length=140)
    lname = models.CharField(max_length=140)
    course = models.CharField(max_length=140)
    rating = models.IntegerField()

    def __str__(self):
        return self.fname

    class Meta:
        ordering = ['fname']