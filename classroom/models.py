from django.db import models


class Classroom(models.Model):
    name = models.CharField(max_length=3, primary_key=True)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    classroom = models.OneToOneField(Classroom, related_name="schedule")

    def __str__(self):
        return "Schedule for " + self.classroom.name


class TimeSlot:
    schedule = models.ForeignKey(Schedule, related_name="times")
    begin_time = models.TimeField()
    end_time = models.TimeField()
    is_reserved = models.BooleanField()
    name = models.CharField(max_length=40)
    activity = models.CharField(max_length=100)

    def __str__(self):
        resp = "Time from " + self.begin_time + " to " + self.end_time + " class " + self.schedule.classroom
        if not self.is_reserved:
            resp += " for " + self.activity + " by " + self.name
        return resp