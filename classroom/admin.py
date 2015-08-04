from django.contrib import admin
from classroom.models import Classroom, TimeSlot, Schedule


admin.site.register(Classroom)
admin.site.register(Schedule)
admin.site.register(TimeSlot)