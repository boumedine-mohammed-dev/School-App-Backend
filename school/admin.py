from django.contrib import admin
from .models import (Event, FeedbackUser, Grade, Profile, Program, Review, Student, Subject,
    Teacher, Testimonial)
# Register your models here.
admin.site.register(Program)
admin.site.register(Event)
admin.site.register(Grade)
admin.site.register(FeedbackUser)
admin.site.register(Profile)
admin.site.register(Testimonial)
admin.site.register(Review)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)