from django.contrib import admin

# Register your models here.
from .models import Kafedra, Institut, Student, StudentInstance

#admin.site.register(Student)
#admin.site.register(Kafedra)
admin.site.register(Institut)
#admin.site.register(StudentInstance)
# Define the admin class
class KafedrasInstanceInline(admin.TabularInline):
    model = Student

class KafedraAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    inlines = [KafedrasInstanceInline]
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Register the admin class with the associated model
admin.site.register(Kafedra, KafedraAdmin)

# Register the Admin classes for Book using the decorator
class StudentsInstanceInline(admin.TabularInline):
    model = StudentInstance


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('title', 'kafedra', 'display_institut')
    inlines = [StudentsInstanceInline]

# Register the Admin classes for StudentInstance using the decorator

@admin.register(StudentInstance) 
class StudentInstanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('student', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )