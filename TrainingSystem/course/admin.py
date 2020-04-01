from django.contrib import admin

# Register your models here.
from course.models import Course, Subject, Supervisor, CourseSubject, TraineeCourseSubject

admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Supervisor)
admin.site.register(CourseSubject)
admin.site.register(TraineeCourseSubject)
