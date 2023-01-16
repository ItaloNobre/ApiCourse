from django.contrib import admin

from django.contrib import admin
from .models import Course, Assessment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'create', 'update', 'active')

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id_course', 'name', 'email', 'assessment', 'create', 'update', 'active')

