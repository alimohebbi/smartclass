from django.db import models


class Classroom(models.Model):
    name = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    classroom = models.ForeignKey(Classroom)

    def __str__(self):
        return "Schedule for " + self.classroom.name


class TimeSlot:
    schedule = models.ForeignKey(Schedule)
    begin_time = models.TimeField()
    end_time = models.TimeField()


class Reservation(models.Model):
    name = models.CharField(max_length=40)
    classroom = models.ForeignKey(Classroom)
    time_slot = models.ForeignKey(TimeSlot)
    activity = models.CharField(max_length=100)

    def __str__(self):
        return "Class " + self.classroom + " reserved by " + self.name + " for " + self.activity