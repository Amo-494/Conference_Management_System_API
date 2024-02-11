from django.db import models

# Create your models here.
class Conference(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()

    # class Meta:
    #     db_table = 'conference_management_conference'

class Speaker(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()

class Schedule(models.Model):
    conference = models.ForeignKey(Conference, on_delete = models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    title = models.CharField(max_length=255)

class Attendee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    conference = models.ForeignKey(Conference, on_delete = models.CASCADE)

class Feedback(models.Model):
    conference = models.ForeignKey(Conference, on_delete = models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()